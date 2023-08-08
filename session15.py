"""
pet: name , age , weight , breed , gender , createdon
create table Pet(
    pid int primary key auto_increment,
    name text,
    age int,
    weight int,
    breed text,
    gender text,
    cid int,
    createdon datetime,
    FOREIGN KEY (cid) REFERENCES Customer(cid)
    );
"""

import datetime
class Pet:
    def __init__(self):
        self.pid = 0
        self.name = ""
        self.age = 0
        self.weight= ""
        self.breed = 0
        self.gender = ""
        self.cid = 0
        self.createdon = ""

    def read_pet_data(self):
        self.name = input("Enter Pets Name: ")
        self.age = int(input("Enter Pets Age: "))
        self.weight = int(input("Enter Pets Weight: "))
        self.breed = input("Enter Breed: ")
        self.gender = input("Enter Pets Gender(male/female): ").lower()
        # get the date and time
        self.createdon = str(datetime.datetime.today())
        # eliminate milli seconds
        self.createdon=self.createdon[:self.createdon.rindex(".")]

    def get_insert_sql_query(self, cid=""):
        sql = "insert into Pet values(null, '{name}',{age},{weight},"\
        "'{breed}','{gender}',{cid},'{createdon}');".format_map(vars(self))
        return sql
    def get_pets_sql_query(self, cid=""):
        if len(cid) == 0:
            sql = "select * from Pet"
        else:
            sql = "select * from Pet where cid={}".format(cid)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from Pet where pid = '{}'".format(self.pid)
        return sql
"""
    def get_update_sql_query(self):
        sql = "update  pet set( '{name}',{age},{weight},"\
              "'{breed}','{gender}',{cid},'{createdon}');".format_map(vars(self))
        return sql
"""