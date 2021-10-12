# import peewee
from models import *
from create_data import *
from datetime import datetime

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

def main():
    db.connect()
    db.create_tables(
        [User, Tag, Product, UserProduct, Transaction]
        )

    # create_data()

    # search('sweater')
    # search('koffie')
    # search('JBL')
    # list_user_products('Niels')
    # list_user_products('Renier')

    # list_products_per_tag('Books')
    # list_products_per_tag('Tech')

    # remove_product('Espresso machine')
    # list_user_products('Niels')

    # add_product_to_catalog('Niel', 'Blue sweater')
    # list_user_products('Niels')

    # update_stock('Headphones', 2)
    # purchase_product('Headphones', 'Kasper', 10)
    # purchase_product('Espresso machine', 'Niels', 1)


# Search for products based on a term. 
def search(term):
    search_term = term.lower()
    match = Product.select().where(
        (fn.lower(Product.name).contains(search_term)) |
        (fn.lower(Product.description).contains(search_term))
    )

    if match:
        print(f"De term {term} is gematched op:")
        for product in match:
            print(product.name)
    else:
        print('Product niet gevonden')

# View the products of a given user.
def list_user_products(user_id):
    product_list = UserProduct.select().where(
        UserProduct.owner == user_id
    )

    if product_list:
        print(f"{user_id} bezit:")
        for product in product_list:
            print(product.product)
    else:
        print('De eigenaar bestaat niet of bezit geen producten')


# View all products for a given tag.
def list_products_per_tag(tag_id):
    product_list = Product.select().where(Product.tags == tag_id)

    if product_list:
        print(f"Deze producten hebben de {tag_id} tag:")
        for product in product_list:
            print(product.name)
    else:
        print('De tag bestaat niet of heeft geen producten')

# Add a product to a user.
def add_product_to_catalog(user_id, product):
    # is working, but may need to adjust quantity if UserProduct exists already
    product_to_get = Product.select().where(Product.name == product)
    new_owner = User.select().where(User.name == user_id)

    if product_to_get and new_owner:
        added_product = UserProduct.create(
            owner=user_id,
            product=product,
            quantity=1,
            tags=Product.tags
        )
        print('New product toegevoegd.')
        return added_product
    else:
        print('Persoon of product niet gevonden')


# Remove a product from a user.
def remove_product(product_id):
    try:
        product = UserProduct.get(UserProduct.product == product_id)
        print(f"Het product {product_id} is verwijderd.")
        return product.delete_instance()
    except DoesNotExist:
        print('Kan het product niet vinden.')

# Update the stock quantity of a product.
def update_stock(product_id, new_quantity):
    product_to_change = Product.get(Product.name == product_id)

    if product_to_change:
        print(f'Oude aantal: {product_to_change.quantity}')
        product_to_change.quantity = new_quantity
        product_to_change.save()
        print(f'Nieuwe aantal: {product_to_change.quantity}')
    else:
        print('Kan product niet vinden')


# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    buyer = User.get(User.name == buyer_id)
    product_to_buy = Product.get(Product.name == product_id)
    
    if buyer and product_to_buy:
        current_date = datetime.now().date()
        get_date = datetime.strftime(current_date, '%d-%m-%Y')
        check_amount = product_to_buy.quantity - quantity
        # check if quantity exists

        if check_amount >= 0:
            # add a new transaction to the db
            Transaction.create(
                date=get_date,
                user=buyer_id,
                product=product_id,
                quantity=quantity
            )
        
            add_product_to_catalog(buyer_id, product_id)
            list_user_products(buyer_id)
            if check_amount == 0:
                # delete product
                return remove_product(product_id)

            # update
            return update_stock(product_id, check_amount)    
        else:
            print('Aantal niet op voorraad.')
    else:
        print('User of Product is niet gevonden.')    



if __name__ == '__main__':
    main()