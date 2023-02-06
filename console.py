#!/usr/bin/python3
"""CONSOLE"""

import cmd
import re
import shlex
import models
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
    classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User}

    def do_quit(self, args):
        """quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Empty line or ENTER entered by user should not execute anything"""
        return False

    def do_create(self, args):
        """
        checks if given a class name, if not,
            prints ** class name missing **
        if so, creates new instance and prints its id,
        if class name doesn't exist,
            prints ** class name doesn't exist**
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args in HBNBCommand.classes.keys():
            instance = HBNBCommand.classes[args]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Based on class name, prints string representation of an instance"""
        # to create a list of strings that contain the input
        parse_args = args.split()
        # parses argument into strings
        if len(parse_args) == 0:
            # if no argument is given,
            print("** class name missing **")
            return

        elif len(parse_args) < 2:
            # if parse_args is less than 2, input is incomplete, or
            if (parse_args[0] in HBNBCommand.classes) is True:
                # if the ID is missing is True,
                print("** instance id missing **")
                return
            else:
                # no valid class give,
                print("** class doesn't exist **")
                return

        try:
            if (parse_args[0] in HBNBCommand.classes) is True:
                # string format: 'class.id'
                class_id = '.'.join(parse_args)
                objs = storage.all()
                # search in JSON file with the key 'class.id'
                print(objs[class_id])
            else:
                print("** class doesn't exist **")
        except Exception:
            print("** no instance found **")

    def do_destroy(self, args):
        """Based on an class name, deletes an instance"""
        # checks if args is empty or None
        if args == "" or args is None:
            print("** class name missing **")
        else:
            # checks if args is in class_dict, or less than 2
            parsed = args.split(' ')
            if parsed[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(parsed) < 2:
                print("** instance id missing **")
            else:
                # checks key for proper format, and if its found
                key = "{}.{}".format(parsed[0], parsed[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        Structure: all [class name] or all
        """
        # prints the whole file
        args = shlex.split(args)
        obj_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif args[0] in HBNBCommand.classes:
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance by adding or updating attribute.
        """
        if args == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in self.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
