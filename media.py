class Media():
    def __init__(self):
        raise NotImplementedError('Media e uma classe abstrata \
                                    e nao deve ser instanciada!')

    def play():
        self.play_strategy.play(self)


class DVD(Media):
    def __init__(self, title):
        self.title = title
        self.name = 'DVD'
        self.play_strategy = TVStrategy()


class CD(Media):
    def __init__(self, title):
        self.title = title
        self.name = 'CD'
        self.play_strategy = RadioStrategy()


class CD(Media):
    def __init__(self, title):
        self.title = title
        self.name = 'MP3'
        self.play_strategy = RadioStrategy()
