# urls.py
from django.urls import path
from . views import *        


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport", 'content': 'Passengers'}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport", 'content': 'Passengers'}
        ), 
        name="top5paxdestination"),


    path('top5frxorigin/', 
        Top5AirportsFrxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport", 'content': 'Freight'}
        ),
        name="top5frxorigin"),
    path('top5frxdestination/',  
        Top5AirportsFrxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport", 'content': 'Freight'}
        ), 
        name="top5frxdestination"),


    path('top5mxorigin/', 
        Top5AirportsMxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport", 'content': 'Mail'}
        ),
        name="top5mxorigin"),
    path('top5mxdestination/',  
        Top5AirportsMxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport", 'content': 'Mail'}
        ), 
        name="top5mxdestination"),

    path('top5dxorigin/', 
        Top5AirportsDxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport", 'content': 'Distance'}
        ),
        name="top5dxorigin"),
    path('top5Dxdestination/',  
        Top5AirportsDxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport", 'content': 'Distance'}
        ), 
        name="top5dxdestination"),

    path('toppassenger_month/',  
        TopPassengerByMonth.as_view(
            extra_context={'title': "Top Passengers by Month", "content" : 'Passengers'}
        ), 
        name="toppassenger_month"),

    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month", "content" : 'Distance'}
        ), 
        name="topdistance_month"),

    path('topairline_freight/',  
        TopAirlineFreight.as_view(
            extra_context={'title': "Top Airline for Freight", "content" : 'Freight'}
        ), 
        name="topairline_freight"),
            
    path('topairline_passengers/',  
        TopAirlinePassengers.as_view(
            extra_context={'title': "Top Airline for Passengers", "content" : 'Passengers'}
        ), 
        name="topairline_passengers"),
            
    path('topairline_mail/',  
        TopAirlineMail.as_view(
            extra_context={'title': "Top Airline for Mail", "content" : 'Mail'}
        ), 
        name="topairline_mail"),
            
    path('topairline_distance/',  
        TopAirlineDistance.as_view(
            extra_context={'title': "Top Airline for Distance", "content" : 'Distance'}
        ), 
        name="topairline_distance"),

    path('passengers_by_month/<car>',
        PassengersByMonth.as_view(
            extra_context={'title': "Rank Passengers per Month for ", 'content': "Passengers"}
        ),
        name='passengers_by_month'),

    path('passengers_by_destination/<car>',
        PassengersByDesitination.as_view(
            extra_context={'title': "Average Passengers for Flights to ", 'content': "Passengers"}
        ),
        name='passengers_by_destination'),

    path('freight_by_origin/<car>',
        FreightByOrigin.as_view(
            extra_context={'title': "Average Freight for Flights from ", 'content': "Freight"}
        ),
        name='freight_by_destination'),

    path('freight_by_distance/',
        FreightByDistance.as_view(
            extra_context={'title': "Largest Freight by Distance", 'content': "Freight", 'content2' : 'Distance'}
        ),
        name='freight_by_distance'),

    path('mail_by_distance/',
        FreightByDistance.as_view(
            extra_context={'title': "Most Mail by Sortest Distance", 'content': "Mail", 'content2' : 'Distance'}
        ),
        name='mail_by_distance'),

]

