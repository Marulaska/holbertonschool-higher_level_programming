#!/usr/bin/python3

import sys
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker

user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]

engine = create_engine(f"mysql://{user}:{passwd}@localhost/{db}?charset=utf8")

metadata = MetaData()
states = Table('states', metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String(255)),
               )

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(states).order_by(states.c.id).all()

for row in result:
    print(f"({row.id}, '{row.name}')")

session.close()
