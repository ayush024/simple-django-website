from django.shortcuts import render, get_object_or_404
#from django.http import Http404
from .models import Album, Song

def index(request):
	albums = Album.objects.all()
	return render(request,'music/index.html', {'all_albums' : albums}) 

def detail(request, album_id):
#	try:
#		album = Album.objects.get(pk=album_id)
#	except Album.DoesNotExist:
#		raise Http404("Album cannot be found.")
	album = get_object_or_404(Album, pk=album_id)

	return render(request, 'music/details.html', {'albums':album} )
	
def favourite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song=Album.song_set.get(id=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request, 'music/details.html', {'albums':album,
		'error_message': "You selected an invalid song",} )
	else:
		selected_song.is_favourite=True
		selected_song.save()
		return render(request, 'music/details.html', {'albums':album})
		
	

	