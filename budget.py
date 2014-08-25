#
#   budget.py
#   Created by Paul Dodd
#   07/10/2014
#

import datatypes
import database

import datetime

class TransactionReport:
    def __init__(self, config):
        self.config = config;
        self.database = database.transactionManager(config);
        self.database.loadSelection();

    def __del__(self):
        #self.database.saveSelection();
        pass

    def createReport(self, selection = []):
        trans = self.database.findTransactions(selection);
        total_expense = 0.0;
        total_income = 0.0;
        total_trans = len(trans);
        date_min = trans[0]["date"];
        date_max = trans[0]["date"];

        for t in trans:
            if t["date"] < date_min:
                date_min = t["date"];
            if t["date"] > date_max:
                date_max = t["date"];
            if t["amount"] < 0:
                total_expense+=t["amount"];
            else:
                total_income+=t["amount"]
        dmax = datetime.date(date_max.tm_year, date_max.tm_mon, date_max.tm_mday);
        dmin = datetime.date(date_min.tm_year, date_min.tm_mon, date_min.tm_mday);

        num_days = (dmax-dmin).total_seconds()/(3600*24);

        print "-- Summary -- "
        print "Total Expenses : $ %.2f "%total_expense;
        print "  Total Income : $ %.2f "%total_income;
        print "   Total Saved : $ %.2f "%(total_income + total_expense);
        print "Number of days : %i "%num_days



