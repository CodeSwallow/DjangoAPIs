from django.http import HttpResponse
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from geography.models import Country, Continent, City
from geography.serializers import CountrySerializer, ContinentSerializer, CitySerializer

# Create your views here.


class CountryViewSet(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

    @action(detail=True)
    def flag(self, request, pk=None):
        country = self.get_object()
        if country.flag:
            return HttpResponse(country.flag, content_type="image/png")
        return Response({'data': 'No flag found'})

    @action(detail=False)
    def by_population(self, request):
        ascending = int(self.request.query_params.get('ascending', 0))
        asc = "-population"
        if ascending:
            asc = "population"
        countries = Country.objects.all().order_by(asc)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def by_land_area(self, request):
        ascending = int(self.request.query_params.get('ascending', 0))
        asc = "-land_area"
        if ascending:
            asc = "land_area"
        countries = Country.objects.all().order_by(asc)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)


class ContinentViewSet(ReadOnlyModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

    @action(detail=False)
    def by_population(self, request):
        asc = "-population"
        ascending = int(self.request.query_params.get('ascending', 0))
        if ascending:
            asc = "population"
        continents = Continent.objects.all().order_by(asc)
        serializer = self.get_serializer(continents, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def by_land_area(self, request):
        asc = "-land_area"
        ascending = int(self.request.query_params.get('ascending', 0))
        if ascending:
            asc = "land_area"
        continents = Continent.objects.all().order_by(asc)
        serializer = self.get_serializer(continents, many=True)
        return Response(serializer.data)


class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

    @action(detail=False)
    def by_population(self, request):
        ascending = int(self.request.query_params.get('ascending', 0))
        asc = "-population"
        if ascending:
            asc = "population"
        cities = City.objects.all().order_by(asc)
        serializer = self.get_serializer(cities, many=True)
        return Response(serializer.data)
