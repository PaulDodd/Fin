#
#   database.py
#   Created by Paul Dodd
#   07/10/2014
#

import json
import os
import sys
import time
import uuid
import datatypes
import csv

class transactionManager:
    def __init__(self, config):
        self.transactions = [];
        self.config = config;
        self.bAllowDuplicates = False;

    def addTransaction(self, date = time.strftime(datatypes.time_format, time.gmtime(0)), category = "None", amt = 0.0, desc = ""):
        selection = [lambda x: x["date"] == time.strptime(date, datatypes.time_format), lambda x: x["amount"] == amt, lambda x: x["description"] == desc]
        trans = self.findTransactions(selection);
        bAdd = (not self.bAllowDuplicates and len(trans) == 0) or (self.bAllowDuplicates);
        if(bAdd):
            self.transactions.append(datatypes.transaction(date, category, amt, desc, uuid.uuid4()));
        else:
            print "Found duplicate: ", date, amt, desc;


    def findTransactions(self, selection = []):
        if(len(selection) == 0):
            return self.transactions;

        trans = filter(selection[0], self.transactions);
        for func in selection[1:]:
            trans = filter(func, trans);

        return trans;

    def removeTransaction(self, trans, bDelete = False):
        pass

    def loadFromCSV(self, path):
        with open(path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|');
            titles = [];
            for row in reader:
                if len(titles) == 0:
                    titles = row;
                else:
                    date = time.strftime(datatypes.time_format, time.strptime(row[1], "%m/%d/%Y"));
                    category = "None"; # TODO: try to determine automatically.
                    desc = str(row[3]).replace("\"", "");
                    amt = float(row[4]);
                    self.addTransaction(date, category, amt, desc);

    def loadSelection(self, selection = {}):
        try:
            f = open(self.config["transactions_path"], "r");
            self.transactions = json.loads(f.read(), object_hook = datatypes.TransactionEncoder.as_transaction);
            f.close();
            return True;
        except:
            print "Error could not load file."
            return False;


    def saveSelection(self, selection = {}):
        # save all in one file for now
        try:
            f = open(self.config["transactions_path"], "w");
            f.write(json.dumps(self.transactions, cls=datatypes.TransactionEncoder));
            f.close();
            return True;
        except IOError as e:
            print "Error could not save file." , e.strerror
            return False;

    def printTransactions(self):
        print json.dumps(self.transactions, cls=datatypes.TransactionEncoder);

    def clear(self):
        self.transactions = [];

#### end transactionManager ####



