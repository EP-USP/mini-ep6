class PlayStrategy():
    def __init__(self):
        raise NotImplementedError('PlayStrategy e uma classe abstrata \
                                    e nao deve ser instanciada!')

    def play(self, instance):
        pass


class TVStrategy(PlayStrategy):
    def __init__(self):
        pass

    def play(self, instance):
        print('Playing a nice %s\'s %s on \
            my big TV', instance.title, instance.format)


class RadioStrategy(PlayStrategy):
    def __init__(self):
        pass

    def play(self, instance):
        print('Playing a nice %s\'s %s on \
            my big radio', instance.title, instance.format)

