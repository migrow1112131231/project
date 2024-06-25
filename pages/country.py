from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df

def convert_time_to_minutes(time_obj):
    try:
        return time_obj.hour * 60 + time_obj.minute
    except Exception as e:
        print(f"Error converting time: {e}")
        return 0

df['Total Time Spent on Devices'] = df['Total Time Spent on Devices'].apply(convert_time_to_minutes)

df['Daily Time Spent Using Social Media'] = df['Daily Time Spent Using Social Media'].apply(convert_time_to_minutes)

top_countries_internet = df.nlargest(10, '% of Population Using the Internet')

fig_internet = px.bar(df.sort_values('% of Population Using the Internet', ascending=False),
             x='Country',
             y='% of Population Using the Internet',
             labels={'Country': '', '% of Population Using the Internet': '% населения'})

fig_internet.update_layout(
    title='Использование интернета',
    title_x=0.5
)

fig_devices_pie = px.pie(top_countries_internet, values='Total Time Spent on Devices', names='Country',
                         title='Общее время на устройствах по топ-10 странам')

fig_devices_pie.update_layout(
    title='Общее время в интернете на всех устройствах',
    title_x=0.5
)

fig_social_media_bar = px.bar(top_countries_internet, x='Daily Time Spent Using Social Media', y='Country', orientation='h',
                              labels={'Daily Time Spent Using Social Media': 'Ежедневное время в социальных сетях (в минутах)', 'Country': ''},
                              title='Ежедневное время в социальных сетях по топ-10 странам')

fig_social_media_bar.update_layout(
    title='Использование интернета для социальных сетей',
    title_x=0.5
)

layout = dbc.Container([
    html.H1("Использование интернета и социальных сетей по странам"),
    html.Hr(style={'color': 'black'}),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                [html.H3("Топ 10 стран мира:")] +
                [html.P(f"{row['Country']} - {row['% of Population Using the Internet']}%") for _, row in top_countries_internet.iterrows()],
                style={"border": "1px solid black"},
                body=True
            ),
            width=4
        ),
        dbc.Col(
            dbc.Card(
                dcc.Graph(figure=fig_internet),
                body=True,
                style={"border": "1px solid black"}
            ),
            width=8
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dcc.Graph(figure=fig_devices_pie),
                body=True,
                style={"border": "1px solid black"}
            ),
            width=12
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dcc.Graph(figure=fig_social_media_bar),
                body=True,
                style={"border": "1px solid black"}
            ),
            width=12
        )
    ])
])
