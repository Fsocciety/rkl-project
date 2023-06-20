import sqlite3
import os
import json
import read_excel


def db_json_mapper(tuple_reports):
    json_reports = []
    for json_report in tuple_reports:
        report = {
            "broj": json_report[1],
            "datum": json_report[2],
            "posiljalac": json_report[3],
            "porucilac": json_report[4],
            "primalac": json_report[5],
            "artikal": json_report[6],
            "prevoznik": json_report[7],
            "registracija": json_report[8],
            "vozac": json_report[9],
            "bruto": json_report[10],
            "tara": json_report[11],
            "neto": json_report[12],
        }
        json_reports.append(report)
    return json_reports


def get_resources():
    conn = sqlite3.connect('./instance/izvestaj.db')
    cur = conn.cursor()
    res = cur.execute("select * from izvestaj;")
    return db_json_mapper(res)



def save(file_loc):
    # if filename in os.listdir('./input'):
    #     print('POSTOJI')
    conn = sqlite3.connect('./instance/izvestaj.db')
    cur = conn.cursor()
    reports = read_excel.read(file_loc)
    cur.executemany("""
    INSERT INTO izvestaj(
        'broj', 
        'datum', 
        'posiljalac', 
        'porucilac', 
        'primalac', 
        'artikal', 
        'prevoznik', 
        'registracija', 
        'vozac', 
        'bruto', 
        'tara', 
        'neto'
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", reports)
    print("Successfuly added")
    conn.commit()


def delete(file_name):
    conn = sqlite3.connect('./instance/izvestaj.db')
    cur = conn.cursor()
    reports = read_excel.read(f'./input/{file_name}')
    for item in reports:
        cur.execute(f"DELETE FROM izvestaj WHERE broj = {item[0]}")
    print('Successfuly deleted')
    conn.commit()


def select_date(d_from, d_to):
    conn = sqlite3.connect('./instance/izvestaj.db')
    cur = conn.cursor()
    p = []
    x = ['broj=dsaf', 'test=nesto']
    x = ' and '.join(x)

    query = 'SELECT * FROM izvestaj'
    if p:
        query += where(p)
    for item in cur.execute(query):
        print(item)
    conn.close()

# select_date(5874, 5910)

def select_from(args):
    conn = sqlite3.connect('./instance/izvestaj.db')
    cur = conn.cursor()

    p = []
    for k, v in args.items():
        if k == 'datumStart':
            p.append(f"datum > '{v}'")
        if k == 'datumEnd':
            p.append(f"datum < '{v}'")
        if k == 'broj':
            p.append(f"{k} = '{v}'")
        if k == 'posiljalac':
            p.append(f"{k} = '{v}'")
        if k == 'porucilac':
            p.append(f"{k} = '{v}'")
        if k == 'primalac':
            p.append(f"{k} = '{v}'")
        if k == 'prevoznik':
            p.append(f"{k} = '{v}'")
        if k == 'artikal':
            p.append(f"{k} = '{v}'")
        if k == 'prevoznik':
            p.append(f"{k} = '{v}'")
        if k == 'registracija':
            p.append(f"{k} = '{v}'")
    
    final = ' and '.join(p)
    print(final)
    if p:
        sql = f"SELECT * FROM izvestaj WHERE {final} ORDER BY datum DESC"
    else:
        sql = "SELECT * FROM izvestaj ORDER BY datum desc"

    res = cur.execute(sql)
    return db_json_mapper(res)


conn = sqlite3.connect('./instance/izvestaj.db',  check_same_thread=False)
cur = conn.cursor()
def select_posiljalac():
    return cur.execute('SELECT DISTINCT posiljalac FROM izvestaj ORDER BY posiljalac ASC').fetchall()

def select_porucilac():
    return cur.execute('SELECT DISTINCT porucilac FROM izvestaj ORDER BY porucilac ASC').fetchall()

def select_primalac():
    return cur.execute('SELECT DISTINCT primalac FROM izvestaj ORDER BY primalac ASC').fetchall()

def select_artikal():
    return cur.execute('SELECT DISTINCT artikal FROM izvestaj ORDER BY artikal ASC').fetchall()

def select_prevoznik():
    return cur.execute('SELECT DISTINCT prevoznik FROM izvestaj ORDER BY prevoznik ASC').fetchall()
    
def select_registracija():
    return cur.execute('SELECT DISTINCT registracija FROM izvestaj ORDER BY registracija ASC').fetchall()


def currentDate():
    res = cur.execute('SELECT DISTINCT datum FROM izvestaj').fetchall()
    temp = []
    for i in res:
        temp.append(i[0])
    temp = sorted(temp, reverse=True)
    print(temp)
    return temp