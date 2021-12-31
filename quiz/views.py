from django.shortcuts import render

def index_view(request, *args, **kwargs):
    return render(request, "index.html")

# def about_view(request, *args, **kwargs):
#     queryset = About.objects.all()
#     return render(request, "about.html", {"about": queryset})