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
        print ('Playing a nice ' + instance.title + '\'s ' +
            instance.name + ' on my big TV')


class RadioStrategy(PlayStrategy):
    def __init__(self):
        pass

    def play(self, instance):
        print ('Playing a nice ' + instance.title + '\'s ' +
            instance.name + ' on my big Radio')

