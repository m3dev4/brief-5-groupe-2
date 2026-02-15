from utils.connectDb import connect_db


def add_categorie():
    db = connect_db()
    cursor = db.cursor()

    query = "INSERT INTO categories (nom_categorie) VALUES (%s)"
    while True:
        nom_categorie = input("Entrez le nom de la catégorie : ")
        if nom_categorie.strip() == "" or nom_categorie.isnumeric():
            print(
                "Le nom de la catégorie ne peut pas être vide ou numérique. Veuillez réessayer."
            )
            continue
        else:
            nom_categorie = nom_categorie.capitalize()
            break
    try:
        cursor.execute(query, (nom_categorie,))
        db.commit()
        print("✅ Catégorie ajoutée avec succès!")
    except Exception as e:
        db.rollback()
        print(f"❌ Erreur lors de l'ajout de la catégorie: {e}")
    finally:
        cursor.close()
        db.close()
