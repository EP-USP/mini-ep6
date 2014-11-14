class Media():
    def __init__(self):
        raise NotImplementedError('Media e uma classe abstrata \
                                    e nao deve ser instanciada!')

    def __str__(self):
        return self.title


class DVD(Media):
    def __init__(self, title):
        self.title = title
        self.name = 'DVD'

    def play(self):
        print ('Playing a nice ' + instance.title + '\'s ' +
            ' DVD at my big TV')


class CD(Media):
    def __init__(self, title):
        self.title = title
        self.name = 'CD'

    def play(self):
        print ('Playing a nice ' + instance.title + '\'s ' +
            ' CD at my big Radio')


class MP3(Media):
    def __init__(self, title):
        self.title = title
        self.name = 'MP3'

    print ('Playing a nice ' + instance.title + '\'s ' +
            ' MP3 at my big Radio')
