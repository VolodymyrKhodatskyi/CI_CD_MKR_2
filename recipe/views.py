from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def category_list(request):
    return render(request, 'category_list.html')