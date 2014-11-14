class PlayStrategy():
    def __init__(self):
        raise NotImplementedError('PlayStrategy e uma classe abstrata \
                                    e nao deve ser instanciada!')

    def play(self, instance):
        pass


class TVStrategy(Media):
    def play(self, instance):
        print ('Playing a nice ' + instance.title + '\'s ' +
            instance.name + 'at my big TV')


class RadioStrategy(Media):
    def play(self, instance):
        print ('Playing a nice ' + instance.title + '\'s ' +
            instance.name + 'at my big TV')

