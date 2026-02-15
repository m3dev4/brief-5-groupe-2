from utils.connectDb import connect_db


def listProduct():
    db = connect_db()
    if not db:
        return
    
    cursor = db.cursor()
    # Utiliser une jointure pour récupérer directement le nom de la catégorie
    query = """
        SELECT p.id, p.nom_produit, p.prix, p.stock, p.quantite, c.nom_categorie
        FROM produits p
        LEFT JOIN categories c ON p.id_categorie = c.id
        ORDER BY p.id
    """
    
    try:
        cursor.execute(query)
        produits = cursor.fetchall()
        
        if not produits:
            print("\n📦 Aucun produit trouvé.")
        else:
            print("\n" + "="*100)
            print("📦 LISTE DES PRODUITS")
            print("="*100)
            for i, produit in enumerate(produits, start=1):
                id_prod, nom, prix, stock, quantite, categorie = produit
                print(f"\n{i}. {nom}")
                print(f"   ID: {id_prod}")
                print(f"   Prix: {prix}")
                print(f"   Quantité: {quantite} unité(s)")
                print(f"   Stock: {stock}")
                print(f"   Catégorie: {categorie if categorie else 'Non catégorisé'}")
                print("-" * 100)
            print(f"\n📊 Total: {len(produits)} produit(s)")
            print("="*100)
    except Exception as e:
        print(f"❌ Erreur lors de la récupération des produits: {e}")
    finally:
        cursor.close()
        db.close()
