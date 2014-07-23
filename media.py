import webbrowser

class Movie(object):
	"""docstring for Movie"""
	def __init__(self, title, storyline, image, url):
		self.title = title
		self.storyline = storyline
		self.image = image
		self.url = url


	def show_trailer(self):
		webbrowser.open(self.url)