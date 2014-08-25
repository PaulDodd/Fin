#
#   datatypes.py
#   Created by Paul Dodd
#   08/24/2014
#

import json
import os
import sys
import time
import uuid

uuid_null = uuid.UUID(bytes='\x00'*16);
time_format = "%Y-%m-%d";

# class time_struct:
#     def __init__(self):
#         self.year = 0;
#         self.month = 0;
#         self.day = 0;
#     def to_time_string(self):
#         tstr = "";
#         return tstr;
#     def to_time_struct(self):
#         return time.;


# use some machine learing to automatically classify categories.
class categoryManager:
    def __init__(self, path):
        self.categories = ["None"] # Add default categories here.
        if os.path.exists(path):
            self.loadFromFile(path);
        else:
            pass

    def loadFromFile(self, path):
        pass

    def saveToFile(self, path):
        pass

#### end categoryManager ####

class transaction:
    def __init__(self, date = time.strftime(time_format, time.gmtime(0)), category = "None", amt = 0.0, desc = "", tid = uuid_null):
        self.__dict__ = {"date": time.strptime(date, time_format), "category":category, "amount": amt, "description": desc, "__transaction__":tid };

    def __str__(self):
        return json.dumps(self.toJSON()); # indent = 4 ?

    def __getitem__(self, name):
        return self.__dict__[name];

    def toJSON(self):
        temp = self.__dict__.copy();
        temp["date"] = time.strftime(time_format, temp["date"]);
        temp["__transaction__"] = str(temp["__transaction__"]);
        return temp;

    def fromJSON(self, temp):
        self.__dict__ = temp.copy();
        self.__dict__["date"] = time.strptime(temp["date"], time_format);
        self.__dict__["__transaction__"] = uuid.UUID(temp["__transaction__"]);


class TransactionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, transaction):
            return obj.toJSON();
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

    @staticmethod
    def as_transaction(dct):
        if "__transaction__" in dct:
            t = transaction();
            t.fromJSON(dct)
            return t;
        return dct;

#### end transaction ####

class configuration:
    def __init__(self):
        self.path = "";
        self.bInit = False;
        self.__dict__ = {};

    def __setitem__(self, name, val):
        self.__dict__[name] = val;
    def __getitem__(self, name):
        return self.__dict__[name];

    def __str__(self):
        return json.dumps(self.__dict__);

    def loadFromFile(self):
        try:
            if not os.path.exists("config.json"):
                print "could not load configuration file"
                return False;
            else:
                cfile = open("config.json", "r");
                self.__dict__ = json.loads(cfile.read());
                cfile.close();
                self.bInit = True;
                return True;
        except:
            print "Error reading config file"
            return False;

    def saveToFile(self):
        try:
            cfile = open("config.json", "w");
            cfile.write(json.dumps(self.__dict__));
            cfile.close();
            return True;
        except:
            print "Error writing config file"
            return False;

#### end configuration ####



















