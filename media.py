from playstrategy import TVStrategy, RadioStrategy


class Media():
    def __init__(self):
        raise NotImplementedError('Media e uma classe abstrata \
                                    e nao deve ser instanciada!')

    def play(self):
        self.play_strategy.play(self)

    def __str__(self):
        return self.title


class DVD(Media):
    def __init__(self, title):
        self.title = title
        self.format = 'DVD'
        self.play_strategy = TVStrategy()


class CD(Media):
    def __init__(self, title):
        self.title = title
        self.format = 'CD'
        self.play_strategy = RadioStrategy()


class MP3(Media):
    def __init__(self, title):
        self.title = title
        self.format = 'MP3'
        self.play_strategy = RadioStrategy()
