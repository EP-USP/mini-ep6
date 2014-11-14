from media import CD, DVD, MP3

class MediaFactory():

    def create(self, format, title):
        if (format == 'DVD'):
            media = DVD(title)
        elif (format == 'CD'):
            media = CD(title)
        else:
            media = MP3(title)
        return media