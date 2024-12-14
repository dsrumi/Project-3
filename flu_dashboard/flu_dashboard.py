import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd
import dash
app = Dash(__name__)
flu_data_by_state = pd.read_csv('flu_data_by_state.csv')

# App layout

app.layout = html.Div([
    html.H1("Flu Cases by Region"),
    
    # Dropdown for selecting year
    html.Label("Select Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": year, "value": year} for year in flu_data_by_state['YEAR'].unique()],
        value=flu_data_by_state['YEAR'].min()
    ),

    # Dropdown for selecting week
    html.Label("Select Week:"),
    dcc.Dropdown(
        id="week-dropdown",
        options=[{"label": week, "value": week} for week in flu_data_by_state['WEEK'].unique()],
        value=flu_data_by_state['WEEK'].min()
    ),

    # Choropleth map
    dcc.Graph(id="choropleth-map")
])

# Callbacks for interactivity
@app.callback(
    Output("choropleth-map", "figure"),
    [Input("year-dropdown", "value"), Input("week-dropdown", "value")]
)
def update_choropleth(selected_year, selected_week):
    # Filter data
    filtered_data = flu_data_by_state[(flu_data_by_state['YEAR'] == selected_year) & (flu_data_by_state['WEEK'] == selected_week)]
    agg_data = filtered_data.groupby('STATE_ABBR')['ILITOTAL'].sum().reset_index()

    # Create updated choropleth map
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
