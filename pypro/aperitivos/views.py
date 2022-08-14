from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivacao'},
        'instalacao-windows': {'titulo': 'Instalacao Windows '},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
