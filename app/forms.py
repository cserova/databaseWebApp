from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    #databases hardcoded, figure connection can happen after user selects both server and db
    database = SelectField('Database:', choices=[('ic', 'instacart'), ('icn', 'instacart_normalized')]) 
    server = RadioField('Server:', choices=[('mysql', 'MySQL'), ('rs', 'Redshift')])
    query = StringField('Query:', validators=[DataRequired()])
    run = SubmitField('Run')