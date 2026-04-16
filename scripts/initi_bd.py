import sqlite3

def init_db():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            stock INTEGER,
            price REAL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product TEXT,
            total REAL
        )
    ''')
    
    products = [
        ('Clavier Mécanique', 10, 120.0),
        ('Souris Gamer', 25, 60.0),
        ('Écran 27 pouces', 5, 350.0)
    ]
    
    try:
        cursor.executemany('INSERT INTO products (name, stock, price) VALUES (?, ?, ?)', products)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Les données existent déjà.")
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()