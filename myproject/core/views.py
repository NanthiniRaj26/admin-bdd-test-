import time
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from .decorators import LogExecutionTime

# 👇 Class-based view with execution time logging
@method_decorator(LogExecutionTime, name='get')
class ReportView(View):
    def get(self, request):
        time.sleep(1.5)
        return JsonResponse({'status': 'Report generated'})

# 👇 Simple homepage view
def home(request):
    return HttpResponse("<h2>Welcome to Nanthini's Django Site 🎉</h2>")
