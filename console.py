#!/usr/bin/python3
""" Command line console for HBnb """
import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.__init__ import storage
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    # working for db - create(brought from partner proj)
    # working for db - destroy(brought from partner proj)
    # working for db - show
    # working for db - all
    # working for db - update

    # Fixed EOF, quit, and emptyline
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        print()
        exit()

    def emptyline(self):
        """ overwriting the emptyline method """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_create(self, args):
        """ Create an object of any class
        """

        if not args:
            print("** class name missing **")
            return
        cmd_args = args.strip()
        cmd_args = cmd_args.split(" ")
        model = cmd_args[0]
        # if command doesnt start with a class
        if model not in classes:
            print("** class doesn't exist **")
            return
        # if args has no attr setting (create Place)
        if len(cmd_args) < 2 and model != "State":
            return
        i = 0
        tok_args = cmd_args[1:]
        d = {}
        while i < len(tok_args):
            if tok_args[i] and '=' in tok_args[i]:
                dic_args = tok_args[i].split("=")
                value = dic_args[1]
                attr = dic_args[0]
                # remove all ", ', and _
                value =\
                    value.replace('"', '').replace("'", '').replace("_", ' ')
                # Check if called class has attibute passed in.
                # If so, cast new value to the existing attribute type
                if hasattr(classes[model], attr):
                    class_attribute = getattr(classes[model], attr)
                    if type(class_attribute) is int:
                        value = int(value)
                    elif type(class_attribute) is float:
                        value = float(value)
                    d.update({attr: value})
            i += 1
        required_attrs = []
        # get non nullable attributes that have no default
        for column in classes[model].__table__.columns:
            # if attr is not nullable and has no default set
            if not column.nullable and\
                column.default is None and\
                    not column.primary_key:
                required_attrs.append(column.name)
        count = 0
        # Check if new object has all required non nullable attributes
        for attr in d:
            if attr in required_attrs:
                count += 1
        if count < len(required_attrs):
            print(f"Error: must fill all required attrs {required_attrs}")
            return

        new_instance = classes[model](**d)
        print(new_instance.id)
        new_instance.save()

    #### do_create method ryan gave us

    # def _key_value_parser(self, args):
    #     """creates a dictionary from a list of strings"""
    #     new_dict = {}
    #     for arg in args:
    #         if "=" in arg:
    #             kvp = arg.split('=', 1)
    #             key = kvp[0]
    #             value = kvp[1]
    #             if value[0] == value[-1] == '"':
    #                 value = shlex.split(value)[0].replace('_', ' ')
    #             else:
    #                 try:
    #                     value = int(value)
    #                     try:
    #                         value = float(value)
    #                     except Exception:
    #                         continue
    #             new_dict[key] = value
    #     return new_dict

    # def do_create(self, arg):
    #     """Creates a new instance of a class"""
    #     args = arg.split()
    #     if len(args) == 0:
    #         print("** class name missing **")
    #         return False
    #     if args[0] in classes:
    #         new_dict = self._key_value_parser(args[1:])
    #         instance = classes[args[0]](**new_dict)
    #     else:
    #         print("** class doesn't exist **")
    #         return False
    #     print(instance.id)
    #     instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            for k, v in storage.all().items():
                if key == k:
                    print("Deleting")
                    storage.delete(v)
                    storage.save()
        except KeyError:
            print("** no instance found **")

    ### do_destroy Ryan gave us

    # def do_destroy(self, arg):
    #     """Deletes an instance based on the class and id"""
    #     args = shlex.split(arg)
    #     if len(args) == 0:
    #         print("** class name missing **")
    #     elif args[0] in classes:
    #         if len(args) > 1:
    #             key = args[0] + "." + args[1]
    #             if key in models.storage.all():
    #                 models.storage.all().pop(key)
    #                 models.storage.save()
    #             else:
    #                 print("** no instance found **")
    #         else:
    #             print("** instance id missing **")
    #     else:
    #         print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in classes:
            obj_dict = storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value
            Ex: update State id name value
        """
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
