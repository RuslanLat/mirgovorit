from app.store.database import db


class RecipeModel(db.Model):
    __tablename__ = "recipes"
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return self.title
