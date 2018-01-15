class Hello:
    def __init__(self):
        self.mode = ''
        self.lang = {
            'jp': 'こんにちは',
            'en': 'hello'
        }

    def japanese(self):
        self.mode = 'jp'
        return self

    def english(self):
        self.mode = 'en'
        return self

    def say(self):
        return self.lang[self.mode]


obj = Hello()
print(obj.japanese().say())
print(obj.english().say())