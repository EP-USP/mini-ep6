class Media():
    def __init__(self):
        raise NotImplementedError('Media e uma classe abstrata \
                                    e nao deve ser instanciada!')
    def play(self):
        pass

    def __str__(self):
        return self.title


class DVD(Media):
    def __init__(self, title):
        self.title = title
        self.format = 'DVD'

    def play(self):
        print('Playing a nice %s\'s %s'
            ' on my big TV' % (self.title, self.format))

class CD(Media):
    def __init__(self, title):
        self.title = title
        self.format = 'CD'

    def play(self):
        print('Playing a nice %s\'s %s'
            ' on my big radio' % (self.title, self.format))

class MP3(Media):
    def __init__(self, title):
        self.title = title
        self.format = 'MP3'

    def play(self):
        print('Playing a nice %s\'s %s'
            ' on my big radio' % (self.title, self.format))