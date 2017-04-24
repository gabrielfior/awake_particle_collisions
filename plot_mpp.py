username='gabrielfior'
key ='7mvtys8frl'
token='68p1uc2g5f'


import plotly
import plotly.plotly as py
from plotly.graph_objs import *

plotly.tools.set_credentials_file(username=username, api_key=key)


trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

#plotly.offline.plot(data, filename = 'basic-line')
py.plot(data, filename = 'basic-line2')



