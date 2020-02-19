#!/usr/bin/python3
""" console for the Holberton AirBnB_clone project """

import shlex
import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ class HBNB command line console """

    prompt = '(hbnb) '
    group_class = {'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                   'Review'}

    def emptyline(self):
        """
        Called when an empty line is entered
        Prints the prompt again
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Executes the EOF (Ctrl -D/ Ctrl-Z) commands on console"""
        return True

    def do_create(self, arg):
        """ Save in the json file and print the ID """
        if self.group_class.get(arg):
            obj = self.group_class[arg]()
            print("{}".format(getatt(obj, 'id')))
            obj.save()
        elif not arg:
            print("** class name missing **")
        elif arg not in self.group_class:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        _line = shlex.split(arg)
        if len(_line) == 0:
            print("** class name missing **")
        elif _line[0] not in self.group_class:
            print("** class doesn't exist **")
        elif len(_line) == 1:
            print("** instance id missing **")
        elif len(_line) == 2:
            key = _line[0] + "." + _line[1]
            ob = storage.all()
            if ob.get(key):
                print(ob[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id. """
        _line = shlex.split(arg)
        if len(_line) == 0:
            print("** class name missing **")
            return
        elif _line[0] not in self.group_class:
            print("** class doesn't exist **")
            return
        elif len(_line) == 1:
            print("** instance id missing **")
            return
        else:
            objects = storage.all()
            key = "{}.{}".format(_line[0], _line[1])
            if key not in objects.keys():
                print("** no instance found **")
                return
            else:
                objects.pop(key)
                storage.save()
                return

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        objects = storage.all()
        _list = []
        if arg:
            if arg in self.group_class:
                for key, v in objects.items():
                    splitkey = key.split(".")
                    if splitkey[0] == arg:
                        _list.append(str(v))
            else:
                print("** class doesn't exist **")
        else:
            for v in objects.values():
                _list.append(str(v))
        if _list != []:
            print(_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name
        and id by adding or updating attribute.
        """
        _line = shlex.split(arg)
        if len(_line) == 0:
            print("** class name missing **")
        elif _line[0] not in self.group_class:
            print("** class doesn't exist **")
        elif len(_line) == 1:
            print("** instance id missing **")
        elif len(_line) == 2:
            if storage.all().get(_line[0] + "." + _line[1]):
                print("** attribute name missing **")
            else:
                print("** no instance found **")
        elif len(_line) == 3:
            print("** value missing **")
        else:
            if _line[0] in self.group_class:
                key = _line[0] + "." + _line[1]
                objects = storage.all()
                if key in objects:
                    value = objects.get(key)
                    try:
                        attr = getattr(value, _line[2])
                        setattr(value, _line[2], type(attr)(_line[3]))
                    except:
                        setattr(value, _line[2], _line[3])
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
