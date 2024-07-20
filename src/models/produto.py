from db import db
#MODEL DE PRODUTO
class Produto(db.Model):
    __tablename__ = 'produtos'
    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'stock': self.stock,
            'value': self.value,
            'id_category': self.id_category
        }
