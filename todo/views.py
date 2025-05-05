from django.shortcuts import render, redirect


def signup(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
    return render(request, 'sign.html')