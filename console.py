#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand contains the entry point of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """
        quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        print("Goodbye, have a great day!")
        return True

    def emptyline(self):
        """
        Empty line entered by user should not execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
