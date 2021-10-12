from peewee import *

db = SqliteDatabase("betsy.db")

class DBmodel(Model):
    class Meta:
        database = db


# A user has a name, address data, and billing information.
class User(DBmodel):
    name = CharField()
    address = CharField()
    location = CharField()
    postal_code = CharField()
    billing = IntegerField()
    # Billing should include more information

    # Each user must be able to own a number of products.
    # products = ManyToManyField()
    # Not sure yet?


# In order to facilitate search and categorization, a product must have a number of descriptive tags.
class Tag(DBmodel):
    tag = CharField()
    # Unique?
    # The tags should not be duplicated.

# The products must have a name, a description, a price per unit, and a quantity describing the amount in stock.
class Product(DBmodel):
    name = CharField()
    description = CharField()
    # The price should be stored in a safe way; rounding errors should be impossible.
    price = FloatField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref='p_tag')

    # product owner?
    # productOwner = CharField()

class UserProduct(DBmodel):
    owner = CharField()
    product = CharField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref='up_tag')


# We want to be able to track the purchases made on the marketplace, therefore a transaction model must exist
# You can assume that only users can purchase goods
class Transaction(DBmodel):
    date = CharField()
    # The transaction model must link a buyer with a purchased product and a quantity of purchased items
    user = CharField()
    product = CharField()
    quantity = IntegerField()



"""As a bonus requirement, you must consider the various constraints for all fields and incorporate these constraints in the data model."""