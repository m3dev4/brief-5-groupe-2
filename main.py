#Categories Module
from modules.categories.add.addCategorie import add_categorie
from modules.categories.list.listCategorie import list_categories
from modules.categories.delete.deleteCategorie import delete_categorie
from modules.produits.add.addProduct import addProduct
from modules.produits.list.listProduct import listProduct
from modules.produits.update.updateProduit import update_produit
#Products Module
from modules.produits.add.addProduct import addProduct

def main_menu():
    print("Bienvenue dans le menu principal (: ")
    update_produit()
    
    
    
    
if __name__ == "__main__":
    main_menu()