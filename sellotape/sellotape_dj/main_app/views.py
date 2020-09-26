from django.http import HttpResponse
from django.shortcuts import render
from .form import StreamForm


def index(request):
    return render(request, 'sellotape/index.html')


def add_stream(request):
    if request.method == 'POST':  # data sent by user
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()  # this will save stream info to database
            return HttpResponse('Stream added to your Streams!')
    else:  # display empty form
        form = StreamForm()

    return render(request, 'add_stream.html', {'stream_form': form})
