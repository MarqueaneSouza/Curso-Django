from django.shortcuts import render


videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivacao'},
    {'slug': 'intalacao-windows', 'titulo': 'Instalacao Windows'},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
