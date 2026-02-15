from utils.connectDb import connect_db


def alerte_stock():
    """
    Affiche tous les produits dont le stock est inférieur à 5 unités
    """
    db = connect_db()
    if not db:
        return
    
    cursor = db.cursor()
    
    # Requête pour récupérer les produits avec stock < 5, avec le nom de la catégorie
    query = """
        SELECT p.id, p.nom_produit, p.quantite, p.prix, c.nom_categorie
        FROM produits p
        LEFT JOIN categories c ON p.id_categorie = c.id
        WHERE p.quantite < 5
        ORDER BY p.quantite ASC
    """
    
    try:
        cursor.execute(query)
        produits_alerte = cursor.fetchall()
        
        if not produits_alerte:
            print("\n✅ Aucune alerte: Tous les produits ont un stock suffisant (≥ 5 unités)")
        else:
            print("\n" + "="*80)
            print("⚠️  ALERTE STOCK FAIBLE - Produits avec stock < 5 unités")
            print("="*80)
            
            for i, produit in enumerate(produits_alerte, start=1):
                id_prod, nom, quantite, prix, categorie = produit
                print(f"\n{i}. {nom}")
                print(f"   ID: {id_prod}")
                print(f"   Stock actuel: {quantite} unité(s) ⚠️")
                print(f"   Prix: {prix}")
                print(f"   Catégorie: {categorie if categorie else 'Non catégorisé'}")
                print("-" * 80)
            
            print(f"\n📊 Total: {len(produits_alerte)} produit(s) nécessitant une réapprovisionnement")
            print("="*80)
            
    except Exception as e:
        print(f"❌ Erreur lors de la récupération des alertes: {e}")
    finally:
        cursor.close()
        db.close()

