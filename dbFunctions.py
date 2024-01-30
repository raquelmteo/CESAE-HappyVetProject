"""
THIS PROGRAM WAS CREATED BY
- RAQUEL DE MELO TEÓFILO
- MARIA LUISA FREITAS DE LUCENA
"""

from datetime import datetime

# Loads all appointments informations
def loadAppointmentsData(cursorObject):
    query = f"""SELECT p.id, p.tipo_animal, p.raca, c.id, c.data, c.preco_consulta, t.nome, v.id, v.nome
                FROM consulta c 
                LEFT JOIN pet p ON p.id = c.animal_id
                LEFT JOIN tratamento t ON c.tratamento_id = t.id
                LEFT JOIN veterinario v ON c.veterinario_id = v.id"""
    cursorObject.execute(query)
    return cursorObject.fetchall()

# Gets all appointments informatios by pets ids
def allAppointments(listAppointments):
    appointmentsById = {}
    for appointment in listAppointments:
        appointment = list(appointment)
        petId = appointment[3]
        if petId not in appointmentsById:
            appointmentsById[petId] = appointment
        else:
            appointmentsById[petId].append(appointment[3:])
    return appointmentsById 

# Prints all appointments informations   
def printAllAppointments(dictAppointments):
    print("ALL APPOINTMENTS")
    for key, value in dictAppointments.items():
        if value[-1] is None or value[0] is None:
            pass
        else:
            print(f"""\nAPPOINTMENT Nº {key}:
    DATE: {value[4]}
    VETERINARY: {value[-1]}
    ANIMAL ID: {value[0]}
    ANIMAL TYPE: {value[1]}
    ANIMAL RACE: {value[2]}
    TREATMENT: {value[6]}
    PRICE: {value[5]}€""")

# Gets all appointments informations and prints it
def getAllAppointments(cursorObject):
    appointments = allAppointments(loadAppointmentsData(cursorObject))
    printAllAppointments(appointments)

# Loads all pets informations
def loadPetsData(cursorObject):
    query = f"""SELECT p.id, p.tipo_animal, p.raca, c.id, c.data, c.preco_consulta, t.nome, v.id, v.nome
                FROM pet p
                LEFT JOIN consulta c ON p.id = c.animal_id
                LEFT JOIN tratamento t ON c.tratamento_id = t.id
                LEFT JOIN veterinario v ON c.veterinario_id = v.id"""
    cursorObject.execute(query)
    return cursorObject.fetchall()

# Gets all pets informatios by pets ids
def allPets(listAppointments):
    petsAppointmentsById = {}
    for appointment in listAppointments:
        appointment = list(appointment)
        petId = appointment[0]
        if petId not in petsAppointmentsById:
            petsAppointmentsById[petId] = appointment[1:3]
            petsAppointmentsById[petId].append(appointment[3:])
        else:
            petsAppointmentsById[petId].append(appointment[3:])
    return petsAppointmentsById 

# Prints all pets informations
def printAllPets(dictAppointments):
    print("ALL PETS")
    for key, value in dictAppointments.items(): 
        print(f"\nID: {key}\nTYPE: {value[0]}\nRACE: {value[1]}")
        appointments = value[2:]
        if appointments[0][0] is not None:  
            for appointment in appointments:
                print(f"""APPOINTMENT Nº {appointment[0]}:
    DATE: {appointment[1]}
    VETERINARY: {appointment[-1]}
    TREATMENT: {appointment[3]}
    PRICE: {appointment[2]}€""")
        else:
            print("APPOINTMENTS: 0")

# Gets all pets informations and prints it
def getAllPets(cursorObject):
    pets = allPets(loadPetsData(cursorObject))
    printAllPets(pets)

# Loads all treatment data from database
def loadTreatData(cursorObject):
    query = f"""SELECT *
                FROM tratamento"""
    cursorObject.execute(query)
    result = cursorObject.fetchall()
    return [list(item) for item in result]

# Prints each treatment
def printTreatments(listTreatments):
    print("ALL TREATMENTS OF THE CLINIC\n")
    for treatment in listTreatments:
        print(f"ID: {treatment[0]}\nNAME: {treatment[1]}\nPRICE: {treatment[2]}€\n")

# Gets all treatments and prints it
def getAllTreatments(cursorObject):
    printTreatments(loadTreatData(cursorObject))

