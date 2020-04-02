from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class PostForm(FlaskForm):
    name = StringField("Post title", [validators.Length(min=3)])
    content = TextAreaField("Post content")
    class Meta:
        csrf = False

