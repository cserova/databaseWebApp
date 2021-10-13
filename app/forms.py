from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    #databases hardcoded, figure connection can happen after user selects both server and db
    server = RadioField('Server:', choices=[('mysql', 'MySQL'), ('redshift', 'Redshift')])
    query = StringField('Query:', widget=TextArea(), validators=[DataRequired()])