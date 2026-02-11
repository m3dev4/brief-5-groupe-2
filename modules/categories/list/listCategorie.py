from utils.connectDb import connect_db


def list_categories():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM categories"

    try:
        cursor.execute(query)
        if cursor.rowcount == 0:
            print("Aucune catégorie trouvée.")
        categories = cursor.fetchall()
        for i, categorie in enumerate(categories, start=1):
            print(f"{i}. {categorie[1]}")

    except Exception as e:
        print(f"Erreur lors de la récupération des catégories: {e}")
