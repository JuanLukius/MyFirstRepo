from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306216075',
        'name': 'Juan Lukius Barnaby',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
