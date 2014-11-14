from mediacenter import MediaCenter
import sys

mc = MediaCenter()
while (True):
    entry = input('Care to add new media to center? (y/n): ')
    if (entry == 'n'):
        title = input('Which title do I play?: ')
        mc.play_media(title)
    elif (entry == 'y'):
        format = input('Tell me the format of your media: ')
        title = input('Tell me the title of your media: ')
        mc.add_media(format, title)
    else:
        sys.exit()