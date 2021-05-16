from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    number = request.GET['team']
    if number == '2':
        output = "이 팀이 2팀이네ㅎㅎ "
    else:
        output = "저희가 많이 보죠"
    return render(request, "result.html", {'output' : output})