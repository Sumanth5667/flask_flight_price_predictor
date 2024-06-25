from flask_wtf import FlaskForm
from wtforms import SelectField,DateField,TimeField,IntegerField,SubmitField
from wtforms.validators import DataRequired
import pandas as pd

train=pd.read_csv('data/train (4).csv')
validation=pd.read_csv('data/val.csv')
x_data=pd.concat([train,validation],axis=0).drop(columns=['price'])

class Inputform(FlaskForm):
    airline=SelectField(label='Airline',
                        choices=x_data.airline.unique().tolist(),
                        validators=[DataRequired()])
    
    date_of_journey=DateField(label='Date_Of_Journey',
                              validators=[DataRequired()])
    
    source=SelectField(label='Source',
                       choices=x_data.source.unique().tolist(),
                       validators=[DataRequired()])

    destination=SelectField(label='Destination',
                       choices=x_data.destination.unique().tolist(),
                       validators=[DataRequired()])
    
    dep_time=TimeField(label='Dep_Time',
                       validators=[DataRequired()],
                       )
    arrival_time=TimeField(label='Arrival_time',
                       validators=[DataRequired()],
                       )
    duration=IntegerField(label='Duration',
                          validators=[DataRequired()])
    
    total_stops=IntegerField(label='Total_Stops',
                          validators=[DataRequired()])
    additional_info=SelectField(label='Additional_Info',
                                validators=[DataRequired()],
                                choices=x_data.additional_info.unique().tolist())

    predict=SubmitField(
        label='Predict Price'
    )