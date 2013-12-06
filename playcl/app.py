"""
Describes the actual application itself.
"""

import npyscreen

class PlayClApp(npyscreen.NPSAppManaged):
	"""
	Application class.
	"""

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

		#self.registerForm('player', PlayerForm())
		self.registerForm('MAIN', LoginForm())

		npyscreen.setTheme(npyscreen.Themes.TransparentThemeDarkText)

class PlayerForm(npyscreen.FormMutt):
	"""
	The main form of the application and the player.
	"""

	def create(self):
		"""
		Called on from creation.
		"""

		super(PlayerForm, self).create()
		self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application

	def exit_application(self):
		"""
		Quit the application.
		"""

		self.parentApp.NEXT_ACTIVE_FORM = None
		self.editing = False

class LoginForm(npyscreen.ActionForm):
	"""
	Login form for the application.
	"""

	def create(self):
		"""
		Called when creating the form.
		"""

		super(LoginForm, self).create()

		self.add(npyscreen.TitleText, name = 'Google Email: ', use_two_lines = False)
		self.add(npyscreen.TitlePassword, name = 'Google Password: ', use_two_lines = False)

	def on_ok(self):
		"""
		Called when the OK button is clicked.
		"""

	def on_cancel(self):
		"""
		Called when the cancel button is clicked.
		"""

