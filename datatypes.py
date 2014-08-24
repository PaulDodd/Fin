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

global.uuid_null = uuid.UUID(bytes='\x00'*16);

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
    def __init__(self, date = time.strftime("%Y-%m-%d", time.gmtime(0)), category = "None", amt = 0.0, desc = "", tid = global.uuid_null):
        self.__dict__ = {"date": date, "category":category, "amount": amt, "description": desc, "id":str(tid)};

    def __str__(self):
        return json.dumps(self.__dict__); # indent = 4 ?

    def loadFromFile(self, path):
        pass

    def saveToFile(self, path):
        pass

#### end transaction ####

class configuration:
    def __init__(self):
        self.path = "";
        self.bInit = False;
        self.__dict__ = {};

    def loadFromFile(self)
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

