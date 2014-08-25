#
#   fin.py
#   Created by Paul Dodd
#   07/10/2014
#

import datatypes
import database as db
import budget

import argparse
import numpy as np

import sys
import os
import json

def main():
    config = datatypes.configuration();
    config["root_path"] = "/Users/Paul/fin_data/";
    config["category_path"] = os.path.join("/Users/Paul/fin_data/", "categories.json");
    config["transactions_path"] = os.path.join("/Users/Paul/fin_data/", "transactions/transactions.json");

#     tm = db.transactionManager(config);
#     tm.loadSelection();
#     tm.loadFromCSV("/Users/Paul/Downloads/Activity.csv");
# #     tm.addTransaction(date="2014-08-22", category="dining", amt = -10.57, desc="BurgerFi");
#     tm.saveSelection();
    report = budget.TransactionReport(config);
    report.createReport();


if __name__ == "__main__":
    main();


