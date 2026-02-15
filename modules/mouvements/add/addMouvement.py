from utils.connectDb import connect_db
from datetime import date


def add_mouvement():
    """
    Gère les mouvements de stock (entrée ou sortie) et met à jour automatiquement
    l'historique dans la table mouvements
    """
    db = connect_db()
    if not db:
        return

    cursor = db.cursor()

    # Afficher la liste des produits disponibles
    query_produits = "SELECT id, nom_produit, quantite FROM produits"
    cursor.execute(query_produits)
    produits = cursor.fetchall()

    if not produits:
        print(
            "Aucun produit trouvé. Veuillez ajouter un produit avant de faire un mouvement."
        )
        return

    print("\n############## Liste des produits ##############")
    for i, produit in enumerate(produits, start=1):
        print(f"{i}. {produit[1]} - Stock actuel: {produit[2]}")
    print("################################################\n")

    # Sélectionner un produit
    while True:
        try:
            choice = int(
                input(
                    "Entrez le numéro du produit pour lequel vous voulez faire un mouvement: "
                )
            )
            if 1 <= choice <= len(produits):
                selected_product = produits[choice - 1]
                product_id = selected_product[0]
                product_name = selected_product[1]
                current_stock = selected_product[2]
                break
            else:
                print("Numéro invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

    # Choisir le type de mouvement (Entrée ou Sortie)
    print(f"\nProduit sélectionné: {product_name} (Stock actuel: {current_stock})")
    print("\nType de mouvement:")
    print("1. Entrée (Ajouter du stock)")
    print("2. Sortie (Retirer du stock)")

    while True:
        try:
            mouvement_type = int(input("Choisissez le type de mouvement (1 ou 2): "))
            if mouvement_type == 1:
                type_mouvement = "Entrée"
                break
            elif mouvement_type == 2:
                type_mouvement = "Sortie"
                break
            else:
                print("Veuillez choisir 1 pour Entrée ou 2 pour Sortie.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer 1 ou 2.")

    # Demander la quantité
    while True:
        try:
            quantite = int(input(f"Entrez la quantité à {type_mouvement.lower()}: "))
            if quantite <= 0:
                print("La quantité doit être supérieure à 0. Veuillez réessayer.")
                continue

            # Vérifier si on peut retirer la quantité demandée
            if type_mouvement == "Sortie" and quantite > current_stock:
                print(
                    f"Erreur: Vous ne pouvez pas retirer {quantite} unités. Stock disponible: {current_stock}"
                )
                continue

            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

    try:
        # Calculer le nouveau stock
        if type_mouvement == "Entrée":
            nouveau_stock = current_stock + quantite
            quantite_ajoute = quantite
            quantite_retirer = None
        else:  # Sortie
            nouveau_stock = current_stock - quantite
            quantite_ajoute = None
            quantite_retirer = quantite

        # Mettre à jour le stock du produit
        update_query = "UPDATE produits SET quantite = %s WHERE id = %s"
        cursor.execute(update_query, (nouveau_stock, product_id))

        # Enregistrer le mouvement dans l'historique
        mouvement_query = """
            INSERT INTO mouvements (quantite_ajoute, quantite_retirer, date_mouvement, id_produit)
            VALUES (%s, %s, %s, %s)
        """
        today = date.today()
        cursor.execute(
            mouvement_query, (quantite_ajoute, quantite_retirer, today, product_id)
        )

        db.commit()

        print(f"\n✅ Mouvement enregistré avec succès!")
        print(f"   Produit: {product_name}")
        print(f"   Type: {type_mouvement}")
        print(f"   Quantité: {quantite}")
        print(f"   Stock avant: {current_stock}")
        print(f"   Stock après: {nouveau_stock}")
        print(f"   Date: {today}")

    except Exception as e:
        db.rollback()
        print(f"❌ Erreur lors de l'enregistrement du mouvement: {e}")
    finally:
        cursor.close()
        db.close()
