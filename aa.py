import sqlite3
from uuid import uuid4

from pydantic import BaseModel

# Pripojenie do lokalnej databazy
con = sqlite3.connect("databaza.db", check_same_thread=False)
cur = con.cursor()

# Vytvorenie tabulky v databaze
# cur.execute("CREATE TABLE user(id, meno, priezvisko, vek)")

# Zmazanie tabulky - POZOR MOZME STRATIT VSETKY DATA
# cur.execute("DROP TABLE user")

# 1. Vytvorit si validacnu triedu User pomocou kniznice Pydantic a pred pouzitim vstupu zvalidovat data (ak niekomu nesiel na minuluje nainstovalo Pydantic, nech prosim pouziju notebook od Orange)
 
# 2. Pridat jeden novy parameter priezvisko - teda aby ta tabulka mala stlpec navyse a vsetky ostatne funkcie brali aj tento parameter

class Uzivatel():
    def __init__(self, meno, priezvisko, vek):
        if type(meno) != type(""):
            raise Exception()
        self.meno = meno
        self.priezvisko = priezvisko
        self.vek = vek

    def __str__(self):
        return f"{self.meno}, {self.vek}, {self.priezvisko}"

class Uzivatel2(BaseModel):
    meno: str
    priezvisko: str
    vek: int

    def Get_Name(self):
        return self.meno
    def Get_Surname(self):
        return self.priezvisko
    def Get_Age(self):
        return self.vek

    def Set_Name(self, meno):
        self.meno = meno
    def Set_Surname(self, priezvisko):
        self.priezvisko = priezvisko
    def Set_Age(self, vek):
        self.vek = vek


def vylistuj_uzivatelov():
    result = cur.execute("SELECT * from user")
    return result.fetchall()

def nacitaj_uzivatela(user_id):
    result = cur.execute(f"SELECT * from user WHERE id = '{user_id}'")
    return result.fetchone()

def pridaj_uzivatela(meno, priezvisko, vek):
    try:
        my_id = uuid4()
        uzivatel = Uzivatel2(meno=meno, priezvisko=priezvisko, vek=vek)
        cur.execute(f"INSERT INTO user VALUES ('{my_id}','{uzivatel.Get_Name()}','{uzivatel.Get_Surname()}',{uzivatel.Get_Age()})")
        con.commit()
    except Exception as e:
        print("Chyba validacie:", e)
        

def aktualizacia_uzivatela(user_id, meno, priezvisko, vek):
    try:
        uzivatel = Uzivatel2(meno=meno, priezvisko=priezvisko, vek=vek)

        try: 
            u = nacitaj_uzivatela(user_id)
            if u is None:
                raise SyntaxError("ID neexistuje")
        except SyntaxError as e:
            print("Chyba ID:", e)

        query = f"UPDATE user SET meno = '{uzivatel.Get_Name}', vek = {uzivatel.Get_Age}, priezvisko = '{uzivatel.Get_Surname}' WHERE id = '{user_id}'"
        cur.execute(query)
        con.commit()
    except SyntaxError as e:
        print("Chyba ID:", e)
    except Exception as e:
        print("Chyba validacie:", e)


def zmaz_uzivatela(my_id):
    cur.execute(f"DELETE FROM user WHERE id ='{my_id}'")
    con.commit()


# pridaj_uzivatela("Jozef", "Novak", 30)
# pridaj_uzivatela("Anna", "Kovac", "25")

aktualizacia_uzivatela("589a5111-9328-8d1-2cd5d365c86c", "Jozef", "Novak", 12)

uzivatelia = vylistuj_uzivatelov()

for uzivatel in uzivatelia:
    print(uzivatel)