# Gets input with a date format
def getDateInput(mensage):
    while True:
        try:
            data_input = input(mensage)
            data = datetime.strptime(data_input, "%Y-%m-%d")
            return data.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid format of date. Please insert a date in the following format: YYYY-MM-DD.")

# Gets all appointments between the prompted dates and indicates how much it was billed
def getAppointmentsByDate(cursorObject):
    initialDate = getDateInput("Insert the initial date: ")
    finalDate = getDateInput("Insert the final date: ")

    query = "SELECT id, data, preco_consulta FROM consulta WHERE data BETWEEN %s AND %s"
    cursorObject.execute(query, (initialDate, finalDate))
    results = cursorObject.fetchall()

    bill = 0

    for result in results:
        print(f"Id da consulta {result[0]}, Data: {result[1]}, Preço: {result[2]}")
        bill += result[2]

    print(f"\nTotal faturado no período: {bill}")

# Gets id of pets and returns into a list
def loadPetsIds(cursorObject):
    cursorObject.execute(f"SELECT id FROM pet")
    result = cursorObject.fetchall()
    return [item[0] for item in result]

# Prompts a valid id of a pet 
def getPetId(cursorObject):
    while True:
        try:
            petId = int(input("Please insert an ID: "))
        except (ValueError, TypeError):
            print("ERROR! Insert a valid ID")
        else: 
            if petId not in loadPetsIds(cursorObject):
                print("ERROR! ID doesn't exist")
            else:
                return petId

# Gets animal data and historic
def loadSpecificPetData(cursorObject,petId):
    query = f"""SELECT p.id, p.tipo_animal, p.raca, c.id, c.data, c.preco_consulta, t.nome, v.id, v.nome
                FROM pet p
                LEFT JOIN consulta c ON p.id = c.animal_id
                LEFT JOIN tratamento t ON c.tratamento_id = t.id
                LEFT JOIN veterinario v ON c.veterinario_id = v.id
                WHERE p.id = {petId}"""
    cursorObject.execute(query)
    return cursorObject.fetchall()

# Prints main animal info
def printAnimalInfo(petData):
    animalId, animalType, animalRace = petData[:3]
    print(f"\nID: {animalId}\nTYPE: {animalType}\nRACE: {animalRace}")

# Prints appointment informations
def printAppointmentInfo(appointmentData):
    for i in range(len(appointmentData)):
            appointmentId = appointmentData[i][0]
            appointmentDate = appointmentData[i][4]
            appointmentVet = appointmentData[i][-1]
            appointmentTreat = appointmentData[i][6]
            appointmentPrice = appointmentData[i][5]
            print(f"""
    APPOINTMENT Nº {appointmentId}:
        DATE: {appointmentDate}
        VETERINARY: {appointmentVet}
        TREATMENT: {appointmentTreat}
        PRICE: {appointmentPrice}€ 
            """)

# Prints all pet data
def printPetData(allPetData):
    petData = allPetData[0]
    if petData[3] is not None:
        printAnimalInfo(petData)
        printAppointmentInfo(allPetData)
        return
    else:
        printAnimalInfo(petData)
        print("APPOINTMENTS: 0")
        return

# Gets information about pet by it's id
def getSpecificPet(cursorObject):
    printPetData(loadSpecificPetData(cursorObject,getPetId(cursorObject)))

# Gets all pets races
def getPetsRaces(cursorObject):
    cursorObject.execute(f"SELECT raca FROM pet")
    result = cursorObject.fetchall()
    return [item[0] for item in result]

# Gets all pets types
def getPetsType(cursorObject):
    cursorObject.execute(f"SELECT tipo_animal FROM pet")
    result = cursorObject.fetchall()
    return [item[0] for item in result]

# Loads all pets with a certain race
def loadPetDataByRace(cursorObject,race):
    query = f"SELECT * FROM pet WHERE raca LIKE (%s)"
    cursorObject.execute(query,(race,))
    return cursorObject.fetchall()

# Loads all pets of a certain type
def loadPetDataByType(cursorObject,type):
    query = f"SELECT * FROM pet WHERE tipo_animal LIKE (%s)"
    cursorObject.execute(query,(type,))
    return cursorObject.fetchall()

# Prompts for animal race
def promptAnimalRace(cursorObject):
    while True:
        try:
            animalRace = input("Please insert a race: ")
        except (ValueError, TypeError):
                print("ERROR! Insert a valid option")
        else: 
            if animalRace not in getPetsRaces(cursorObject):
                print("ERROR! Race doesn't exist")
            else:
                return animalRace

