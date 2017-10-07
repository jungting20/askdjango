from django.utils import timezone



#필히 사전을 리턴해줘야함
def blog(request):
    return {
        'current_datetime':timezone.now()
    }