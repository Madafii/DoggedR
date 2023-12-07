from pygame.sprite import Sprite
from pygame import Surface


class ChessPiece(Sprite):
    def __init__(self, image: Surface):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

