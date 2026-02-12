from utils.connectDb import connect_db


def listProduct():
    print("##############Liste des produits##############")
    db = connect_db()
    cursor = db.cursor()
    query = """SELECT * from produits"""
    category_query = "SELECT * FROM categories WHERE id = %s"
    cursor.execute(query)
    produits = cursor.fetchall()
    for i, produit in enumerate(produits, start=1):
        cursor.execute(category_query, (produit[5],))
        category = cursor.fetchone()
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print(
            f"{i}. {produit[1]} - Prix: {produit[2]} - Quantité: {produit[3]} - Stock: {produit[4]} - Catégorie: {category[1] if category else 'Inconnue'}"
        )
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------------"
        )
