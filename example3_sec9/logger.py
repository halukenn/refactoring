class Logger:

    STATE_STOPPED = 0
    STATE_LOGGING = 1

    def __init__(self):
        self._state = self.STATE_STOPPED

    def start(self):
        if self.STATE_STOPPED == self._state:
            print('** START LOGGING **')
            self._state = self.STATE_LOGGING
        elif self.STATE_LOGGING == self._state:
            # Do nothing
            pass
        else:
            print('Invalid state:{}'.format(self._state))

    def stop(self):
        if self.STATE_STOPPED == self._state:
            # Do nothing
            pass
        elif self.STATE_LOGGING == self._state:
            print('** STOP LOGGING **')
            self._state = self.STATE_STOPPED
        else:
            print('Invalid state:{}'.format(self._state))

    def log(self, info):
        if self.STATE_STOPPED == self._state:
            print('Ignoring:{}'.format(info))
        elif self.STATE_LOGGING == self._state:
            print('Logging:{}'.format(info))
        else:
            print('Invalid state:{}'.format(self._state))
