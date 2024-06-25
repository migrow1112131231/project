from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df
import numpy as np

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
            html.Div([
                html.H1("Тепловая карта показателей"),
                html.P("Сравнение ВВП стран мира и общего использования интернета"),
                html.Hr(style={'color': 'black'}),
            ])
        )
    ]),

    dbc.Row ([
        dbc.Col([
            dbc.RadioItems(
                value='GDP',
                id='crossfilter-ind',
            ),
            dbc.Label("Выберите страну:"),
            dcc.Dropdown(
                id='crossfilter-country',
                options=[{'label': 'Все', 'value': 'Все'}] + [{'label': i, 'value': i} for i in df['Country'].unique()],
                value='Все'
            ),
            dcc.Graph(id = 'choropleth', config={'displayModeBar': False}),
        ], width=9)
    ])
])


@callback(
    Output('choropleth', 'figure'),
    Input('crossfilter-ind', 'value'),
    Input('crossfilter-country', 'value')
)
def update_choropleth(indication, country):
    df_filtered = df if country == 'Все' else df[df['Country'] == country]
    color_column = 'GDP' if indication == 'GDP' else 'Total Time Spent on Devices'
    indication_label = 'ВВП' if indication == 'GDP' else 'Общее время на устройствах в интернете'

    hover_data = {
        'Country': True,
        'GDP': True,
        'Total Time Spent on Devices': True,
        'Internet via Mobiles': True,
        'Internet via Computer': True,
        '% of Population Using the Internet': True,
        'Mobile Internet Speed (Mbps)': True,
        'Fixed Internet Speed (Mbps)': True,
        'Streaming TV (%)': True,
        'Playing Video Games  (%)': True,
        'Time Spent using a game console': True,
        'Daily Time Spent Using Social Media': True
    }

    figure = px.choropleth(
        df_filtered,
        locations='Country',
        locationmode='country names',
        color=color_column,
        hover_name='Country',
        hover_data=hover_data,
        labels={
            'Country': 'Страна',
            'GDP': 'ВВП',
            'Total Time Spent on Devices': 'Общее время на устройствах в интернете(мин)',
            'Internet via Mobiles': 'Использование интернета через мобильные устройства',
            'Internet via Computer': 'Использование интернета через компьютеры',
            '% of Population Using the Internet': '% населения, использующего интернет',
            'Mobile Internet Speed (Mbps)': 'Скорость мобильного интернета (Мбит/с)',
            'Fixed Internet Speed (Mbps)': 'Скорость фиксированного интернета (Мбит/с)',
            'Streaming TV (%)': 'Потоковое ТВ (%)',
            'Playing Video Games  (%)': 'Люди, играющие в видео игры (%)',
            'Time Spent using a game console': 'Ср. кол-во времени, затрачиваемое в игру на консоли пользователями',
            'Daily Time Spent Using Social Media': 'Среднее кол-во минут, затрачиваемое на социальные сети',
            color_column: indication_label
        },
        color_continuous_scale='twilight',
        range_color=(0, 21000),
    )

    figure.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return figure
