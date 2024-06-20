# Import libraries
import numpy as np
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the wildfire data into pandas dataframe
df =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')

#Extract year and month from the date column
df['Month'] = pd.to_datetime(df['Date']).dt.month_name() #used for the names of the months
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Create a dash applicaion
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Australia Wildlife Dashboard",style={'textAlign':'center','color':'#503D36','font-size':40}),
    html.Div(children=[
        html.H1("Select Region",style={'font-size':30,'textAlign':'left'}),
        # dcc.RadioItems(['NSW','QL','SA','TA','VI','WA'],value='NSW',id='input-region',inline=True)
        dcc.RadioItems([{"label":"New South Wales","value": "NSW"},
                                    {"label":"Northern Territory","value": "NT"},
                                    {"label":"Queensland","value": "QL"},
                                    {"label":"South Australia","value": "SA"},
                                    {"label":"Tasmania","value": "TA"},
                                    {"label":"Victoria","value": "VI"},
                                    {"label":"Western Australia","value": "WA"}],value="NSW", id='input-region',inline=True)
    ]),
    html.Div(children=[
        html.H1("Select Year: ",style={'textAlign':'left','font-size':30}),
        dcc.Dropdown(df.Year.unique(),value=2005,id='input-year')
    ]),
    html.Div(children=[
        html.Div(dcc.Graph(id='plot1')),
        html.Div(dcc.Graph(id='plot2'))
    ],style={'display':'flex'})
])

def compute_info(data_frame,input_region,input_year):
    # select data
    data = data_frame[(data_frame['Region']==input_region) & (data_frame['Year']==int(input_year))]
    # plot1 data
    pie_data = data.groupby('Month')['Estimated_fire_area'].mean().reset_index()

    # plot2 data
    bar_data = data.groupby('Month')['Count'].mean().reset_index()

    return pie_data,bar_data


# Callback operator
@app.callback([
    Output(component_id='plot1',component_property='figure'),
    Output(component_id='plot2',component_property='figure')
    ],
    Input(component_id='input-region',component_property='value'),
    Input(component_id='input-year',component_property='value')
    )

# Add computation to callback function and return graph
def get_graph(input_region,input_year):
    pie_data,bar_data = compute_info(df,input_region,input_year)
    pie_fig = px.pie(data_frame=pie_data,values='Estimated_fire_area',names='Month',title="{} : Monthly Average Estimated Fire Area in year {}".format(input_region,input_year))

    bar_fig = px.bar(data_frame=bar_data,x='Month',y='Count',title='{} : Average Count of Pixels for Presumed Vegetation Fires in year {}'.format(input_region,input_year))
    
    return [pie_fig,bar_fig]


# Run the application
if __name__ == '__main__':
    app.run_server()