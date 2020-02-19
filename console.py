#!/bin/usr/python3
""" console for the Holberton AirBnB_clone project """

import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class HBNB command line console """

    prompt = '(hbnb) '

    def emptyline(self):
        """Called when an empty line is entered
        Prints the prompt again
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Executes the EOF (Ctrl -D/ Ctrl-Z) commands on console"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
