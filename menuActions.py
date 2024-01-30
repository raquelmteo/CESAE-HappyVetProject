"""
THIS PROGRAM WAS CREATED BY
- RAQUEL DE MELO TEÓFILO
- MARIA LUISA FREITAS DE LUCENA
"""

import mysql.connector
from menuPrints import *
from menuLists import *
from dbFunctions import *

connection = mysql.connector.connect(user='root', host='localhost', database='clinica_happyvet', autocommit=True)
cursorObject = connection.cursor()

def handleAppointmentsMenu():
    clearScreen()
    displayMenu(APPOINTMENT_MENU_OPTIONS, "APPOINTMENTS MENU")
    userOption = getIntegerInput("Insert an option: ", 1, len(APPOINTMENT_MENU_OPTIONS))
    match userOption:
        case 1:
            clearScreen()
            getAllAppointments(cursorObject)
            input("\n(Enter to go back)\n")
        case 2:
            clearScreen()
            getAppointmentsByDate(cursorObject)
            input("\n(Enter to go back)\n")
        case 3:
            clearScreen()
            insertAppointmentData(cursorObject,mysql.connector)
            input("\n(Enter to go back)\n")
        case 4:
            clearScreen()
            getAllAppointments(cursorObject)
            deleteAppointment(cursorObject,mysql.connector)
            input("\n(Enter to go back)\n")
        case 5:
            return
            
def handlePetsMenu():
    clearScreen()
    displayMenu(PET_MENU_OPTIONS, "PET MENU")
    userOption = getIntegerInput("Insert an option: ", 1, len(PET_MENU_OPTIONS))
    match userOption:
        case 1:
            clearScreen()
            getAllPets(cursorObject)
            input("\n(Enter to go back)\n")
        case 2:
            clearScreen()
            getSpecificPet(cursorObject)
            input("\n(Enter to go back)\n")
        case 3:
            clearScreen()
            getAnimalsByRace(cursorObject)
            input("\n(Enter to go back)\n")
        case 4:
            clearScreen()
            getAnimalsByType(cursorObject)
            input("\n(Enter to go back)\n")
        case 5:
            clearScreen()
            insertPet(cursorObject)
            input("\n(Enter to go back)\n")    
        case 6:
            clearScreen()
            updatePet(cursorObject)
            input("\n(Enter to go back)\n")  
        case 7:
            clearScreen()
            deletePet(cursorObject)
            input("\n(Enter to go back)\n")   
        case 8:
            return

def handleVetMenu():
    clearScreen()
    displayMenu(VETERINARY_MENU_OPTIONS, "VETERINARY MENU")
    userOption = getIntegerInput("Insert an option: ", 1, len(VETERINARY_MENU_OPTIONS))
    match userOption:
        case 1:
            clearScreen()
            printVets(loadVets(cursorObject))
            input("\n(Enter to go back)\n")
        case 2:
            clearScreen()
            getSpecificVet(cursorObject)
            input("\n(Enter to go back)\n")
        case 3:
            clearScreen()
            insertVet(cursorObject)
            input("\n(Enter to go back)\n")
        case 4:
            clearScreen()
            updateVet(cursorObject)
            input("\n(Enter to go back)\n")
        case 5:
            clearScreen()
            deleteVet(cursorObject)
            input("\n(Enter to go back)\n")
        case 6:
            return

def handleTreatMenu():
    clearScreen()
    displayMenu(TREATMENT_MENU_OPTIONS, "TREATMENT MENU")
    userOption = getIntegerInput("Insert an option: ", 1, len(TREATMENT_MENU_OPTIONS))
    match userOption:
        case 1:
            clearScreen()
            getAllTreatments(cursorObject)
            input("\n(Enter to go back)\n")
        case 2:
            clearScreen()
            insertTreatment(cursorObject)
            input("\n(Enter to go back)\n")
        case 3:
            clearScreen()
            updateTreatment(cursorObject)
            input("\n(Enter to go back)\n")
        case 4:
            clearScreen()
            deleteTreatment(cursorObject)
            input("\n(Enter to go back)\n")
        case 5:
            return


def handleUserOption():
    while True:
        clearScreen()
        displayMenu(MAIN_MENU_OPTIONS, "VETERINARY CLINIC")
        userOption = getIntegerInput("Insert an option: ", 1, len(MAIN_MENU_OPTIONS))
        match userOption:
            case 1:
                handleAppointmentsMenu()
            case 2:
                handlePetsMenu()
            case 3:
                handleVetMenu()
            case 4:
                handleTreatMenu()
            case 5:
                return

try:
    handleUserOption()

finally:
    cursorObject.close()
    connection.close()
