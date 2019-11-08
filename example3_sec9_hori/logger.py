
class State:

    def start(self):
        pass

    def stop(self):
        pass

    def log(self, info):
        pass


class Logging(State):

    def start(self):
        pass

    def stop(self):
        print('** STOP LOGGING **')

    def log(self, info):
        print('Logging:{} '.format(info))


class Stopped(State):

    def start(self):
        print('** START LOGGING **')

    def stop(self):
        pass

    def log(self, info):
        print('Ignoring:{}'.format(info))


class Logger:

    def __init__(self):
        self._state = Stopped()

    def start(self):
        self._state.start()
        self._state = Logging()

    def stop(self):
        self._state.stop()
        self._state = Stopped()

    def log(self, info):
        self._state.log(info)
