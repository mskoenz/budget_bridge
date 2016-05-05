#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    28.04.2016 08:29:06 CEST
# File:    to_sql.py

import os
from addon import core

def sql_setup(tbl):
    return """ALTER TABLE {0} ADD num INT;
           """.format(tbl)

def postprocess(path):
    res = dict()
    with open(os.path.join(path, "res.txt"), "r") as f:
        res["num"] = sum(core.to_number(f.readlines()))
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
