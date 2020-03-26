from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PostForm(FlaskForm):
    name = StringField("Post title", [validators.Length(min=3)])
    content = StringField("Post content")
    class Meta:
        csrf = False

