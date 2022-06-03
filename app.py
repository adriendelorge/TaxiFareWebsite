import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''

''')
from datetime import datetime
import pytz
#d = st.date_input("Pick Up Date",datetime.date()) ?
d = st.date_input("PickUp Date")
t = st.time_input('PickUp Time', value=datetime.now())
plon = st.number_input('PickUp Longitude', format="%.15f",step=1e-15)
plat = st.number_input('PickUp Latitude', format="%.15f",step=1e-15)
dlon = st.number_input('DropOff Longitude', format="%.15f",step=1e-15)
dlat = st.number_input('DropOff Latitude', format="%.15f",step=1e-15)
pcount = st.number_input('Passenger Count',min_value=1, max_value=10, value=1, step=1)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(' ')

    combined = datetime.combine(d, t)

    dic={"pickup_datetime": [combined],
        "pickup_longitude": [plon],
        "pickup_latitude": [plat] ,
        "dropoff_longitude": [dlon],
        "dropoff_latitude": [dlat],
        "passenger_count": [pcount]
        }

    import requests

    url_complete=f'https://taxifare.lewagon.ai/predict?pickup_datetime={combined}&pickup_longitude={plon}&pickup_latitude=-{plat}&dropoff_longitude={dlon}&dropoff_latitude={dlat}&passenger_count={pcount}'

    response = requests.get(url_complete).json()

    st.write('Your fare is',response["fare"])
