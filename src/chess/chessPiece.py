from pygame.sprite import Sprite
from pygame import Surface


class ChessPiece(Sprite):
    # cord (x, y)
    def __init__(self, image: Surface, cord: list[int, int]):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = cord[0]
        self.rect.y = cord[1]

    def update(self):
        pass
