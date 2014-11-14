from media import CD, DVD, MP3

class MediaFactory():

    def create(self, format, title):
        if (format == 'dvd'):
            media = DVD(title)
        elif (format == 'cd'):
            media = CD(title)
        else:
            media = MP3(title)
        return media
