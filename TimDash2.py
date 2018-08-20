# Acquires a single sample from the USB1608G and displays it.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType, AiInputMode, Range, AInFlag)

app = dash.Dash()

#app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H1(children='DSL Dyno App'),
    dcc.Graph(
        id='DSL Scatter',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Force-Displacement'
            }
        }
    ),
    dcc.Slider(value=4, min=-10, max=20, step=0.5, marks={-5: '-5 Degrees', 0: '0', 10: '10 Degrees'}),
    html.Hr(),
    html.Button(id='acq-button', n_clicks=0, children='Acquire'),
    html.Div(id='output-state')
])

@app.callback(
    Output('output-state', 'children'),
    [Input('acq-button', 'n_clicks')])
def click(num):
    data=555
    try:
        # Get a list of available DAQ devices
        devices = get_daq_device_inventory(InterfaceType.USB)
        # Create a DaqDevice Object and connect to the device
        daq_device = DaqDevice(devices[0])
        daq_device.connect()
        daq_device.flash_led(3)
        # Get AiDevice and AiInfo objects for the analog input subsystem
        ai_device = daq_device.get_ai_device()
        ai_info = ai_device.get_info()
        print(ai_info)
        # Read and display voltage values for all analog input channels
        for channel in range(1):
            data = ai_device.a_in(channel, AiInputMode.SINGLE_ENDED,
                                  Range.BIP10VOLTS, AInFlag.DEFAULT)
            print('Channel', channel, 'Data:', data)

        daq_device.disconnect()
        daq_device.release()
    except:
        print('some error')  
    return data


if __name__ == '__main__':
    app.run_server(debug=True)