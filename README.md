Introduction 
-------------

A administration of a well known retail store is interested in using data collected over time
from their various branches to understand consumer behaviour in the different regions of the
country.My plan is to create interactive visualisations using dash to generat their data
which tells a story about their customers.They’ve provided 10 years worth of data collected from all available branches.


Technologies used to clean the data 
-------------------------------------

Use datalore to clean up your data it has notebooks already set up for you.
Then import the files needed.Use the link below.

https://datalore.jetbrains.com/

pip install pandas

pip install petl

Then import pandas as pd

import petl as etl

Cleaning the Data 
------------------


Project is split into two parts. The data is inconsistent in terms of format and content as the data collection and storage strategy is
decided by the manager of a store branch. Due to the data being inconsistent, their were errors in the data that had to be fixed. 

for example : I have imported the East lindey branch.

First, I have to read the data that has been imported and store it in a data frame  . Then with the data fix any errors that may occur. 
all the data given need to have the same headings for example total_quantity was quantity and sku or item was changed to product.



Technologies used for making a Dash board
------------------------------------------

pip install pandas 

pip insatll dash 

pip insatll numpy

pip install petl 

pip install plotly.express


Creating the Dash board
------------------------


Once, all the data is cleaned use the files and open up visual studio code.
create a product.py - this is were the layout, functions and callbacks will go.

fisrt import all the dependencies needed in product.py


import dash

from dash import dcc, html

from dash.dependencies import Input, Output,State


import pandas as pd

import plotly.express as px

import numpy as np


Layout
-------

Then you can start with the layout of your dash board and slowly bulid your layout.




      app.layout = html.Div( 

    
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
       
    ])
    
    
    You can add as many graph for the diffrent data you want to display.
    
    
   
   
   
   Callbacks 
   ---------
   
   
A callback consist of a Output and a Input.For this call back the output will be a graph and the input will be a button. When the button is click it should 
show the graph.



Function
---------



 

     
      def show_visualisation(button_click):
    print('callback')
    if button_click is not None:
        return product_top5()
        return {}
 
 
 This fuction is to show the visualisation of the graph once the button is clicked.
 
 
 This the basics components needed for you to build your Dash board.
 
 
 You can run python3 product.py and it should give you a link.
 
 
 graph data 
 -------------------------
 
create a new file and name it product2.py . Also create a empty file call pivot.
 
import this dependencies :

 
import pandas as pd 

import os

import numpy as np


You will have to  are make a for loop that go through each of the files that end with .csv or .json and from that data I only want product and the amount in gbp. Once you have done this, make sure you have done this for all of your data.
After that yu will need to save his new table into a new folder. I have created a pivot folder and in that folder i have named a file called summary.csv and this is the where the new data will go.
You will repeat the process for quantity , per hour. and profitable branch. 

You should have a summary.csv in the folder called pivot. Take the summary.csv out of the folder so you have access to it.
Then go back to your product.py and you are going to create a function that reads the new data from summary.csv and with that data return a graph that displays the top 5 products.

 
     
 








    
    
    
    
















user stories
 -------------

 As a user I want to track the most wanted iteams so that I can see which product is performing well.

 As a user I want to track the least wanted iteams so that I can see which product is not performing well.

 As a user I want to track the 10 least performing branches so that I can see which branch is not performing well.

As a user I want to track the 10 best performing branches so that I can see which branch is performing well.

As a user I want to track sales per hour for the top 10 braches so that I can see which branchs are in the top 10.

 As a user I want Identify the top 10 profitable braches so that I can indicate how profitable the braches are.

 As a user I want Identify the bottom 10 profitable braches so that I can indicate which branches are the least profitable.
