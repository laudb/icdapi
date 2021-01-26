from app import db

class Record(db.Model):
    """This class handles diagnosis records"""

    __tablename__ = 'records'

    code = db.Column(db.Integer, primary_key=True)
    desc_short = db.Column(db.String(20))
    desc_long = db.Column(db.String(80))
    type = db.Colum(db.String(10))
    year = db.Column(db.Integer(6))

    def __init__(self, code, desc_short, desc_long, type, year):
        self.code = code
        self.desc_short = desc_short
        self.desc_long = desc_long
        self.type = type
        self.year = year

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Record-{self.year}-{self.code}-{self.type}>"

    def serialise(self):
        return {
            'code': self.code,
            'desc_short': self.desc_short,
            'type': self.type,
            'year': self.year
        }