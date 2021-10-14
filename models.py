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


# In order to facilitate search and categorization, a product must have a number of descriptive tags.
class Tag(DBmodel):
    tag = CharField(unique=True)


# The products must have a name, a description, a price per unit, and a quantity describing the amount in stock.
class Product(DBmodel):
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref='p_tag')

class UserProduct(DBmodel):
    owner = CharField()
    product = CharField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref='up_tag')


# We want to be able to track the purchases made on the marketplace, therefore a transaction model must exist
class Transaction(DBmodel):
    # date could be DateField, but instead I've used datetime module to create a string of the date.
    date = CharField()
    user = CharField()
    product = CharField()
    quantity = IntegerField()