# Prompts for animal type
def promptAnimalType(cursorObject):
    while True:
        try:
            animalRace = input("Please insert a type of animal: ").capitalize()
        except (ValueError, TypeError):
                print("ERROR! Insert a valid option")
        else: 
            if animalRace not in getPetsType(cursorObject):
                print("ERROR! Type of animal doesn't exist")
            else:
                return animalRace

# Prints all animals from a list of animals
def printAllAnimals(allAnimals):
    for animal in allAnimals:
        printAnimalInfo(animal)

# Prints all animals by type
def getAnimalsByType(cursorObject):
    printAllAnimals(loadPetDataByType(cursorObject,promptAnimalType(cursorObject)))

# Prints all animals by race
def getAnimalsByRace(cursorObject):
    printAllAnimals(loadPetDataByRace(cursorObject,promptAnimalRace(cursorObject)))

# Load all veterinaries names and ids
def loadVets(cursorObject):
    cursorObject.execute(f"SELECT id, nome FROM veterinario")
    result = cursorObject.fetchall()
    listVets = []
    for item in result:
        vets = {"id" : item[0], "name" : item[1]}
        listVets.append(vets)
    return listVets

# Gets all vets informations by their IDs
def allVets(listAppointments):
    appointmentsByVetId = {}
    for appointment in listAppointments:
        appointment = list(appointment)
        vetId = appointment[7]
        if vetId not in appointmentsByVetId:
            appointmentsByVetId[vetId] = appointment[8:]
            appointmentsByVetId[vetId].append(appointment[:7])
        else:
            appointmentsByVetId[vetId].append(appointment[:7])
    return appointmentsByVetId 

# Prints all vets informations
def printAllVets(dictAppointments):
    for key, value in dictAppointments.items(): 
        print(f"ID: {key}\nNAME: {value[0]}")
        appointments = value[1:]
        if appointments[0][0] is not None:  
            print("APPOINTMENTS:")
            for appointment in appointments:
                print(f"""  Nº {appointment[3]}:
    DATE: {appointment[4]}
    ANIMAL ID: {appointment[0]}
    ANIMAL TYPE: {appointment[1]}
    ANIMAL RACE: {appointment[2]}
    TREATMENT: {appointment[-1]}
    PRICE: {appointment[-2]}€
    """)
        else:
            print("APPOINTMENTS: 0")

# Prits all veterinaries ids and names
def printVets(listVets):
    print("VETERINARIES OF THE CLINIC:\n")
    for vet in listVets:
        for key, value in vet.items():
            print(f"{key.upper()}: {value}",end="  ")
        print("")

# Prompts a valid name of veterinary and checks if exists in the database
def checkVetName(cursorObject):
    vets = loadVets(cursorObject)
    vetsNames = [vet['name'] for vet in vets]
    printVets(vets)
    while True:
        try:
            vetName = input("\nInsert a name of veterinary: ")
        except(ValueError, TypeError):
            print("ERROR! Insert a valid vame")
        else: 
            if vetName not in vetsNames:
                print("ERROR! Veterinary name doesn't exist in the database")
            else:
                return vetName

# Loads data of a specific veterinary by their id
# Loads data of a specific veterinary by their id
def loadSpecificVet(cursorObject):
    vetName = checkVetName(cursorObject)
    dataInicio = datetime.now().strftime("%Y-%m-%d")
    query = f"""SELECT p.id, p.tipo_animal, p.raca, c.id, c.data, c.preco_consulta, t.nome, v.id, v.nome
                FROM veterinario v
                LEFT JOIN consulta c ON v.id = c.veterinario_id
                LEFT JOIN pet p ON c.animal_id = p.id
                LEFT JOIN tratamento t ON c.tratamento_id = t.id
                WHERE v.nome = %s AND c.data >= %s
                ORDER BY c.data ASC"""
    cursorObject.execute(query, (vetName, dataInicio))

    return cursorObject.fetchall()

# Gets data from specific veterinary and prints it
def getSpecificVet(cursorObject):
    printAllVets(allVets(loadSpecificVet(cursorObject)))

