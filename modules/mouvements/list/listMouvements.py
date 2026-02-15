from utils.connectDb import connect_db


def list_mouvements():
    """
    Affiche l'historique de tous les mouvements de stock
    """
    db = connect_db()
    if not db:
        return
    
    cursor = db.cursor()
    
    # Requête pour récupérer tous les mouvements avec les informations du produit
    query = """
        SELECT m.id, m.date_mouvement, p.nom_produit, 
               m.quantite_ajoute, m.quantite_retirer, p.quantite as stock_actuel
        FROM mouvements m
        JOIN produits p ON m.id_produit = p.id
        ORDER BY m.date_mouvement DESC, m.id DESC
    """
    
    try:
        cursor.execute(query)
        mouvements = cursor.fetchall()
        
        if not mouvements:
            print("\n📋 Aucun mouvement enregistré dans l'historique.")
        else:
            print("\n" + "="*100)
            print("📋 HISTORIQUE DES MOUVEMENTS DE STOCK")
            print("="*100)
            
            for i, mouvement in enumerate(mouvements, start=1):
                id_mouv, date_mouv, nom_produit, qte_ajoute, qte_retirer, stock_actuel = mouvement
                
                if qte_ajoute:
                    type_mouvement = "ENTRÉE"
                    quantite = qte_ajoute
                    symbole = "➕"
                else:
                    type_mouvement = "SORTIE"
                    quantite = qte_retirer
                    symbole = "➖"
                
                print(f"\n{i}. {symbole} {type_mouvement}")
                print(f"   Date: {date_mouv}")
                print(f"   Produit: {nom_produit}")
                print(f"   Quantité: {quantite} unité(s)")
                print(f"   Stock actuel: {stock_actuel} unité(s)")
                print("-" * 100)
            
            print(f"\n📊 Total: {len(mouvements)} mouvement(s) enregistré(s)")
            print("="*100)
            
    except Exception as e:
        print(f"❌ Erreur lors de la récupération de l'historique: {e}")
    finally:
        cursor.close()
        db.close()

