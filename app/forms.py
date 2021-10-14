from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    database = SelectField('Database:', choices=[('instacart_normalized', 'instacart_normalized'), ('instacart', 'instacart')])
    server = RadioField('Server:', choices=[('mysql', 'MySQL'), ('redshift', 'Redshift')])
    query = StringField('Query:', widget=TextArea(), validators=[DataRequired()])