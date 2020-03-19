# Tuodaan tietokanta
from application import db

# Luodaan malli blogipostaukselle tietokantaan
class Post(db.Model):
    # Primary key (id)
    id = db.Column(db.Integer, primary_key=True)
    # Viittaus postauksen tehneeseen käyttäjään
    user_id = db.Column(db.Integer)
    # Päiväys jolloin postaus tehtiin
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Postauksen otsikko ja sisältö
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    # Postauksen äänimäärä väliaikaisesti tässä, toteutetaan myöhemmässä vaiheessa
    # liitostaulun avulla (many-to-many suhde käyttäjään)
    votes = db.Column(db.Integer, default=0)

    # Konstruktori, tallennetaan otsikko ja sisältö
    def __init__(self, title, content):
        self.title = title
        self.content = content
