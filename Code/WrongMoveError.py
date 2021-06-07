class WrongMoveError(Exception):
    def __str__(self):
        return "No space left"
