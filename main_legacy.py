from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Simulation d'une base de données déjà existante
DATABASE = "ecommerce.db"

@app.get("/products/{user_id}")
async def product_infos(id: int):
    # Requête SQL brute au milieu de la route
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        # Requête SQL brute au milieu de la route
        cursor.execute("SELECT stock, price FROM products WHERE id = ?", (id,))
        product = cursor.fetchone()

        if not product:
            raise HTTPException(status_code=404, detail="Produit introuvable")

        stock, price = product

        if stock == 0:
            raise HTTPException(status_code=400, detail="Stock insuffisant")
       
        return {"status": "success", "total": price}

    except sqlite3.Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))