# Tuodaan tietokanta
from application import db
from application.models import Base


# Luodaan malli blogipostaukselle tietokantaan
class Post(Base):

    # Postauksen otsikko ja sisältö
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(5000), nullable=False)

    # Viittaus postauksen tehneeseen käyttäjään
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    # Postauksen äänimäärä väliaikaisesti tässä, toteutetaan myöhemmässä vaiheessa
    # liitostaulun avulla (many-to-many suhde käyttäjään)
    votes = db.Column(db.Integer, default=0)

    # Konstruktori, tallennetaan otsikko ja sisältö
    def __init__(self, title, content):
        self.title = title
        self.content = content
