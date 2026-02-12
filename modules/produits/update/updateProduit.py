from utils.connectDb import connect_db


def update_produit():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM produits"
    category_query = "SELECT * FROM categories WHERE id = %s"
    query_update = "UPDATE produits SET nom_produit = %s, prix = %s, quantite = %s, stock = %s, id_categorie = %s WHERE id = %s"
    cursor.execute(query)
    produits = cursor.fetchall()
    if not produits:
        print(
            "Aucun produit trouvé. Veuillez ajouter un produit avant de tenter de le mettre à jour."
        )
        return
    for i, produit in enumerate(produits, start=1):
        cursor.execute(category_query, (produit[5],))
        category = cursor.fetchone()
        print(
            f"{i}. {produit[1]} - Prix: {produit[2]}, Quantité: {produit[3]}, Stock: {produit[4]}, Catégorie {category[1] if category else 'Inconnue'}"
        )

    while True:
        try:
            choice = int(
                input("Entrez le numéro du produit que vous souhaitez mettre à jour: ")
            )
            if 1 <= choice <= len(produits):
                selected_product = produits[choice - 1]
                break
            else:
                print("Numéro invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

    while True:
        nom_produit = input(
            "Entrez le nouveau nom du produit (laissez vide pour ne pas changer): "
        )
        if nom_produit == "":
            nom_produit = selected_product[1]
            break
        else:
            nom_produit = nom_produit.strip().capitalize()
            break
    while True:
        try:
            price_input = input(
                "Entrez le nouveau prix du produit (laissez vide pour ne pas changer): "
            )
            if price_input == "":
                price = selected_product[2]
                break
            price = float(price_input)
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
            quantite_input = input(
                "Entrez la nouvelle quantité du produit (laissez vide pour ne pas changer): "
            )
            if quantite_input == "":
                quantite = selected_product[3]
                break
            quantite = int(quantite_input)
            if quantite < 0:
                print("La quantité ne peut pas être négative. Veuillez réessayer.")
                continue
            else:
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier pour la quantité.")
    while True:
        try:
            stock_input = input(
                "Entrez le nouveau stock du produit (laissez vide pour ne pas changer): "
            )
            if stock_input == "":
                stock = selected_product[4]
                break
            stock = int(stock_input)
            if stock < 0:
                print("Le stock ne peut pas être négatif. Veuillez réessayer.")
                continue
            else:
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier pour le stock.")

    while True:
        cursor.execute("SELECT * FROM categories")
        categorie = cursor.fetchall()
        for i, cat in enumerate(categorie, start=1):
            print(f"{i}. {cat[1]}")
        try:
            chooseCat_input = input(
                "Choisissez une nouvelle catégorie pour le produit (entrez le numéro, laissez vide pour ne pas changer): "
            )
            if chooseCat_input == "":
                category_id = selected_product[5]
                break
            chooseCat = int(chooseCat_input)
            if chooseCat < 1 or chooseCat > len(categorie):
                print("Numéro de catégorie invalide. Veuillez réessayer.")
                continue
            else:
                category_id = categorie[chooseCat - 1][0]
                break
        except ValueError:
            print(
                "Entrée invalide. Veuillez entrer un nombre entier pour la catégorie."
            )
    cursor.execute(
        query_update,
        (nom_produit, price, quantite, stock, category_id, selected_product[0]),
    )
    db.commit()
    print("Produit mis à jour avec succès.")
