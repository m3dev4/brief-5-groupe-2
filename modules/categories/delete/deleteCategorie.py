from utils.connectDb import connect_db


def delete_categorie():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM categories"
    if cursor.execute(query) == 0:
        print("No categories found.")
        return
    categories = cursor.fetchall()
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category[1]} (ID: {category[0]})")
        id = input(f"Enter the ID of the category to delete  ")
        message = "Vous êtes sûr de vouloir supprimer cette catégorie ? (y/n) "
        confirmation = input(message)
        if (
            confirmation.lower() == "y"
            or confirmation.lower() == "yes"
            or confirmation.lower() == "o"
            or confirmation.lower() == "oui"
        ):
            delete_query = "DELETE FROM categories WHERE id = %s"
            cursor.execute(delete_query, (id,))
            db.commit()
            print("Category deleted successfully.")
