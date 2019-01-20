from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    itemId = db.Column(db.String(30), unique=True)
    title = db.Column(db.String(300))
    price = db.Column(db.String(50))
    shop = db.Column(db.String(300))

    __tablename__ = "jd"

    def to_dict(self):
        return {
            'id': self.id,
            'itemId': self.itemId,
            'title': self.title,
            'price': self.price,
            'shop': self.shop
        }