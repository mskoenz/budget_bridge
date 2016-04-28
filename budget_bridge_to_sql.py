#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    28.04.2016 08:29:06 CEST
# File:    to_sql.py

import os
from addon import core, zurkon

def to_sql(db, tbl, path, m5c):
    if not db.has_table(tbl):
        db.execute("CREATE TABLE budget_bridge (m5c TEXT not null, num INT, PRIMARY KEY(m5c));")
    res = dict()
    res["m5c"] = m5c
    with open(os.path.join(path, "res.txt"), "r") as f:
        res["num"] = sum(core.to_number(f.readlines()))
    
    db.add_dict(tbl, res)

zurkon.SQLsubscribe["budget_bridge/budget_bridge"]["default"] = to_sql

def main():
    path = "."
    db = zurkon.SQLiteSupport("foo.db")
    
    to_sql(db, "budget_bridge", path, "foobar")
    
    db.commit()
    
if __name__ == "__main__":
    main()
