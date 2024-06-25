from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df

available_indicators = [
    {'label': 'ВВП', 'value': 'GDP'},
    {'label': 'Общее время использования', 'value': 'Total Time Spent on Devices'},
    {'label': 'Мобильные устройства', 'value': 'Internet via Mobiles'},
    {'label': 'Компьютеры и ноутбуки', 'value': 'Internet via Computer'},
    {'label': 'Использование интернета населением', 'value': '% of Population Using the Internet'},
    {'label': 'Скорость мобильного интернета', 'value': 'Mobile Internet Speed (Mbps)'},
    {'label': 'Скорость фиксированного интернета (LAN)', 'value': 'Fixed Internet Speed (Mbps)'},
    {'label': 'Использование потокового ТВ', 'value': 'Streaming TV (%)'},
    {'label': 'Компьютерные игры', 'value': 'Playing Video Games (%)'},
    {'label': 'Игровые консоли', 'value': 'Time Spent using a game console'},
    {'label': 'Социальные сети', 'value': 'Daily Time Spent Using Social Media'}
]

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("Сравнение показателей стран мира"),
                html.Hr(style={'color': 'black'}),
            ])
        )
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Выберите критерий:"),
            dcc.Dropdown(
                id='crossfilter-indicators',
                options=available_indicators,
                value='GDP',
            ),
            dbc.Label("Выберите страну:"),
            dcc.Dropdown(
                id='crossfilter-country-indicators',
                options=[{'label': 'Все', 'value': 'Все'}] + [{'label': i, 'value': i} for i in df['Country'].unique()],
                value='Все',
                multi=True
            ),
        ], width=12),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='indicator-graphic', config={'displayModeBar': False}),
        ], width=12)
    ])
])




@callback(
    Output('indicator-graphic', 'figure'),
    Input('crossfilter-indicators', 'value'),
    Input('crossfilter-country-indicators', 'value'))
