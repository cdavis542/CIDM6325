# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum, Avg, Min 

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_x=Sum('passengers')) \
                        .order_by('-total_x')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_x=Sum('passengers')) \
                                 .order_by('-total_x')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFrxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_x=Sum('freight')) \
                        .order_by('-total_x')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFrxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_x=Sum('freight')) \
                                 .order_by('-total_x')[0:5]
    template_name="rankorder_list_destination.html"

# Total mail origin
class Top5AirportsMxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_x=Sum('mail')) \
                        .order_by('-total_x')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_x=Sum('mail')) \
                                 .order_by('-total_x')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_x=Sum('distance')) \
                        .order_by('-total_x')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_x=Sum('distance')) \
                                 .order_by('-total_x')[0:5]
    template_name="rankorder_list_destination.html"


# Which airport reported the most passangers by month?
class TopPassengerByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_x=Max('passengers')) \
                .order_by('-total_x')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_x=Max('distance')) \
                .order_by('-total_x')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class TopAirlineFreight(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects.values('carrier_name') \
                                 .annotate(total_x=Sum('freight')) \
                                 .order_by('-total_x')[0:1]
    template_name="discrete_carrier.html"

class TopAirlinePassengers(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects.values('carrier_name') \
                                 .annotate(total_x=Sum('passengers')) \
                                 .order_by('-total_x')[0:1]
    template_name="discrete_carrier.html"

class TopAirlineMail(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects.values('carrier_name') \
                                 .annotate(total_x=Sum('mail')) \
                                 .order_by('-total_x')[0:1]
    template_name="discrete_carrier.html"

class TopAirlineDistance(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects.values('carrier_name') \
                                 .annotate(total_x=Sum('distance')) \
                                 .order_by('-total_x')[0:1]
    template_name="discrete_carrier.html"


# Carrier passengers by month?
class PassengersByMonth(ListView):
    context_object_name = "carrier_list"
    template_name="carrier_by_month.html"
    carrier = ''
    def get_queryset(self, **kwargs):
        carrier = self.kwargs['car']
        queryset = MarketData.objects \
        .values('carrier_name',
        'month') \
        .filter(carrier_id__exact= carrier) \
        .annotate(total_x=Sum('passengers')) \
        .order_by('-total_x')
        return queryset
    airline = MarketData.objects.values('carrier_name').filter(carrier_id__exact= carrier)

class PassengersByDesitination(ListView):
    context_object_name = "dest_list"
    template_name="averages.html"
    carrier = ''
    def get_queryset(self, **kwargs):
        carrier = self.kwargs['car']
        queryset = MarketData.objects \
        .values('dest_city_name', 'dest_iata_code'
        ) \
        .filter(dest_iata_code__exact= carrier) \
        .annotate(total_x= Avg('passengers'))

        return queryset

    airline = MarketData.objects.values('dest_city_name').filter(dest_iata_code__exact= carrier)


class FreightByOrigin(ListView):
    context_object_name = "dest_list"
    template_name="averages.html"
    carrier = ''
    def get_queryset(self, **kwargs):
        carrier = self.kwargs['car']
        queryset = MarketData.objects \
        .values('orig_city_name', 'orig_iata_code'
        ) \
        .filter(orig_iata_code__exact= carrier) \
        .annotate(total_x= Avg('freight'))

        return queryset

    airline = MarketData.objects.values('orig_city_name').filter(orig_iata_code__exact= carrier)
  

class FreightByDistance(ListView):
    context_object_name = "dest_list"
    template_name="citypairs.html"
    queryset = MarketData.objects \
        .values('orig_city_name', 'orig_iata_code', 'dest_city_name', 'dest_iata_code', 'freight', 'distance') \
        .annotate(total_x= Max('freight'), total_y=Max('distance')).order_by('-freight','-distance')

class MailByDistance(ListView):
    context_object_name = "dest_list"
    template_name="citypairs.html"
    queryset = MarketData.objects \
        .values('orig_city_name', 'orig_iata_code', 'dest_city_name', 'dest_iata_code', 'mail', 'distance') \
        .annotate(total_x= Max('mail'), total_y=Min('distance')).order_by('-mail','distance')


