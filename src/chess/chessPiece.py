from pygame.sprite import Sprite
from pygame import Surface


class ChessPiece(Sprite):
    # cord (x, y)
    def __init__(self, image: Surface, cord: list[int, int]):
        """

        :param image:
        :param cord: set cords to center of the tile
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = cord[0]
        self.rect.y = cord[1]

    def draw(self, surface: Surface):
        surface.blit(self.image, [self.rect.x - self.rect.width / 2, self.rect.y - self.rect.height / 2])
