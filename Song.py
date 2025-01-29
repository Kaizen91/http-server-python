class Song():
    def __init__(self):
        self.lyrics = """Heeey HeeeEEEEyyyyy Baaaby!
            Ooooooooh! Aaaaaaah!
            I want to knoOOOooOOO will you be my girl?"""
        self.lines = self._gen_lines()

    def _gen_lines(self):
        for line in self.lyrics.split('\n'):
            yield line

    def next_line(self):
        try:
            return next(self.lines)
        except StopIteration:
            self.lines = self._gen_lines()
            return next(self.lines)
