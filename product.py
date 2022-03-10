import dash

from dash import dcc, html

from dash.dependencies import Input, Output,State

#import openpyxl 
#import ptl as etl

import pandas as pd
import plotly.express as px
import numpy as np


import per_hour_sales





app =  dash.Dash('', title='Data from Retail Stores')
server = app.server

print('hello world')
def product_top5():                 
    all_data_df_pivot= pd.read_csv('summary.csv')
    return px.scatter(all_data_df_pivot.head(5),x='product', y='amount_in_gbp')

def product_least5():                 
    all_data_df_pivot= pd.read_csv('summary.csv')
    return px.scatter(all_data_df_pivot.tail(5),x='product', y='amount_in_gbp')

def quantity_top10():                 
    all_data_df_pivot= pd.read_csv('quantity.csv')
    return px.bar(all_data_df_pivot.head(10),x='product', y='quantity')

def quantity_least10():                 
    all_data_df_pivot= pd.read_csv('quantity.csv')
    return px.bar(all_data_df_pivot.tail(10),x='product', y='quantity')

def per_hour_sales() :

   
    all_data_df_pivot = pd.read_csv('per_hour.csv')
    return px.line(all_data_df_pivot.head(10),x='hour', y='amount_in_gbp')

def profit_top5 ():
    all_data_df_pivot = pd.read_csv('profit.csv')
    return px.line(all_data_df_pivot.head(5),x='branch', y='profit')

def profit_least5 ():
    all_data_df_pivot = pd.read_csv('profit.csv')
    return px.line(all_data_df_pivot.tail(5),x='branch', y='profit')





 
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
colors = {
    'background': '#ddbea9',
    'text': '#ffffff'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Retail Data',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-size':'80px',
        }
    ),

    html.Div(children='A web application for retail data collected over time from their various branches to understand consumer behaviour in the different regions of the country.',
     style={
        'textAlign': 'center',
        'font-size':'50px',
        'color': colors['text']
    }),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("Click to display a graph that shows the 5 top  product purchased",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-btn-1',style={
        'padding':'10px','color':'#b08968','font-size':'20px'}),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='most_product_graph'),
       
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P(" Click to display a graph that shows the 5 least product purchased",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
    html.Br(),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-btn-2',style={
        'padding':'10px','color':'#b08968','font-size':'20px'}),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='least_product_graph'),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("Click to display a graph that shows the 10 top  performing branches",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-btn-3',style={
        'padding':'10px','color': '#b08968','font-size':'20px'}),
    html.Br(),
    html.Br(),
    html.Br(),   
    dcc.Graph(figure={}, id='most_quantity_graph'),
        
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("Click to display a graph that shows the 10 least performing branches",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-btn-4',style={
        'padding':'10px','color': '#b08968','font-size':'20px'}),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='least_quantity_graph'),
    html.Br(),
    html.Br(),

    html.P("Click to display Per hour sales for the top 10 branches identified ",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-btn-per_hour',style={
        'padding':'10px','color': '#b08968','font-size':'20px'}),
    dcc.Graph(figure={}, id='per_hour_graph'),

    html.P("Click to display the best profitable branches ",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-profit',style={
        'padding':'10px','color': '#b08968','font-size':'20px'}),
    dcc.Graph(figure={}, id='profit_graph'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.P("Click to display the least profitable branches  ",style={
        'font-size':'30px',
        'color': colors['text']}),
    html.Br(),
    html.Br(),
   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Button('Plot Graph', id='plot-graph-profit_least',style={
        'padding':'10px','color': '#b08968','font-size':'20px'}),
    dcc.Graph(figure={}, id='profit_least_graph'),
    


       


])

@app.callback (

    Output(component_id='most_product_graph', component_property='figure'),
    Input(component_id='plot-graph-btn-1', component_property='n_clicks')
    

)
def show_visualisation(button_click):
    print('callback')
    if button_click is not None:
        return product_top5()

    return {}
       
        
    


@app.callback (
    
    Output(component_id='least_product_graph', component_property='figure'),
    Input(component_id='plot-graph-btn-2', component_property='n_clicks')
    
)
def show_visualisation_2(button_click):
    if button_click is not None:
       return product_least5()
    return {} 
        
        
     
@app.callback (

    Output(component_id='most_quantity_graph', component_property='figure'),
    Input(component_id='plot-graph-btn-3', component_property='n_clicks')

)
def show_visualisation_3 (button_click):
    if button_click is not None:
        return quantity_top10()
    return {}    

    


@app.callback (
    Output(component_id='least_quantity_graph', component_property='figure'),
    Input(component_id='plot-graph-btn-4', component_property='n_clicks')
   
)

def show_visualisation_3 (button_click):
    if button_click is not None:
         return quantity_least10()
    return {} 
     

    

@app.callback (
  
    Output(component_id='per_hour_graph', component_property='figure'),
    Input(component_id='plot-graph-btn-per_hour', component_property='n_clicks')
    
)
   

    
def show_vis_per_hour (button_click):
    print('callback')
    if button_click is not None:
        return per_hour_sales()
    return {}


@app.callback (

    Output(component_id='profit_graph', component_property='figure'),
    Input(component_id='plot-graph-profit', component_property='n_clicks')
    
)
   

    
def show_vis_profit (button_click):
    print('callback')
    if button_click is not None:
        return profit_top5()
    return {}


@app.callback (

    Output(component_id='profit_least_graph', component_property='figure'),
    Input(component_id='plot-graph-profit_least', component_property='n_clicks')
    
)
   

    
def show_vis_profit (button_click):
    print('callback')
    if button_click is not None:
        return profit_least5()
    return {}
        
        
        
 

app.run_server(debug= True)
