import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import os
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



def zahl2land(b):
    c = "{0:02d}".format(b)
    a = str(c)
    zahl2landdic = {'00': 'Deutschland',
    '01': 'Schleswig-Holstein',
    '02': 'Freie und Hansestadt Hamburg',
    '03': 'Niedersachsen',
    '04': 'Freie Hansestadt Bremen',
    '05': 'Nordrhein-Westfalen',
    '06': 'Hessen',
    '07': 'Rheinland-Pfalz',
    '08': 'Baden-Württemberg',
    '09': 'Freistaat Bayern',
    '10': 'Saarland',
    '11': 'Berlin',
    '12': 'Brandenburg',
    '13': 'Mecklenburg-Vorpommern',
    '14': 'Freistaat Sachsen',
    '15': 'Sachsen-Anhalt',
    '16': 'Freistaat Thüringen'}
    land2zahldic = {v: k for k, v in zahl2landdic.items()}
    return zahl2landdic[a]


def give_cases(a,df):
    if a == 0:
        return df.groupby(['daten_stand']).sum().reset_index()
    if a < 17:
        df = df[df['bundesland'] == a].groupby(['daten_stand']).sum().reset_index()
        return df
    if a > 17:
        return df[df['gemeindeschluessel'] == a]


df = pd.read_csv('data/gesamt.csv',parse_dates=['daten_stand'])


available_indicators = np.insert(df['bundesland'].unique(),0,0)
print(available_indicators)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label': zahl2land(i)+': Intesivstationssituation', 'value': i} for i in available_indicators],
        value=0
    ),
    dcc.Graph(
        id='my-graph'
    )
])


@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
#def update_output(value):
#    return '{}'.format(zahl2land(value))
        #[zahl2land(n) for n in value])
def update_graph(value):
    dff =  give_cases(value,df)
    return {
        'data': [
            {'x': dff['daten_stand'],'y': dff['betten_frei'],'name': 'Betten frei'},
            {'x': dff['daten_stand'],'y': dff['betten_belegt'],'name': 'Betten belegt'},
            {'x': dff['daten_stand'],'y': dff['faelle_covid_aktuell'],'name': 'stationär wg. COVID'},
            {'x': dff['daten_stand'],'y': dff['faelle_covid_aktuell_beatmet'],'name': 'beatmet wg. COVID'}

        ],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}},
    }

server = app.server

if __name__ == '__main__':
    app.run_server()