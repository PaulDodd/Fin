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

class transactionManager:
    def __init__(self, config):
        self.transactions = [];

    def addTransaction(self, date = time.strftime("%Y-%m-%d", time.gmtime(0)), category = "None", amt = 0.0, desc = "", tid = global.uuid_null):
        self.transactions.append(datatypes.transaction(date, category, amt, desc, tid));

    def removeTransaction(self, trans, bDelete):
        pass

    def loadSelection(self, selection):
        pass

    def saveSelection(self, selection):
        pass

    def clear(self):
        self.transactions = [];

#### end transactionManager ####



