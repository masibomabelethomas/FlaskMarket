
from app.extentions import db


class item(db.model):
    name = db.Column(db.String(length = 30), nullable=False,unique=True)
    price=db.Column(db.intenger(),nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description =db.Column(db.String(length=1045),nullable=False,unique=True)
    id=db.Column(db.intenger(length=23),nullable=False,unique=True)
