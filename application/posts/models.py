# Tuodaan tietokanta
from application import db
from application.models import Base

from sqlalchemy.sql import text

# Luodaan malli blogipostaukselle tietokantaan
class Post(Base):

    # Postauksen otsikko ja sisältö
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(5000), nullable=False)

    # Viittaus postauksen tehneeseen käyttäjään
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    # Konstruktori, tallennetaan otsikko ja sisältö
    def __init__(self, title, content):
        self.title = title
        self.content = content


class Vote(Base):

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

    @staticmethod
    def get_post_vote_count(id):
        stmt = text("SELECT COUNT(*) FROM vote WHERE post_id = :id").params(id=id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        return response[0]


class Tag(Base):

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name


class PostTag(Base):
    
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, tag_id, post_id):
        self.tag_id = tag_id
        self.post_id = post_id

    @staticmethod
    def get_post_tags(id):
        stmt = text("SELECT name FROM post_tag LEFT JOIN tag ON post_tag.tag_id = tag.id WHERE post_id = :id").params(id=id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        return response
