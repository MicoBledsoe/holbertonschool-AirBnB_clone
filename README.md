# <center>![HolbertonBnB]
(https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

# Project 0x00. AirBnB Clone - The Console

## Purpose

#### 	The objective of this project is to build a command interpreter for managing  objects within the AirBnB clone project. The goals of the project were to learn how to create a Python package, use the cmd module to create a command interpreter, implement unit testing, serialize and deserialize a class, write and read a JSON file, manage datetime, use UUID, handle *args and **kwargs, and handle named arguments in a function. Our goal is to be able to explain these concepts to others without the help of Google.

### Requirements for our Project

-   Allowed editors: vi, vim, emacs
-   All files should end with a new line
-   Must use the unittest module
-   All test files should be Python files (extension: .py)
-   All test files and folders should start with "test_"
-   File organization in the tests folder should match the project organization
-   All your tests should be executed by using this command: python3 -m unittest discover tests
-   All modules, classes, and functions should have documentation
-   We are encouraged to work together on test cases to avoid missing edge cases.


## <center> Examples of how to use the console

###  The console can be used in an interactive or non-interactive mode.

#### Running `./console.py` in terminal will open a prompt that the user can call functions from. For example:

    
		$ ./console.py
		(hbnb) help

		Documented commands (type help <topic>):
		========================================
		EOF  help  quit

		(hbnb) 
		(hbnb) 
		(hbnb) quit
		$

#### Commands may be also be executed non-interactively by piping them into the console. For example


		$ echo "help" | ./console.py
		(hbnb)

		Documented commands (type help <topic>):
		========================================
		EOF  help  quit
		(hbnb) 
		$
		$ cat test_help
		help
		$
		$ cat test_help | ./console.py
		(hbnb)

		Documented commands (type help <topic>):
		========================================
		EOF  help  quit
		(hbnb) 
		$

#### The user may exit the console by using the 'EOF' command, as well as Ctrl+D.

Project completed by [Mico Bledsoe](https://github.com/MicoBledsoe) & [Jason Beagle](https://github.com/JasonBeagle)