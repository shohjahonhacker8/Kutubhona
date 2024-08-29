import sqlite3
from sqlite3 import Error


class DbManager:

    def __init__(self):
        self.open_db()
        self.create_table()

    def open_db(self):
        try:
            self.con = sqlite3.connect('kutubhona.sqlite')
            self.cursor = self.con.cursor()
            print("Database is created")
        except Error:
            print(Error)

    def create_table(self):
        cursor = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS kurs(
              id integer PRIMARY KEY AUTOINCREMENT,
              nomi TEXT
            );
        """
        cursor.execute(sql)
        sql = """
        CREATE TABLE IF NOT EXISTS talabalar(
          id integer PRIMARY KEY AUTOINCREMENT,
          ismi TEXT,
          kurs_id INTEGER,
          FOREIGN KEY(kurs_id) REFERENCES kurs(id)
        );
        """
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS kitoblar(
                  id integer PRIMARY KEY AUTOINCREMENT,
                  nomi TEXT,
                  muallifi TEXT,
                  soni INTEGER
                );
        """
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS olingan_kitoblar(
          id integer PRIMARY KEY AUTOINCREMENT,
          olingan_sana TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          beriladigan_sana TIMESTAMP,
          talaba_id INTEGER,
          kitob_id INTEGER,
          FOREIGN KEY(talaba_id) REFERENCES talabalar(id),
          FOREIGN KEY(kitob_id) REFERENCES kitoblar(id)
        );"""
        cursor.execute(sql)

    # Talaba CRUD
    # Read - o'qish
    def talabalar(self):
        sql = """SELECT t.id[talaba_id], t.ismi, k.nomi, k.id[kurs_id]
                    FROM talabalar t
                    LEFT JOIN kurs k ON k.id = t.kurs_id"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def talabalarni_top(self, keyword=""):
        sql = f"""SELECT t.id[talaba_id], t.ismi
                    FROM talabalar t
                    WHERE t.ismi like "{keyword}%"
                    """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    # Read - o'qish
    def talaba(self, id):
        sql = """SELECT id, ismi, kurs_id FROM talabalar WHERE id=?"""
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchone()
        return rows

    # Create - kiritish
    def talaba_kirit(self, ismi, kurs_id):
        sql = """INSERT INTO talabalar(ismi, kurs_id) VALUES(?,?)"""
        self.cursor.execute(sql, (ismi, kurs_id))
        self.con.commit()
        return self.cursor.lastrowid

    # Update - yangilash
    def talaba_yangila(self, id, ismi, kurs_id):
        sql = """UPDATE talabalar SET ismi=?, kurs_id=? WHERE id=?"""
        self.cursor.execute(sql, (ismi, kurs_id, id))
        self.con.commit()

    # Delete - o'chirish
    def talaba_ochir(self, id):
        sql = """DELETE FROM talabalar WHERE id=?"""
        self.cursor.execute(sql, (id,))
        self.con.commit()

    # Kurs jadvali
    def kurs(self):
        sql = """SELECT id, nomi FROM kurs        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def kurslar(self, id):
        sql = """SELECT id, nomi FROM kurs WHERE id=?"""
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        return rows

    def kurs_kirit(self, nomi):
        sql = """INSERT INTO kurs(nomi) VALUES(?)"""
        self.cursor.execute(sql, (nomi,))
        self.con.commit()
        return rows

    def kurs_yangila(self, id, nomi):
        sql = """UPDATE kurs SET nomi=? WHERE id=?"""
        self.cursor.execute(sql, (nomi, id))
        self.con.commit()
        return rows

    def kurs_ochir(self, id):
        sql = """DELETE FROM kurs WHERE id=?"""
        self.cursor.execute(sql, (id,))
        self.con.commit()
        return rows

    # Kitoblar jadvali
    def kitoblar(self):
        sql = """SELECT id, nomi, muallifi, soni FROM kitoblar        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def kitobni_top(self, keyword=""):
        sql = f"""SELECT id, nomi
                    FROM kitoblar 
                    WHERE kitoblar.nomi like "{keyword}%"
                    """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def kitob(self, id):
        sql = """SELECT id, nomi, muallifi, soni FROM kitoblar WHERE id=?"""
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        return rows

    def kitob_kirit(self, nomi, muallifi, soni):
        sql = """INSERT INTO kitoblar(nomi, muallifi, soni) VALUES(?,?,?)"""
        self.cursor.execute(sql, (nomi, muallifi, soni))
        self.con.commit()
        return self.cursor.lastrowid

    def kitob_yangila(self, id, nomi, muallifi, soni):
        sql = """UPDATE kitoblar SET nomi=?, muallifi=?, soni=? WHERE id=?"""
        self.cursor.execute(sql, (nomi, muallifi, soni, id))
        self.con.commit()

    def kitob_ochir(self, id):
        sql = """DELETE FROM kitoblar WHERE id=?"""
        self.cursor.execute(sql, (id,))
        self.con.commit()

    # Olingan_kitoblar jadvali
    def olingan_kitoblar(self):
        sql = """SELECT id, olingan_sana, beriladigan_sana, talaba_id, kitob_id FROM olingan_kitoblar        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def olingan_kitob(self, id):
        sql = """SELECT id, olingan_sana, beriladigan_sana, talaba_id, kitob_id  FROM olingan_kitoblar WHERE id=?"""
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        return rows

    def olk_kirit(self, olingan_sana, beriladigan_sana, talaba_id, kitob_id):
        sql = """INSERT INTO olingan_kitoblar(olingan_sana, beriladigan_sana, talaba_id, kitob_id) VALUES(?,?,?,?)"""
        self.cursor.execute(sql, (olingan_sana, beriladigan_sana, talaba_id, kitob_id))
        self.con.commit()


    def olk_yangila(self, id, olingan_sana, beriladigan_sana, talaba_id, kitob_id):
        sql = """UPDATE olingan_kitoblar SET olingan_sana=?, beriladigan_sana=?, talaba_id=?, kitob_id=? WHERE id=?"""
        self.cursor.execute(sql, (id, olingan_sana, beriladigan_sana, talaba_id, kitob_id))
        self.con.commit()


    def olk_ochir(self, id):
        sql = """DELETE FROM olingan_kitoblar WHERE id=?"""
        self.cursor.execute(sql, (id,))
        self.con.commit()
        return rows


if __name__ == "__main__":
    db = DbManager()
    # rows = db.talabalar()
    # print(rows)
    # print(db.talaba(1))
    # # # kiritish
    # print('===================')
    # db.talaba_kirit("Shohjahon", 2)
    # rows = db.talabalar()
    # print(rows)
    #     yangilash
    # print('===================')
    # db.talaba_yangila(3, "Ulug'bek", 1)
    # rows = db.talabalar()
    # print(rows)
    #     o'chirish
    #     print('===================')
    #     db.talaba_ochir(3)
    #     rows = db.talabalar()
    #     print(rows)
    # rows = db.kurs()
    # print(rows)
    # print(db.kurslar(1))
    # db.kurs_kirit("Dasturlash")
    # rows = db.kurs()
    # print(rows)
    rows = db.kitoblar()
    print(rows)
    print(db.kitob(1))
    db.kitob_kirit("Sariq devni minib", "G'afur G'ulom", 2)
    rows = db.kitoblar()
    print(rows)
    # rows = db.olingan_kitoblar()
    # print(rows)
    # print(db.olingan_kitob(1))
    # db.olk_kirit(1, 21, 2, 1,8)
    # rows = db.olingan_kitoblar()
    # print(rows)
