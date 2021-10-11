# import peewee
from models import *
from create_data import *

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

template = "{product.name} {product.description} {product.price} {product.quantity}"

def main():
    db.connect()
    db.create_tables([User, Product, Tag, ProductTag, Transaction])

    # create_data()

    search('sweater')


# Search for products based on a term. 
# Searching for 'sweater' should yield all products 
# that have the word 'sweater' in the name. 
# This search should be case-insensitive
def search(term):
    search_term = term.lower()
    match = Product.select().where(
        (fn.lower(Product.name).contains(search_term)) 
        or 
        (fn.lower(Product.description).contains(search_term))
    )

    if match:
        for product in match:
            print(product.name)
    else:
        print('Product not found')

# View the products of a given user.
def list_user_products(user_id):
    pass


# View all products for a given tag.
def list_products_per_tag(tag_id):
    pass


# Add a product to a user.
def add_product_to_catalog(user_id, product):
    pass


# Remove a product from a user.
def remove_product(product_id):
    pass


# Update the stock quantity of a product.
def update_stock(product_id, new_quantity):
    pass


# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    pass

if __name__ == '__main__':
    main()