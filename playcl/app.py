"""
Describes the actual application itself.
"""

import npyscreen

import playcl.client

class PlayClApp(npyscreen.NPSAppManaged):
	"""
	Application class.
	"""

	def __init__(self):
		"""
		Construct the application.
		"""

		super(PlayClApp, self).__init__()

		self.play_client = None

	def main(self):
		"""
		Main loop of the application
		"""

		npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)

		super(PlayClApp, self).main()

	def onStart(self):
		"""
		Called on application startup.
		"""

		self.registerForm('player', PlayerForm())
		self.registerForm('MAIN', LoginForm())

	def onCleanExit(self):
		"""
		Called on exit of application.
		"""

		if self.play_client:
			self.play_client.logout()

class PlayerForm(npyscreen.FormMutt):
	"""
	The main form of the application and the player.
	"""

	STATUS_BASE = 'Google Play - {0}'

	def create(self):
		"""
		Called on from creation.
		"""

		super(PlayerForm, self).create()

		self.play_client    = None
		self.wStatus1.value = PlayerForm.STATUS_BASE.format('Updating library...')

	def display(self):
		"""
		Called to display the form.
		"""

		self.play_client = self.parentApp.play_client

		self.wStatus1.value = PlayerForm.STATUS_BASE.format(self.play_client.email)

		super(PlayerForm, self).display()

class LoginForm(npyscreen.ActionForm):
	"""
	Login form for the application.
	"""

	def create(self):
		"""
		Called when creating the form.
		"""

		super(LoginForm, self).create()

		self.add(npyscreen.TitleText, w_id = 'email',
				 name = 'Google Email: ', use_two_lines = False)
		self.add(npyscreen.TitlePassword, w_id = 'password',
				 name = 'Google Password: ', use_two_lines = False)

	def on_ok(self):
		"""
		Called when the OK button is clicked.
		"""

		email    = self.get_widget('email').value
		password = self.get_widget('password').value

		self.parentApp.play_client = playcl.client.GooglePlayClient(email, password)

		self.parentApp.switchForm('player')

		# Trigger the update of the library.
		# TODO: make this asynchronous
		self.parentApp.play_client.update_local_music_lib()

	def on_cancel(self):
		"""
		Called when the cancel button is clicked.
		"""

		self.parentApp.switchForm(None)

