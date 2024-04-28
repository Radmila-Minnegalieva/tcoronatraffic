"""returns a running server with an interactive map and takes data from the dataset"""
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc
from dash import Dash
import collections.abc

collections.MutableMapping = collections.abc.MutableMapping
collections.Mapping = collections.abc.Mapping
collections.MutableSequence = collections.abc.MutableSequence
collections.Sequence = collections.abc.Sequence
collections.Iterable = collections.abc.Iterable
collections.Iterator = collections.abc.Iterator
collections.MutableSet = collections.abc.MutableSet
collections.Callable = collections.abc.Callable

app = Dash(__name__)

dataframe = pd.read_csv("../../data/covid_19_data.csv")
dataframe = dataframe.rename(columns={'Country/Region': 'Страна'})
dataframe = dataframe.rename(columns={'ObservationDate': 'Дата'})
dataframe = dataframe.rename(columns={'Confirmed': 'Подтверждено'})
dataframe_countrydate = dataframe[dataframe['Подтверждено'] > 0]
dataframe_countrydate = dataframe_countrydate.groupby(
        ['Дата', 'Страна']).sum(numeric_only=False).reset_index()

maps = px.choropleth(data_frame=dataframe_countrydate,
                        locations="Страна",
                        locationmode="country names",
                        color="Подтверждено",
                        hover_name="Страна",
                        animation_frame="Дата"
                        )

maps.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ))

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(dcc.Graph(figure=maps)), align="center"),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)

