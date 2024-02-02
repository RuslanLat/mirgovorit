from app.store.database import db


class ProductModel(db.Model):
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.title
