#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
import json
import shlex
import string
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

class HBNBCommand(cmd.Cmd):
    '''
        Contains the entry point of the command interpreter.
    '''

    cls_names = ["BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"]

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        '''
            Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        '''
            Exits after receiving the EOF signal.
        '''
        return True

    def do_create(self, args):
        '''
            Create a new instance of class BaseModel and saves it
            to the JSON file.
        '''
        if args == "":
            print("** class name missing **")
        else:
            acceptable_cls = 0
            split_args = args.split()
            for item in HBNBCommand.cls_names:
                if item == split_args[0]:
                    inst = eval(split_args[0])()
                    inst.save()
                    print(inst.id)
                    acceptable_cls = 1
            if (acceptable_cls != 1):
                print("** class doesn't exist **")
                return
            for param in split_args:
                if (param is not split_args[0]):
                    HBNBCommand.handle_param(param, split_args[0], inst.id)

    def handle_param(param, cls_name, instance_id):
        if (param.count('=') != 1):
            return

        name, eq, value = param.partition('=')

        if "\"" in name:
            return

        if "\'" in name:
            return

        int_chars = set(string.digits + '-')
        flo_chars = set(string.digits + '.' + '-')

        if ((set(value) <= int_chars) and (value.count('-') < 2) and
                                          (value.find('-') < 1)):
            value = int(value)
        elif ((set(value) <= flo_chars) and (value.count('.') == 1)
              and (value.count('-') < 2) and (value.find('-') < 1)):
            value = float(value)
        elif (value[0] == '"') and (value[-1] == '"'):
            value = value[1:-1]
            quote_pos = value.find('"')
            if quote_pos != -1:
                if value[quote_pos - 1] != '\\':
                    return
            value = value.replace("_", " ")
            value = value.replace('\\"', '"')
            value = value.replace('\\\\', '\\')
        else:
            return

        storage.reload()
        key = cls_name + '.' + instance_id
        obj_dict = storage.all()
        obj_value = obj_dict[key]

        setattr(obj_value, name, value)
        obj_value.save()

    def add_param():
        pass

    def do_show(self, args):
        '''
            Print the string representation of an instance baed on
            the class name and id given as args.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        '''
            Deletes an instance based on the class name and id.
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]

        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        '''
            Prints all string representation of all instances
            based or not on the class name.
        '''
        obj_list = []

        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)

        print(obj_list)

    def do_update(self, args):
        '''
            Update an instance based on the class name and id
            sent as args.
        '''

        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):
        '''
            Prevents printing anything when an empty line is passed.
        '''
        pass

    def do_count(self, args):
        '''
            Counts/retrieves the number of instances.
        '''
        obj_list = []

        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        '''
            Catches all the function names that are not expicitly defined.
        '''
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    '''
        Entry point for the loop.
    '''
    HBNBCommand().cmdloop()