# Prompts a valid name of veterinary and checks if exists in the database
def checkVetId(cursorObject,action):
    vets = loadVets(cursorObject)
    vetsIds = [vet['id'] for vet in vets]
    printVets(vets)
    while True:
        try:
            vetId = int(input(f"\nInsert an id of veterinary to {action}: "))
        except(ValueError, TypeError):
            print("ERROR! Insert a valid id")
        else: 
            if vetId not in vetsIds:
                print("ERROR! Veterinary id doesn't exist in the database")
            else:
                return vetId

# Requests for a valid new veterinary name
def requestNewVetName(id):
    while True:
        try:
            vetName = input(f"\nInsert a new name for the veterinary with id {id}: ")
        except(ValueError, TypeError):
            print("ERROR! Insert a valid id")
        else:
            if len(vetName.split()) >= 2:
                return vetName.title()
            else:
                print("Please enter at least two names")

# Requests for a valid veterinary name
def requesVetName():
    while True:
        name = input("Veterinary name (first name and last name): ")
        if len(name.split()) >= 2:
            return name.title()
        else:
            print("Please enter at least two names")

# Insert data vet table
def insertVet(cursorObject):
    name = requesVetName()
    insertVetQuery = "INSERT INTO veterinario (nome) VALUES (%s)"
    valuesVet = (name,)
    try:
        cursorObject.execute(insertVetQuery, valuesVet)
    except:
        print(f"Veterinary info {name} successfully inserted!")
    finally:
        print("Successfully insert into the database!")
    
# Update data in veterinary table
def updateVet(cursorObject):
    vetId = checkVetId(cursorObject, "UPDATE")
    newName = requestNewVetName(vetId)
    updateQuery = "UPDATE veterinario SET nome = %s WHERE id = %s"
    try:
        cursorObject.execute(updateQuery, (newName, vetId))
    except:
        print("Something went wrong while trying to update")
    finally:
        print("Successfully updated name in the database!")

# Delete veterinary data
def deleteVet(cursorObject):
    vetId = checkVetId(cursorObject,"DELETE")
    deleteVetQuery = "DELETE FROM veterinario WHERE id = %s"
    valuesVet = (vetId,)
    try:
        cursorObject.execute(deleteVetQuery, valuesVet)
    except:
        print("Something went wrong while trying to delete")
    finally:
        print("Successfully deleted veterinary in the database!")

# Checks if prompted pet id is in database
def checkPetId(cursorObject,action):
    petsIds = loadPetsIds(cursorObject)
    getAllPets(cursorObject)
    while True:
        try:
            petId = int(input(f"\nInsert an id of pet to {action}: "))
        except(ValueError, TypeError):
            print("ERROR! Insert a valid id")
        else: 
            if petId not in petsIds:
                print("ERROR! Pet id doesn't exist in the database")
            else:
                return petId

# Insert data pet table
def insertPet(cursorObject):
    typeAnimal = input("Pet type: ")
    race = input("Animal race: ")
    insertPetQuery = "INSERT INTO pet (tipo_animal, raca) VALUES (%s, %s)"
    valuesPet = (typeAnimal, race)
    try:
        cursorObject.execute(insertPetQuery, valuesPet)
    except:
        print("Something went wrong while trying to insert")
    finally:
        print(f"Pet type {typeAnimal} and pet race {race} successfully inserted!")

# Update data in pet table
def updatePet(cursorObject):
    petId = checkPetId(cursorObject, "UPDATE")
    newType = input(f"\nInsert a new type of animal for pet with id {petId}: ")
    newRace = input(f"\nInsert a new race of animal for pet with id {petId}: ")
    updateQuery = "UPDATE pet v SET tipo_animal = %s, raca = %s WHERE id = %s"
    try:
        cursorObject.execute(updateQuery, (newType, newRace, petId))
    except:
        print("Something went wrong while trying to update")
    finally:
        print("Successfully updated name in the database!")

# Delete data pet table
def deletePet(cursorObject):
    petId = checkPetId(cursorObject,"DELETE")
    deletePetQuery = "DELETE FROM pet WHERE id = %s"
    valuesPet = (petId,)
    try:
        cursorObject.execute(deletePetQuery, valuesPet)
    except:
        print("Something went wrong while trying to delete")
    finally:
        print(f"Pet with id {petId} successfully deleted!")

# Check if prompted treatment id is in database
def checkTreatmentId(cursorObject,action):
    treatIds = [element[0] for element in loadTreatData(cursorObject)]
    getAllTreatments(cursorObject)
    while True:
        try:
            treatId = int(input(f"\nInsert an id of a treatment to {action}: "))
        except(ValueError, TypeError):
            print("ERROR! Insert a valid id")
        else: 
            if treatId not in treatIds:
                print("ERROR! Treatment id doesn't exist in the database")
            else:
                return treatId

