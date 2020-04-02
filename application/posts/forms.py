from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class PostForm(FlaskForm):
    name = StringField("Post title", [validators.Length(min=3, max=144)])
    content = TextAreaField("Post content", [validators.Length(min=3, max=5000)])
    class Meta:
        csrf = False

