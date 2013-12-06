"""
Defines the actual media player.
"""

import thread

class MediaPlayer(object):
	"""
	Plays media in some fashion or another.
	"""

	def __init__(self):
		"""
		Creates a new media player instance.
		"""

		self.player_thread = thread.start_new_thread(self.run, ())

	def run(self):
		"""
		Runs as a separate thread to play media.
		"""

		pass # TODO: do player

