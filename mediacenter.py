from mediafactory import MediaFactory

class MediaCenter():

    def __init__(self):
        self.media_list = []

    def list_media(self):
        for m in self.media_list:
            print(m)

    def play_media(self, title):
        for m in self.media_list:
            if (m.title == title):
                m.play()

    def add_media(self, format, title):
        f = MediaFactory()
        media = f.create(format, title)
        self.media_list.append(media)

    def remove_media(self, title):
        self.media_list.remove(title)