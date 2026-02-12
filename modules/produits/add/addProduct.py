from utils.connectDb import connect_db


def addProduct():
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO produits (nom_produit, prix, quantite, stock, id_categorie) VALUES (%s, %s, %s, %s, %s)"
    category_query = "SELECT * FROM categories"

    if cursor.execute(category_query) == 0:
        print(
            "Pas de catégories trouvées. Veuillez ajouter une catégorie avant d'ajouter un produit."
        )
        return

    while True:
        nom_produit = input("Entrez le nom du produit: ")
        if nom_produit == "":
            print("Le nom du produit ne peut pas être vide. Veuillez réessayer.")
            continue
        else:
            nom_produit = nom_produit.strip().capitalize()
            break
    while True:
        try:
            price = float(input("Entrez le prix du produit: "))
            if price < 0:
                print("Le prix ne peut pas être négatif. Veuillez réessayer.")
                continue
            elif price == 0:
                print("Le prix ne peut pas être zéro. Veuillez réessayer.")
                continue
            else:
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre pour le prix.")
    while True:
        try:
            quantite = int(input("Entrez la quantité du produit: "))
            if quantite < 0:
                print("La quantité ne peut pas être négative. Veuillez réessayer.")
                continue
            else:
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier pour la quantité.")
    while True:
        try:
            stock = int(input("Entrez le stock du produit: "))
            if stock < 0:
                print("Le stock ne peut pas être négatif. Veuillez réessayer.")
                continue
            else:
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier pour le stock.")
    while True:
        categorie = cursor.fetchall()
        for i, cat in enumerate(categorie, start=1):
            print(f"{i}. {cat[1]}")
        try:
            chooseCat = int(
                input("Choisissez une catégorie pour le produit (entrez le numéro): ")
            )
            if chooseCat < 1 or chooseCat > len(categorie):
                print("Numéro de catégorie invalide. Veuillez réessayer.")
                continue
            else:
                category_id = categorie[chooseCat - 1][0]
                break
        except ValueError:
            print(
                "Entrée invalide. Veuillez entrer un nombre entier pour choisir la catégorie."
            )
    cursor.execute(query, (nom_produit, price, quantite, stock, category_id))
    db.commit()
    print("Produit ajouté avec succès!")
