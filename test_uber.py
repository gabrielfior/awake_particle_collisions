# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:46:15 2017

@author: gabrielfior
"""
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from geopy.geocoders import Nominatim


geolocator = Nominatim()

server_token = 'SGcqySIBULwEWPTq2SaXhEIu2WwubNnzmdbPUsUQ'

session = Session(server_token=server_token)
client = UberRidesClient(session)

response = client.get_products(37.77, -122.41)
products = response.json.get('products')

masp = geolocator.geocode("MASP, Sao Paulo")
borbaGato = geolocator.geocode("Borba gato, Sao Paulo")

run_paulista = client.get_price_estimates(
    start_latitude=masp.latitude,
    start_longitude=masp.longitude,
    end_latitude=borbaGato.latitude,
    end_longitude=borbaGato.longitude,
    seat_count=1
)
estimate_paulista = run_paulista.json.get('prices')

print estimate_paulista