from django.shortcuts import render

# Create your views here.
def member_list(request):
    return render(request, 'match/member_list.html', {})