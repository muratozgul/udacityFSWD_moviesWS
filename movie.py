import webbrowser
from video import Video

class Movie(Video):
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, duration, image_url, storyline, video_url):
		Video.__init__(self, title, duration, image_url)
		self.title = title
		self.storyline = storyline
		self.poster_image_url = image_url
		self.trailer_youtube_url = video_url

	# opens a new browser tab and navigates to youtube link
	def show_trailer(self):
		webbrowser.open(self.trailer_url)