# ![logo](https://user-images.githubusercontent.com/108279441/220420558-12b71945-3e02-4adf-b989-5f8fa1b4c683.png)

# AirBnB Clone - The Console

## Overview

This repository is the first step towards building a complete web application that mirrors the AirBnB site. This phase, known as "The Console," involves creating a command-line storage system to manage the application's data effectively. This custom command interpreter can handle operations such as creating, retrieving, updating, and destroying objects.

## Technical Stack

- **Programming Language**: Python 3
- **Data Storage**: JSON serialization/deserialization
- **Testing**: Unittest module for Python
- **Front-end**: HTML5, CSS3
- **Version Control**: Git and GitHub

## Core Components

### Console

The console is a command-line interpreter that allows management of the application's data. It is built using Python's `cmd` module and supports commands like `create`, `show`, `destroy`, `all`, `update`, and `quit`.

- **Storage Engine**: 
  - Utilizes a custom storage engine using the `FileStorage` class to serialize and deserialize data to and from a JSON file, facilitating data persistence across sessions.
  - Future implementations will integrate database storage systems like MySQL to replace or augment JSON storage.

### Models

Defines classes that manage the data of the application:
- **BaseModel**: The fundamental class that all other models (like `User`, `Place`, and `State`) inherit from. It handles initialization, serialization, and deserialization of instances.

### Web Static

Contains all front-end files:
- HTML files define the structure of the web pages.
- CSS files manage the styling.
- Images and design assets to enhance the UI.

### Unit Testing

Extensive testing is crucial to ensure that all parts of the project function as expected:
- Every class and method has corresponding test cases.
- Utilizes Python’s `unittest` framework to automate testing and validate code.

### File Storage System

Handles the serialization of instances to a JSON file and deserialization back to instances:
- This mechanism allows for an easy transition to more complex database systems in later project stages.

## Compilation and Usage

### Running the Console

Activate the console in interactive mode:

#```bash
$ ./console.py
(hbnb) help

$ echo "help" | ./console.py
Web Static Deployment
To view the static web pages, open the HTML files in a web browser.

Testing
Execute all tests with:
$ python3 -m unittest discover tests

Installation
Clone the repository and navigate to the directory:
$ git clone [Repository URL]
$ cd holbertonschool-AirBnB_clone


### Part 4: Additional Information
#```markdown
## Architectural Design

The project is designed to be scalable and modular, allowing easy updates and maintenance. The separation of concerns is achieved by dividing the application into distinct layers (data handling, business logic, and presentation).

## Contributors

This project is part of the Holberton School curriculum, aimed at introducing students to fundamental programming concepts and preparing them for software engineering careers.

## Authors
Mico Bledsoe - (www.linkedin.com/in/micobledsoe)
Jason Beagle - (https://github.com/JasonBeagl)

Refer to the `AUTHORS` file for more details.
