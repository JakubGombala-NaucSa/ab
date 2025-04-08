import sqlite3
from uuid import uuid4

# Pripojenie do lokalnej databazy
con = sqlite3.connect("databaza.db", check_same_thread=False)
cur = con.cursor()

# Vytvorenie tabulky v databaze
# cur.execute("CREATE TABLE user(id, meno, vek)")

# Zmazanie tabulky - POZOR MOZME STRATIT VSETKY DATA
# cur.execute("DROP TABLE user")

def vylistuj_uzivatelov():
    result = cur.execute("SELECT * from user")
    return result.fetchall()

def nacitaj_uzivatela(user_id):
    result = cur.execute(f"SELECT * from user WHERE id = '{user_id}'")
    return result.fetchone()

def pridaj_uzivatela(meno, vek):
    my_id = uuid4()
    cur.execute(f"INSERT INTO user VALUES ('{my_id}','{meno}',{vek})")
    con.commit()

def aktualizacia_uzivatela(user_id, meno, vek):
    query = f"UPDATE user SET meno = '{meno}', vek = {vek} WHERE id = '{user_id}'"
    cur.execute(query)
    con.commit()

def zmaz_uzivatela(my_id):
    cur.execute(f"DELETE FROM user WHERE id ='{my_id}'")
    con.commit()