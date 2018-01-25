#Lab 3 Part 1
import sqlite3

global chainsawDb
global cur

global count
global update_id

def db_setup():

    global chainsawDb
    global cur
    global count

    chainsawDb = sqlite3.connect('chainsaw_juggling_record.db')

    cur = chainsawDb.cursor()

    cur.execute('create table if not exists records (id, name text, country text, catches int)')

    count = count()

    return count


def menu():

    '''Display choices for user, return user selection'''

    print('''
        1. View Records
        2. Add Record
        3. Search and Update
        4. Delete Record
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def handle_choice(choice):

    '''Handle user selection and call function needed'''

    if choice == '1':
        print_records(db_return_data())

    elif choice == '2':
        add_record(True)

    elif choice == '3':
        search_record()

    elif choice == '4':
        delete_record()

    elif choice == 'q':
        db_close()

    else:
        print("Please enter a valid selection")


def print_records(records):

    for record in records:
        print(record)


def db_return_data():

    global chainsawDb
    global cur

    r = cur.execute('select * from records').fetchall()

    return r

def count():

    global count

    count = len(db_return_data())

    return count


def add_record(bool):

    name = input("Enter the name of the record holding chainsaw juggler: ")
    country = input("Enter the chainsaw juggler's country of origin: ")
    catches = int(input("Enter the chainsaw juggler's number of catches: "))

    if bool == True:
        db_insert_data(name,country,catches)

    elif bool == False:
        db_update_data(name,country,catches)


def db_insert_data(name, country, catches):

    global chainsawDb
    global cur
    global count

    count +=1
    id = count

    cur.execute('insert into records values (?, ?, ?, ?)', (id, name, country, catches))
    chainsawDb.commit()



def search_record():

    find = input("Enter a search term: ")

    records = db_return_query_data(find)

    if len(records) > 0:
        print_records(records)
        update_record()



def update_record():

    global count
    global update_id

    update_id = int(input("Enter the id number of the record to update: "))


    if update_id > 0 and update_id <= count:
        add_record(False)


def db_update_data(name,country,catches):

    global chainsawDb
    global cur
    global update_id

    cur.execute('update records set name = ?, country = ?, catches = ? where id = ?', (name, country, catches, update_id))
    chainsawDb.commit()


def db_return_query_data(find):

    global chainsawDb
    global cur

    s = cur.execute("select * from records where name like ? or country like ? or catches like ?", (find, find, find)).fetchall()

    return s


def delete_record():
    global count

    delete_id = int(input("Enter the id number of the record to delete: "))

    db_delete_data(delete_id)


def db_delete_data(delete_id):

    global chainsawDb
    global cur

    cur.execute('DELETE FROM records WHERE id = ?', (delete_id,))

    chainsawDb.commit()


def db_close():

    global chainsawDb

    chainsawDb.commit()
    chainsawDb.close()

    print('Database Closed')


def main():
    db_setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = menu()
        handle_choice(choice)

main()
