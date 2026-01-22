import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import os

# Load the data using pandas
# Handle both local and deployed paths
if os.path.exists('../data/automobile_sales.csv'):
    data_path = '../data/automobile_sales.csv'
elif os.path.exists('data/automobile_sales.csv'):
    data_path = 'data/automobile_sales.csv'
else:
    data_path = 'automobile_sales.csv'

data = pd.read_csv(data_path)

# Initialize the Dash app
app = dash.Dash(__name__)

app.title = "Automobile Sales Statistics Dashboard"

# Server for deployment
server = app.server

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div(children=[
    # 1. Professional Header Section
    html.Div([
        html.H1("Automobile Sales Statistics Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'font-size': 32, 'font-family': 'Arial, sans-serif', 'padding-top': '20px'}),
        html.P("Analyzing historical sales data across recessionary and stable economic cycles.",
               style={'textAlign': 'center', 'color': '#7f8c8d', 'font-size': 18, 'margin-bottom': '30px'})
    ], style={'backgroundColor': '#f8f9fa', 'borderBottom': '2px solid #e9ecef', 'padding': '10px'}),

    # 2. Controls Section (Dropdowns)
    html.Div([
        # Statistics Selection
        html.Div([
            html.Label("Select Report Category:", style={'font-weight': 'bold', 'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown-statistics',
                options=dropdown_options,
                value='Select Statistics',
                placeholder='Choose a Report Type',
                style={'width': '100%', 'padding': '3px', 'font-size': '16px'}
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),

        # Year Selection
        html.Div([
            html.Label("Select Target Year:", style={'font-weight': 'bold', 'margin-right': '10px'}),
            dcc.Dropdown(
                id='select-year',
                options=[{'label': i, 'value': i} for i in year_list],
                value='Select Year',
                placeholder='Choose a Year',
                style={'width': '100%', 'padding': '3px', 'font-size': '16px'}
            )
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'margin': '20px auto', 'width': '90%', 'display': 'flex', 'justify-content': 'space-between'}),

    # 3. Output Display Container
    html.Div(id='output-container', style={'padding': '20px', 'margin': '0 auto', 'width': '95%'})
])

# Callback for enabling/disabling year selection
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='value'))

def update_input_container(selected_statistics):
    if selected_statistics =='Yearly Statistics': 
        return False
    else: 
        return True

#Callback for plotting
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')])
def update_output_container(selected_statistics, input_year):
    # --- RECESSION REPORT ---
    if selected_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]
        
        # Plot 1: Sales Trend
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                           title="Automobile Sales Trend (Recession Periods)",
                           template='plotly_white'))

        # Plot 2: Avg Sales by Type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
                          title="Avg Sales by Vehicle Type (Recession)",
                          template='plotly_white'))
        
        # Plot 3: Ad Spend
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type',
                          title="Ad Spend Share by Vehicle Type", template='plotly_white'))

        # Plot 4: Unemployment impact
        unemp_data = recession_data.groupby(['unemployment_rate','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(unemp_data, x='unemployment_rate', y='Automobile_Sales', color='Vehicle_Type',
                          title='Unemployment Rate vs. Sales', template='plotly_white'))

        # PRO FEATURE: Calculate Recession KPIs
        total_rec_sales = recession_data['Automobile_Sales'].sum()
        avg_rec_sales = recession_data['Automobile_Sales'].mean()

        return html.Div([
            # KPI Row
            html.Div([
                html.Div([
                    html.H4("Total Recession Sales"),
                    html.P(f"{total_rec_sales:,.0f}", style={'fontSize': 24, 'color': '#e74c3c', 'fontWeight': 'bold'})
                ], style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'width': '30%', 'textAlign': 'center'}),
                html.Div([
                    html.H4("Avg Sales per Month"),
                    html.P(f"{avg_rec_sales:,.2f}", style={'fontSize': 24, 'color': '#e74c3c', 'fontWeight': 'bold'})
                ], style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'width': '30%', 'textAlign': 'center'}),
            ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '20px'}),

            # Charts Grid
            html.Div(children=[R_chart1, R_chart2, R_chart3, R_chart4],
                     style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'})
        ])

    # --- YEARLY REPORT ---
    elif (selected_statistics == 'Yearly Statistics'):
        if input_year == 'Select Year' or input_year is None:
            return html.H2("Please select a year from the dropdown to view the report.", 
                           style={'textAlign':'center', 'color':'#7f8c8d', 'margin-top': '40px'})
        
        # 1. Use .copy() to avoid the 'SettingWithCopy' warning you saw earlier
        yearly_data = data[data['Year'] == int(input_year)].copy()
        
        # 2. PRO MOVE: Force months to stay in Calendar Order (Jan, Feb, Mar...)
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        yearly_data['Month'] = pd.Categorical(yearly_data['Month'], categories=month_order, ordered=True)
        
        # 3. Add observed=False to avoid the 'FutureWarning' in your console
        mas = yearly_data.groupby('Month', observed=False)['Automobile_Sales'].sum().reset_index()
        
        # Plot 1: Overall Trend
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales', 
                                           title='Overall Yearly Sales Trend (1980-2023)', template='plotly_white'))
            
        # Plot 2: Monthly Sales (Now sorted Jan -> Dec)
        Y_chart2 = dcc.Graph(figure=px.line(mas, x='Month', y='Automobile_Sales',
                                           title=f'Monthly Sales Trend in {input_year}', template='plotly_white'))

        # Plot 3: Avg Sales per Vehicle Type
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales',
                                          title=f'Avg Vehicles Sold by Type in {input_year}', template='plotly_white'))

        # Plot 4: Ad Spend per Vehicle Type
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type',
                                          title=f'Ad Spend per Vehicle Type in {input_year}', template='plotly_white'))

        # PRO FEATURE: Calculate Yearly KPIs
        yearly_total = yearly_data['Automobile_Sales'].sum()
        best_month = mas.loc[mas['Automobile_Sales'].idxmax(), 'Month']

        return html.Div([
            # KPI Row
            html.Div([
                html.Div([
                    html.H4(f"Total Sales in {input_year}"),
                    html.P(f"{yearly_total:,.0f}", style={'fontSize': 24, 'color': '#27ae60', 'fontWeight': 'bold'})
                ], style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'width': '30%', 'textAlign': 'center'}),
                html.Div([
                    html.H4("Peak Performance Month"),
                    html.P(f"{best_month}", style={'fontSize': 24, 'color': '#27ae60', 'fontWeight': 'bold'})
                ], style={'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'width': '30%', 'textAlign': 'center'}),
            ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '20px'}),

            # Charts Grid
            html.Div(children=[Y_chart1, Y_chart2, Y_chart3, Y_chart4],
                     style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'})
        ])
    
    return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
