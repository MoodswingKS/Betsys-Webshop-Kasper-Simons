import peewee
from models import *

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

def main():
    pass


# Search for products based on a term. 
# Searching for 'sweater' should yield all products that have the word 'sweater' in the name. 
# This search should be case-insensitive
def search(term):
    pass


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