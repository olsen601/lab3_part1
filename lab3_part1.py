#Lab 3 Part 1
import sqlite3

    global chainsawDb

    global cur


def db_setup():

    global chainsawDb
    global cur

    chainsawDb = sqlite3.connect('chainsaw_juggling_record.db')

    cur = chainsawDb.cursor()

    cur.execute('create table if not exists records (name text, country text, catches int)')


def db_insert_data(name, country, catches):

    global cur

    cur.execute('insert into records values (?, ?, ?)', (name, country, catches))


def db_return_data():

    global chainsawDb

    global cur

    r = cur.execute('select * from records').fetchall()

    return r


def user_input():

    name = input("Enter the name of the record holding chainsaw juggler: ")
    country = input("Enter the chainsaw juggler's country of origin: ")
    catches = int(input("Enter the chainsaw juggler's number of catches: "))

    db_insert_data(name,country,catches)

def main():
    db_setup()
    a = db_return_data()
    print(a)
