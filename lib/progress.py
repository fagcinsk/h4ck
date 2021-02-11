class Progress:
    prg = '|/-\\'
    prg_len = len(prg)

    def __init__(self, total=0):
        self.i = 0
        self.total = total
        self.val = ''
        self.update = self._progress if total else self._spin

    def _spin(self):
        self.i %= self.prg_len
        self.val = self.prg[self.i]

    def _progress(self):
        self.val = f'{int(self.i*100/self.total)}%'

    def __call__(self):
        self.i += 1
        self.update()
        print(f'\r    \r{self.val}', end='', flush=True)
        if self.total != 0 and self.total == self.i:
            self.__del__()

    def __del__(self):
        print('\r    \r', end='', flush=True)
