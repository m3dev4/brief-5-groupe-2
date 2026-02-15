from utils.connectDb import connect_db


def list_categories():
    db = connect_db()
    if not db:
        return
    
    cursor = db.cursor()
    query = "SELECT * FROM categories"

    try:
        cursor.execute(query)
        categories = cursor.fetchall()
        if not categories:
            print("Aucune catégorie trouvée.")
        else:
            print("\n📋 Liste des catégories:")
            print("-" * 50)
            for i, categorie in enumerate(categories, start=1):
                print(f"{i}. {categorie[1]}")
            print("-" * 50)

    except Exception as e:
        print(f"❌ Erreur lors de la récupération des catégories: {e}")
    finally:
        cursor.close()
        db.close()
