from mediafactory import MediaFactory

class MediaCenter():

    def __init__(self):
        self.media_list = []

    def list_media(self):
        for m in media_list:
            print(m)

    def play_media(self, title):
        for m in media_list:
            if (m.title == 'title'):
                m.play()

    def add_media(self, format, title):
        f = MediaFactory()
        media = f.create(format, title)
        media_list.append(media)

    def remove_media(self, title):
        media_list.remove(title)

