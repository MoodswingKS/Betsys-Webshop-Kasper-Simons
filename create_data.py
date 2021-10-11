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

    # PRODUCTS

    Product.create(
        name="Headphones",
        description="JBL headphones",
        price=40,
        quantity=3
    )

    Product.create(
        name="Blue sweater",
        description="Blue sweater",
        price=10,
        quantity=1
    )

    # TAGS

    Tag.create(
        tag="Tech"
    )

    Tag.create(
        tag="Clothes"
    )

    Tag.create(
        tag="Lifestyle"
    )


