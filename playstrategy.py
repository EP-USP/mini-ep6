class PlayStrategy():
    def __init__(self):
        raise NotImplementedError('PlayStrategy e uma classe abstrata \
                                    e nao deve ser instanciada!')

    def play(self, instance):
        pass


class TVStrategy(PlayStrategy):
    def play(self, instance):
        print ('Playing a nice ' + instance.title + '\'s ' +
            instance.name + 'at my big TV')


class RadioStrategy(PlayStrategy):
    def play(self, instance):
        print ('Playing a nice ' + instance.title + '\'s ' +
            instance.name + 'at my big TV')

