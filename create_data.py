from models import *

# create some data for testing
def create_data():
    # USERS
    User.create(
        name="Kasper",
        address="Fatimaplein 44",
        location="Maastricht",
        postal_code="6214TT",
        billing="012345"
    )
    User.create(
        name="Niels",
        address="Fakestreet 12",
        location="Den Haag",
        postal_code="1015AA",
        billing="111111"
    )

    # TAGS
    Tag.create(tag="Tech")
    Tag.create(tag="Clothes")
    Tag.create(tag="Lifestyle")
    Tag.create(tag="Books")

    # PRODUCTS
    Product.create(
        name="Headphones",
        description="JBL headphones",
        price=40,
        quantity=3,
        tags="Tech"
    )
    Product.create(
        name="Blue sweater",
        description="Blue sweater",
        price=10,
        quantity=1,
        tags="Clothes"
    )
    Product.create(
        name="Hardloop schoenen",
        description="Schoenen om mee te hardlopen",
        price=30,
        quantity=5,
        tags="Clothes"
    )
    Product.create(
        name="Clean Code Boek",
        description="Schrijven van code die iedereen snapt",
        price=20,
        quantity=5,
        tags="Books"
    )

    # PRODUCT OWNED BY USER
    UserProduct.create(
        owner="Niels",
        product="Hardloop schoenen",
        quantity=1,
        tags="Clothes"
    )

    UserProduct.create(
        owner="Kasper",
        product="Clean Code Boek",
        quantity=1,
        tags="Books"
    )





