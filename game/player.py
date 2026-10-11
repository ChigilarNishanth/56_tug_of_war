import pygame

class Player:
    def __init__(self, name: str, key: int, color: tuple, side: str):
        self.name = name
        self.key = key
        self.color = color
        self.side = side

    def is_pulling(self, event: pygame.event.Event) -> bool:
        """Check if the user pressed their designated key."""
        return event.type == pygame.KEYDOWN and event.key == self.key