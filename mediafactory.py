class MediaFactory():

	def create(self, format, title):
		if (format == 'dvd'):
			media = dvd(title)
		elif (format == 'cd'):
			media = cd(title)
		else (format == 'mp3'):
			media = mp3(title)
		return media