# Check if the prompted treatment price is valid
def checkTreatPrice():
    while True:
        try:
            price = float(input(f"\nInsert a treatment price: "))
        except(ValueError, TypeError):
            print("ERROR! Insert a valid price")
        else: 
            return price

# Insert data treatment table
def insertTreatment(cursorObject):
    treatName = input("Insert a treatment name: ").capitalize()
    treatPrice = checkTreatPrice()
    insertTreatQuery = "INSERT INTO tratamento (nome, preco) VALUES (%s, %s)"
    valuesTreatment = (treatName, treatPrice)
    try:
        cursorObject.execute(insertTreatQuery, valuesTreatment)
    except:
        print("Something went wrong while trying to insert")
    finally:
        print(f"Treatment {treatName} with price {treatPrice}€ successfully inserted!")

# Update treatment
def updateTreatment(cursorObject):
    treatId = checkTreatmentId(cursorObject,"UPDATE")
    newName = input(f"\nInsert a new name for treament with id {treatId}: ")
    newprice = checkTreatPrice()
    updateQuery = "UPDATE tratamento SET nome = %s, preco = %s WHERE id = %s"
    try:
        cursorObject.execute(updateQuery, (newName, newprice, treatId))
    except:
        print("Something went wrong while trying to update")
    finally:
        print("Successfully updated treatment in the database!")

# Delete treatment
def deleteTreatment(cursorObject):
    treatId = checkTreatmentId(cursorObject,"DELETE")
    deleteQuery = "DELETE FROM tratamento WHERE id = %s"
    valueTreat = (treatId,)
    try:
        cursorObject.execute(deleteQuery, valueTreat)
    except:
        print("Something went wrong while trying to delete")
    finally:
        print(f"Treatment with id {treatId} successfully deleted!")

# Load appointment by vet id and appointment date
def appointmentConsult(cursorObject, veterinario_id, data_consulta):
    query = "SELECT COUNT(*) FROM consulta WHERE veterinario_id = %s AND data = %s"
    values = (veterinario_id, data_consulta)

    cursorObject.execute(query, values)
    count = cursorObject.fetchone()[0]

    return count > 0

# Insert appoinment 
def insertAppointmentData(cursorObject,mysqlConnector):
    try:
        petId = int(input("ID Pet: "))
        vetId = int(input("ID Vet: "))
        treatId = int(input("ID do Treatment: "))
        priceAppoint = float(input("Price: "))

        while True:
            dateHourAppointment = input("Date and hour appointment (YYYY-MM-DD HH:MM): ")
            try:
                data_consulta = datetime.strptime(dateHourAppointment, "%Y-%m-%d %H:%M")
                break 
            except ValueError:
                print("Invalid date and time format. Please enter in the format (YYYY-MM-DD HH:MM)")

        if appointmentConsult(cursorObject, vetId, data_consulta):
            print("We already have an appointment for this time, please enter a new date or time")
            return False
        else:
            insertConsultaQuery = "INSERT INTO consulta (data, preco_consulta, animal_id, veterinario_id, tratamento_id) VALUES (%s, %s, %s, %s, %s)"
            valuesConsulta = (data_consulta, priceAppoint, petId, vetId, treatId)
            try:
                cursorObject.execute(insertConsultaQuery, valuesConsulta)
                print("Data entered successfully!")
                return True
            except mysqlConnector.Error as err:
                print(f"Error when entering data: {err}")
                return False 
    except ValueError:
        print(f"Invalid input. Please enter a valid numeric value.")
        return False

# Delete an appointment from database
def deleteAppointment(cursorObject,mysqlConnector):
    while True:
        try:
            consultaId = int(input("\nEnter the ID you wish to delete: "))
            deleteConsultaQuery = "DELETE FROM consulta WHERE id = %s"
            valuesConsulta = (consultaId,)
            try:
                cursorObject.execute(deleteConsultaQuery, valuesConsulta)
                if cursorObject.rowcount > 0:
                    print("Appointment deleted successfully!")
                    return True
                else:
                    print("Appointment not found.")
                    return False
            except mysqlConnector.Error as err:
                print(f"Error when deleting data: {err}")
                return False
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
            continue