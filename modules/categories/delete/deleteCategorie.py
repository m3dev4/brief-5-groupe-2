from utils.connectDb import connect_db


def delete_categorie():
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
            return
        
        print("\n📋 Catégories disponibles:")
        print("-" * 50)
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category[1]} (ID: {category[0]})")
        print("-" * 50)
        
        while True:
            try:
                choice = int(input("\nEntrez le numéro de la catégorie à supprimer: "))
                if 1 <= choice <= len(categories):
                    selected_category = categories[choice - 1]
                    category_id = selected_category[0]
                    category_name = selected_category[1]
                    break
                else:
                    print("Numéro invalide. Veuillez réessayer.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")
        
        message = f"\n⚠️  Êtes-vous sûr de vouloir supprimer la catégorie '{category_name}' ? (o/n): "
        confirmation = input(message)
        
        if (
            confirmation.lower() == "y"
            or confirmation.lower() == "yes"
            or confirmation.lower() == "o"
            or confirmation.lower() == "oui"
        ):
            delete_query = "DELETE FROM categories WHERE id = %s"
            cursor.execute(delete_query, (category_id,))
            db.commit()
            print(f"✅ Catégorie '{category_name}' supprimée avec succès!")
        else:
            print("❌ Suppression annulée.")
            
    except Exception as e:
        db.rollback()
        print(f"❌ Erreur lors de la suppression de la catégorie: {e}")
    finally:
        cursor.close()
        db.close()
