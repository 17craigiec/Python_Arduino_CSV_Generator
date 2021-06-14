import time

class Timer:

    t0 = 0

    def reset(self):
        self.t0 = time.time()

    def getCurrentTime(self):
        return time.time() - self.t0

    def __init__(self):
        self.reset()
