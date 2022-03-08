from django.shortcuts import render
from django.http import HttpResponse
from .models import Forecast

# Create your views here.
def index(request):
    """
    Контроллер для отображения на главной странице списка всех записей.
    """
    list_of_forecast = Forecast.objects.all()
    context = {'list_of_forecast': list_of_forecast}
    return render(
        request=request,
        template_name='daily_horoscopes/index.html',
        context=context
    )
