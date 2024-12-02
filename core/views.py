from django.shortcuts import render, get_object_or_404

from core.models import Speaker


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://abre.ai/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'https://abre.ai/turing-pic'}
    ]
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})
