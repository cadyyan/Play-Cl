"""
Defines clients for connecting to different services.
"""

import gmusicapi

import playcl.util

class GooglePlayClient(object):
	"""
	A client for connecting to Google Play for music.
	"""

	def __init__(self, email, password):
		"""
		Creates a client that is logged in using the given credentials.
		"""

		if not playcl.util.EMAIL_REGEX.match(email):
			raise ValueError('Username is not a valid email')

		self.play_api = gmusicapi.Webclient()

		if not self.play_api.login(email, password):
			raise RuntimeError('Unable to log in to Google Play. Invalid username or password?')

		self.music_library = {}
		self.playlists     = {}

	def __del__(self):
		print 'Logging out of Google Play...'
		self.play_api.logout()

	def update_local_music_lib(self):
		"""
		Update the local copy of the user's music library.
		"""

		# Clear out the library.
		self.music_library = {}
		self.playlists     = {}

		songs = self.play_api.get_all_songs()

		# Do some formatting on the data that was returned.
		for song in songs:
			if song['artist'] == '':
				song['artist'] = 'Unknown Artist'

			if song['album'] == '':
				song['album'] = 'Unknown Album'

			artist = song['artist']
			if artist not in self.music_library:
				self.music_library[artist] = {}
			artist_albums = self.music_library[artist]

			album = song['album']
			if album not in artist_albums:
				artist_albums[album] = []
			album_tracks = artist_albums[album]

			album_tracks.append(song)

		playlists = self.play_api.get_all_playlist_ids().values()
		for playlist in playlists:
			self.playlists[playlist] = self.play_api.get_playlist_songs(playlist)

