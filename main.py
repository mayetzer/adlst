import sqlite3

# Auth: Zerare Tamay

# Database ismi
DB_FILE = "adlst.db"


def db_baglanti():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""CREATE TABLE IF NOT EXISTS kisi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT NOT NULL,
        telefon TEXT,
        email TEXT,
        adres TEXT
    )""")
    return conn

def kisi_ekle(conn):
    isim = input("İsim: ")
    tel = input("Telefon: ")
    email = input("E-posta: ")
    adres = input("Adres: ")
    conn.execute("INSERT INTO kisi (isim, telefon, email, adres) VALUES (?, ?, ?, ?)",
                 (isim, tel, email, adres))
    conn.commit()

def kisileri_listele(conn):
    for row in conn.execute("SELECT * FROM kisi"):
        print(row)

def kisi_ara(conn):
    kelime = input("Arama: ")
    for row in conn.execute("SELECT * FROM kisi WHERE isim LIKE ? OR telefon LIKE ? OR email LIKE ? OR adres LIKE ?",
                            (f"%{kelime}%",)*4):
        print(row)

def kisi_sil(conn):
    id_ = input("Silinecek ID: ")
    conn.execute("DELETE FROM kisi WHERE id=?", (id_,))
    conn.commit()

def kisi_guncelle(conn):
    id_ = input("Güncellenecek ID: ")
    isim = input("Yeni Isim: ")
    tel = input("Yeni Telefon: ")
    email = input("Yeni E-posta: ")
    adres = input("Yeni Adres: ")
    conn.execute("""UPDATE kisi SET isim=?, telefon=?, email=?, adres=? WHERE id=?""",
                 (isim, tel, email, adres, id_))
    conn.commit()

def menu():
    conn = db_baglanti()
    while True:
        print("\n1) Ekle\n2) Listele\n3) Ara\n4) Sil\n5) Güncelle\n6) Çıkış")
        secim = input("Seçim: ")
        if secim == "1": kisi_ekle(conn)
        elif secim == "2": kisileri_listele(conn)
        elif secim == "3": kisi_ara(conn)
        elif secim == "4": kisi_sil(conn)
        elif secim == "5": kisi_guncelle(conn)
        elif secim == "6": break
        else: print("Hatalı seçim.")

if __name__ == "__main__":
    menu()
