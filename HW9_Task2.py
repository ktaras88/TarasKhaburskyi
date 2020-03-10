from random import choice
class Ghost(object):
    def __init__(self):
        self.color = choice(['white', 'yellow', 'purple', 'red'])

ghost = Ghost()
print(ghost.color)