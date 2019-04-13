import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理子弹"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船位置创建子弹"""
        super(Bullet, self).__init__()
        self.screen = screen
        