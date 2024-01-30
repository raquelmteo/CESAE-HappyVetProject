# HappyVet Veterinary Clinic Management System

Welcome to the HappyVet Management System! This Python project integrates MySQL with Python using the `mysql_connector` library. The system efficiently manages animal consultations, veterinary information, treatments, and related data.

## Database Structure

The MySQL database, named `clinica_happyvet`, consists of the following tables:

### 1. Table `consulta`

- Fields:
  - `id` (Primary Key)
  - `data` (Date and time of consultation)
  - `preco_consulta` (Consultation price)
  - `animal_id` (Foreign Key referencing `pet` table)
  - `veterinario_id` (Foreign Key referencing `veterinario` table)
  - `tratamento_id` (Foreign Key referencing `tratamento` table)

### 2. Table `pet`

- Fields:
  - `id` (Primary Key)
  - `tipo_animal` (Type of animal)
  - `raca` (Breed of the animal)

### 3. Table `tratamento`

- Fields:
  - `id` (Primary Key)
  - `nome` (Name of the treatment)
  - `preco` (Price of the treatment)

### 4. Table `veterinario`

- Fields:
  - `id` (Primary Key)
  - `nome` (Name of the veterinarian)

## Getting Started

1. Set up a MySQL database using XAMPP.
2. Execute the provided SQL dump in PHPMyAdmin to manage data.

## Prerequisites

- `mysql-connector-python` (version 8.0.28): Library for connecting Python to MySQL databases.
- `datetime`: Python module for date and time handling.

## Key Features

Appointment Management: Easily view, insert, and delete appointments. The system allows listing all appointments, appointments by date, and supports the addition and removal of appointments.

Pet Management: Facilitates the handling of pet-related data, including listing all pets, viewing the historical records of a specific pet, listing pets by race or type, and managing pet records through insertion, update, and deletion.

Veterinary Management: Enables comprehensive management of veterinary information, including listing all veterinaries, displaying data for a specific veterinary, and managing veterinary records through insertion, update, and deletion.

Treatment Management: Provides functionality to handle treatments, allowing users to list all treatments and manage treatment records through insertion, update, and deletion.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and suggestions are highly appreciated.
