import sqlite3

def main():
    conn = sqlite3.connect("El_Fieston.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS favoritos
    (id Integer,
    nombre Text,
    tags Text,
    categoria Text,
    alcohol Text,
    vaso Text,
    instrucciones Text,
    imagen Text,
    ingredientes Text,
    medidas Text,
    bienElectrico Integer)  
    ''')
    conn.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS bebidas
        (id Integer,
        nombre Text,
        tags Text,
        categoria Text,
        alcohol Text,
        vaso Text,
        instrucciones Text,
        imagen Text,
        ingredientes Text,
        medidas Text,
        bienElectrico Integer)    
        ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()