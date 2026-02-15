# Categories Module
from modules.categories.add.addCategorie import add_categorie
from modules.categories.list.listCategorie import list_categories
from modules.categories.delete.deleteCategorie import delete_categorie

# Products Module
from modules.produits.add.addProduct import addProduct
from modules.produits.list.listProduct import listProduct
from modules.produits.update.updateProduit import update_produit

# Mouvements Module
from modules.mouvements.add.addMouvement import add_mouvement
from modules.mouvements.list.listMouvements import list_mouvements

# Alertes Module
from modules.alertes.alerteStock import alerte_stock


def main_menu():
    """
    Menu principal du système de gestion de stock
    """
    while True:
        print("\n" + "="*80)
        print("🏢 SYSTÈME DE GESTION DE STOCK - MENU PRINCIPAL")
        print("="*80)
        print("\n📦 GESTION DES CATÉGORIES:")
        print("   1. Ajouter une catégorie")
        print("   2. Lister les catégories")
        print("   3. Supprimer une catégorie")
        
        print("\n📋 GESTION DES PRODUITS:")
        print("   4. Ajouter un produit")
        print("   5. Lister tous les produits")
        print("   6. Modifier un produit")
        
        print("\n🔄 GESTION DES MOUVEMENTS:")
        print("   7. Ajouter/Retirer du stock (Mouvement)")
        print("   8. Consulter l'historique des mouvements")
        
        print("\n⚠️  ALERTES:")
        print("   9. Afficher les alertes de stock faible (< 5 unités)")
        
        print("\n   0. Quitter")
        print("="*80)
        
        try:
            choice = input("\nVeuillez choisir une option (0-9): ").strip()
            
            if choice == "0":
                print("\n👋 Au revoir ! Merci d'avoir utilisé le système de gestion de stock.")
                break
            elif choice == "1":
                print("\n" + "-"*80)
                add_categorie()
            elif choice == "2":
                print("\n" + "-"*80)
                list_categories()
            elif choice == "3":
                print("\n" + "-"*80)
                delete_categorie()
            elif choice == "4":
                print("\n" + "-"*80)
                addProduct()
            elif choice == "5":
                print("\n" + "-"*80)
                listProduct()
            elif choice == "6":
                print("\n" + "-"*80)
                update_produit()
            elif choice == "7":
                print("\n" + "-"*80)
                add_mouvement()
            elif choice == "8":
                print("\n" + "-"*80)
                list_mouvements()
            elif choice == "9":
                print("\n" + "-"*80)
                alerte_stock()
            else:
                print("\n❌ Option invalide. Veuillez choisir un nombre entre 0 et 9.")
            
            # Pause pour permettre à l'utilisateur de voir le résultat
            if choice != "0":
                input("\n⏎ Appuyez sur Entrée pour continuer...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir !")
            break
        except Exception as e:
            print(f"\n❌ Une erreur est survenue: {e}")
            input("\n⏎ Appuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main_menu()