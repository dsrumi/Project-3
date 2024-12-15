import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
# Figure 1: Choropleth Map
data=pd.read_csv('data.csv')
fig1 = px.choropleth(
    data_frame=data,
    locations="STATE_ABBR",
    locationmode="USA-states",
    color="ACTIVITY_LEVEL",
    hover_name="STATENAME",
    hover_data=["ACTIVITY_LEVEL", "WEEK"],
    animation_frame="WEEK",
    color_continuous_scale="Viridis",
    scope="usa",
    title="Influenza Activity Levels by State Over Time"
)

# Figure 2: Bar Chart
agg_data=pd.read_csv('agg_data.csv')


fig2 = px.bar(
    agg_data, 
    x='REGION', 
    y='Count', 
    color='Virus Type', 
    title='Flu Counts by Region and Virus Type for 2024-2025 Season',
    labels={'Count': 'Number of Cases', 'REGION': 'Region'}
)
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Flu Data Dashboard", style={'text-align': 'center'}),

    # First figure (Choropleth Map)
    html.Div([
        dcc.Graph(
            id='choropleth-map',
            figure=fig1
        )
    ], style={'margin-bottom': '50px'}),

    # Second figure (Bar Chart)
    html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=fig2
        )
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)
