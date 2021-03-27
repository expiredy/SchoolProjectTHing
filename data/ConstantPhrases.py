import random


class list(list):
    def __repr__(self, *args, **kwargs):
        return random.choice(self)

ChatTitle = 'Chat'
MotivationPhrase = list(["HaHa Let's go", "U can do it"])