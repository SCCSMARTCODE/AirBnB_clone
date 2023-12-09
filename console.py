#!/usr/bin/python3
"""This is the command line module"""

import cmd
import datetime
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
import re


class HBNBCommand(cmd.Cmd):
    """Command line class"""

    prompt = "(hbnb) "

    class_box = {
            "BaseModel": BaseModel,
            "State": State,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "User": User
        }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, class_):
        """This creates"""
        class_ = class_.strip()
        """Issue with create function:
                This will update the file at the end of the program
            """
        if len(class_) <= 0 or class_ is None:
            print("** class name missing **")
            return
        elif class_ not in self.class_box.keys():
            print("** class doesn't exist **")
            return
        new_model = self.class_box[class_]()
        storage.new(new_model)
        storage.save()
        print(new_model.id)

    def do_show(self, args):
        """Do_show shows data"""
        args = args.strip()
        args = args.split()
        args[1] = args[1].strip('"')

        if len(args) <= 0 or args is None or args[0] == "":
            print("** class name missing **")
            return
        elif args[0] not in self.class_box.keys():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        print_ = False
        for x in storage.all().keys():
            if args[1] == storage.all()[x]["id"] and \
                    args[0] == storage.all()[x]["__class__"]:

                print_ = True
                break
        a = "created_at"
        b = "updated_at"
        key = "{}.{}".format(args[0], args[1])

        if print_:
            storage_all[key][a] = datetime.datetime.fromisoformat(
                    storage_all[key][a]
            )

            key = "{}.{}".format(args[0], args[1])
            storage_all = storage.all()

            storage_all[key][b] = datetime.datetime.fromisoformat(
                    storage_all[key][b]
            )

            print("[{}] ({})".format(
                args[0],
                args[1]),
                storage.all()["{}.{}".format(args[0], args[1])]
                )
        else:
            print("** no instance found **")
        if print_:
            a = "created_at"
            b = "updated_at"
            key = "{}.{}".format(args[0], args[1])
            storage_all = storage.all()

            storage_all[key][a] = storage_all[key][a].isoformat()

            key = "{}.{}".format(args[0], args[1])
            storage_all = storage.all()

            storage_all[key][b] = storage_all[key][b].isoformat()

    def do_destroy(self, args):
        """This removes or clears data"""
        args = args.strip()
        args = args.split()
        args[1] = args[1].strip('"')

        if len(args) <= 0 or args is None or args[0] == "":
            print("** class name missing **")
            return
        elif args[0] not in self.class_box.keys():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        for x in storage.all().keys():
            if args[1] == storage.all()[x]["id"] and \
                    args[0] == storage.all()[x]["__class__"]:
                """Work to do"""
                del storage.all()[x]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """This print all specified class data"""
        args = args.strip()

        output = []

        for x in storage.all().keys():
            storage_all = storage.all()
            storage_all_x = storage_all[x]
            storage_all_x_created_at = storage_all_x["created_at"]
            storage_all_x["created_at"] = datetime.datetime.fromisoformat(
                    storage_all_x_created_at
                    )

            storage_all = storage.all()
            storage_all_x = storage_all[x]
            storage_all_x_updated_at = storage_all_x["updated_at"]
            storage_all_x["updated_at"] = datetime.datetime.fromisoformat(
                    storage_all_x_updated_at
                    )
        if args:
            if args not in self.class_box.keys() and args != "":
                print("** class doesn't exist **")

                for x in storage.all().keys():
                    storage_all = storage.all()
                    storage_all_x = storage_all[x]
                    storage_all_x_updated_at = storage_all_x["updated_at"]
                    storage_all_x["updated_at"] = datetime.datetime.isoformat(
                            storage_all_x_updated_at
                            )

                    storage_all = storage.all()
                    storage_all_x = storage_all[x]
                    storage_all_x_created_at = storage_all_x["created_at"]
                    storage_all_x["created_at"] = datetime.datetime.isoformat(
                            storage_all_x_created_at
                            )
                return

            if args:
                for x in storage.all().keys():
                    if args in x:
                        """Work to do"""
                        output.append("[{}] ({}) {}".format(
                            args,
                            storage.all()[x]["id"],
                            storage.all()[x]
                            ))

        else:
            for x in storage.all().keys():
                output.append("[{}] ({}) {}".format(
                    storage.all()[x]["__class__"],
                    storage.all()[x]["id"],
                    storage.all()[x]
                    ))
        if output:
            print(output)

        for x in storage.all().keys():
            storage.all()[x]["updated_at"] = datetime.datetime.isoformat(
                    storage.all()[x]["updated_at"]
                    )
            storage.all()[x]["created_at"] = datetime.datetime.isoformat(
                    storage.all()[x]["created_at"]
                    )

    def do_update(self, args):
        """This updates atributes"""
        args = args.strip()
        my_arg = []
        for x in range(len(args)):
            if args[x] != '"' and args[x] != ",":
                my_arg.append(args[x])

        args = "".join(my_arg)
        args = args.split()

        if len(args) != 4:
            return
        if args[0] == '':
            print("** class name missing **")
            return
        elif args[0] not in self.class_box.keys():
            print("** class doesn't exist **")
            return
        elif len(args) <= 1:
            print("** instance id missing **")
            return
        found_instance = False
        for x in storage.all().keys():
            if args[1] == storage.all()[x]["id"] and \
                    args[0] == storage.all()[x]["__class__"]:
                """Work to do"""
                found_instance = True
        if not found_instance:
            print("** no instance found **")
            return
        if len(args) <= 2:
            print("** attribute name missing **")
            return
        if len(args) <= 3:
            print("** value missing **")
            return
        if args[2] in ["id", "created_at", "updated_at"]:
            return

        storage.reload()
        dict_data = storage.all()["{}.{}".format(args[0], args[1])]

        for x in self.class_box:
            if args[0] == x:
                new_updated = self.class_box[args[0]](**dict_data)

                if args[3].count("\"") == 2:
                    args[3] = args[3].strip("\"")
                else:
                    try:
                        args[3] = int(args[3])
                    except ValueError:
                        pass

                new_updated.__dict__.update(
                        {"{}".format(args[2]): "{}".format(args[3])}
                        )

                new_updated.save()
                storage.reload()
                break

    def do_quit(self, arg):
        """This exit the program"""
        return True

    def do_count(self, arg):
        """counts class existence"""
        arg = arg.strip()
        count = 0
        for x in storage.all().keys():
            if x.startswith(arg):
                count += 1
        else:
            print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
