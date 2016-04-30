#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    28.04.2016 08:29:06 CEST
# File:    to_sql.py

import os
from addon import core, zurkon

def setup_sql(tbl):
    return """ALTER TABLE {0} ADD num INT;
              ALTER TABLE {0} ADD num2 INT;
           """.format(tbl)

def to_dict(path):
    res = dict()
    with open(os.path.join(path, "res.txt"), "r") as f:
        res["num"] = sum(core.to_number(f.readlines()))
        res["num2"] = res["num"]
    return res

def main():
    path = "."
    core.rm_file("zoo.db")
    db = zurkon.SQLiteSupport("zoo.db")
    tbl = "budget_bridge"
    
    if not db.has_table(tbl):
        db.execute("CREATE TABLE {} (m5c TEXT UNIQUE NOT NULL, PRIMARY KEY (m5c))".format(tbl))
        cmd = setup_sql(tbl)
        db.executescript(cmd)
    
    res = to_dict("./")
    res["m5c"] = "12345"
    db.add_dict(tbl, res)
    
    db.commit()
    
if __name__ == "__main__":
    main()
