import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Data for the first set of figures
data = pd.read_csv('data.csv')
activity_map = {
    'Level 1': 1,
    'Level 2': 2,
    'Level 3': 3,
    'Level 4': 4,
    'Level 5': 5,
    'Level 6': 6,
    'Level 7': 7,
    'Level 8': 8,
}
data['ACTIVITY LEVEL NUMERIC'] = data['ACTIVITY_LEVEL'].map(activity_map)
fig1 = px.choropleth(
    data_frame=data,
    locations="STATE_ABBR",
    locationmode="USA-states",
    color="ACTIVITY LEVEL NUMERIC",
    hover_name="STATENAME",
    hover_data=["ACTIVITY LEVEL NUMERIC", "WEEK"],
    animation_frame="WEEK",
    color_continuous_scale="Viridis",
    scope="usa",
    title="Influenza Activity Levels by State Over Time"
)

agg_data = pd.read_csv('agg_data.csv')
fig2 = px.bar(
    agg_data,
    x='REGION',
    y='Count',
    color='Virus Type',
    title='Flu Counts by Region and Virus Type for 2024-2025 Season',
    labels={'Count': 'Number of Cases', 'REGION': 'Region'}
)

# Data for the interactive dashboard
flu_data_by_state = pd.read_csv('flu_data_by_state.csv')

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Flu Data Dashboard", style={'text-align': 'center'}),

    # First set of figures
    html.Div([
        html.H2("Influenza Activity Levels Over Time"),
        dcc.Graph(id='choropleth-map-static', figure=fig1)
    ], style={'margin-bottom': '50px'}),

    html.Div([
        html.H2("Flu Counts by Region and Virus Type"),
        dcc.Graph(id='bar-chart', figure=fig2)
    ], style={'margin-bottom': '50px'}),

    # Interactive Dashboard Section
    html.Div([
        html.H2("Interactive Flu Cases by Region"),
        html.Label("Select Year:"),
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": year, "value": year} for year in flu_data_by_state['YEAR'].unique()],
            value=flu_data_by_state['YEAR'].min(),
            style={'margin-bottom': '10px'}
        ),
        html.Label("Select Week:"),
        dcc.Dropdown(
            id="week-dropdown",
            options=[{"label": week, "value": week} for week in flu_data_by_state['WEEK'].unique()],
            value=flu_data_by_state['WEEK'].min(),
            style={'margin-bottom': '20px'}
        ),
        dcc.Graph(id="choropleth-map-interactive")
    ])
])

# Callback for the interactive choropleth map
@app.callback(
    Output("choropleth-map-interactive", "figure"),
    [Input("year-dropdown", "value"), Input("week-dropdown", "value")]
)
def update_choropleth(selected_year, selected_week):
    filtered_data = flu_data_by_state[
        (flu_data_by_state['YEAR'] == selected_year) &
        (flu_data_by_state['WEEK'] == selected_week)
    ]
    agg_data = filtered_data.groupby('STATE_ABBR')['ILITOTAL'].sum().reset_index()

    fig = px.choropleth(
        agg_data,
        locations="STATE_ABBR",
        locationmode="USA-states",
        color="ILITOTAL",
        color_continuous_scale="Reds",
        scope="usa",
        title=f"Flu Cases by Region (Year: {selected_year}, Week: {selected_week})"
    )
    return fig

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