def update_graph(indicator_name, countries):
    if not countries or (isinstance(countries, str) and countries == 'Все'):
        return {}

    if isinstance(countries, str):
        countries = [countries]

    if 'Все' in countries:
        df_filtered = df.copy()
    else:
        df_filtered = df[df['Country'].isin(countries)]

    yaxis = ''
    if indicator_name == 'GDP':
        df_filtered = df_filtered[df_filtered['GDP'] <= 21000].sort_values('GDP')
        fig = px.bar(df_filtered, x='Country', y='GDP', labels={'Country': 'Страна', 'GDP': 'ВВП'})
        fig.update_layout(title='ВВП')
        fig.update_yaxes(range=[0, df_filtered['GDP'].max()*1.1], title_text='ВВП', showgrid=True)
    elif indicator_name == 'Total Time Spent on Devices':
        df_filtered = df_filtered.sort_values('Total Time Spent on Devices')
        fig = px.bar(df_filtered, x='Country', y='Total Time Spent on Devices', labels={'Country': 'Страна', 'Total Time Spent on Devices': 'Общее время на устройствах'})
        fig.update_layout(title='Общее время в интернете на всех устройствах по странам')
        fig.update_yaxes(range=[0, df_filtered['Total Time Spent on Devices'].max()*1.1], title_text='Общее время на устройствах', showgrid=True)
        yaxis = 'Ср. кол-во минут в день'
    elif indicator_name == 'Internet via Mobiles':
        df_filtered['Internet via Mobiles'] = df_filtered['Internet via Mobiles'].apply(lambda x: x.hour * 60 + x.minute)
        df_filtered = df_filtered.sort_values('Internet via Mobiles')
        fig = px.bar(df_filtered, x='Country', y='Internet via Mobiles', labels={'Country': 'Страна', 'Internet via Mobiles': 'Интернет через мобильные устройства'})
        fig.update_layout(title='Использование интернета через мобильные устройства')
        fig.update_yaxes(range=[0, df_filtered['Internet via Mobiles'].max()*1.1], title_text='Интернет через мобильные', showgrid=True)
        yaxis = 'Ср. кол-во минут в день'
    elif indicator_name == 'Internet via Computer':
        df_filtered['Internet via Computer'] = df_filtered['Internet via Computer'].apply(lambda x: x.hour * 60 + x.minute)
        df_filtered = df_filtered.sort_values('Internet via Computer')
        fig = px.bar(df_filtered, x='Country', y='Internet via Computer', labels={'Country': 'Страна', 'Internet via Computer': 'Интернет через компьютеры и ноутбуки'})
        fig.update_layout(title='Использование интернета через персональные компьютеры и ноутбуки')
        yaxis = 'Ср. кол-во времени в день'
    elif indicator_name == '% of Population Using the Internet':
        df_filtered = df_filtered.sort_values('% of Population Using the Internet')
        fig = px.bar(df_filtered, x='Country', y='% of Population Using the Internet', labels={'Country': 'Страна', '% of Population Using the Internet': '% населения'})
        fig.update_layout(title='Использование интернета населением')
        yaxis = 'Процент населения, %'
    elif indicator_name == 'Mobile Internet Speed (Mbps)':
        df_filtered = df_filtered.sort_values('Mobile Internet Speed (Mbps)')
        fig = px.bar(df_filtered, x='Country', y='Mobile Internet Speed (Mbps)', labels={'Country': 'Страна', 'Mobile Internet Speed (Mbps)': 'Скорость мобильного интернета'})
        fig.update_layout(title='Скорость мобильного интернета')
        yaxis = 'Мбит/с'
    elif indicator_name == 'Fixed Internet Speed (Mbps)':
        df_filtered = df_filtered.sort_values('Fixed Internet Speed (Mbps)')
        fig = px.bar(df_filtered, x='Country', y='Fixed Internet Speed (Mbps)', labels={'Country': 'Страна', 'Fixed Internet Speed (Mbps)': 'Скорость фиксированного интернета'})
        fig.update_layout(title='Скорость фиксированного интернета')
        yaxis = 'Мбит/с'
    elif indicator_name == 'Streaming TV (%)':
        df_filtered = df_filtered.sort_values('Streaming TV (%)')
        fig = px.bar(df_filtered, x='Country', y='Streaming TV (%)', labels={'Country': 'Страна', 'Streaming TV (%)': 'Просмотр потокового ТВ (%)'})
        fig.update_layout(title='Использование потокового ТВ населением')
        yaxis = 'Процент, %'
    elif indicator_name == 'Playing Video Games (%)':
        df_filtered = df_filtered.sort_values('Playing Video Games  (%)')
        fig = px.bar(df_filtered, x='Country', y='Playing Video Games  (%)', labels={'Country': 'Страна', 'Playing Video Games  (%)': 'Игры по странам (%)'})
        fig.update_layout(title='Процент пользователей интернета в стране, которые играют в компьютерные игры')
        yaxis = 'Процент, %'
    elif indicator_name == 'Time Spent using a game console':
        df_filtered['Time Spent using a game console'] = df_filtered['Time Spent using a game console'].apply(lambda x: x.hour * 60 + x.minute)
        df_filtered = df_filtered.sort_values('Time Spent using a game console')
        fig = px.bar(df_filtered, x='Country', y='Time Spent using a game console', labels={'Country': 'Страна', 'Time Spent using a game console': 'Время, проведенное с игровой консолью'})
        fig.update_layout(title='Среднее время, которое пользователи проводят, играя на игровых консолях')
        yaxis = 'Ср. кол-во минут в день'
    elif indicator_name == 'Daily Time Spent Using Social Media':
        # df_filtered['Daily Time Spent Using Social Media'] = df_filtered['Daily Time Spent Using Social Media'].apply(lambda x: x.hour * 60 + x.minute)
        df_filtered = df_filtered.sort_values('Daily Time Spent Using Social Media')
        fig = px.bar(df_filtered, x='Country', y='Daily Time Spent Using Social Media', labels={'Country': 'Страна', 'Daily Time Spent Using Social Media': 'Время, проведенное в социальных сетях'})
        fig.update_layout(title='Среднее кол-во минут, затрачиваемое на социальные сети')
        yaxis = 'Ср. кол-во минут в день'
    else:
        return {}

    fig.update_layout(xaxis_title='', yaxis_title=yaxis)
    fig.update_layout(margin={"r": 0, "t": 30, "l": 0, "b": 30})
    return fig
