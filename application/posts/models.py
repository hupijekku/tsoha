from application import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    # Temporary
    votes = db.Column(db.Integer, default=0)

    def __init__(self, title, content):
        self.title = title
        self.content = content
