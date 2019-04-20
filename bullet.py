import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理子弹"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船位置创建子弹"""
        super(Bullet, self).__init__()
        self.screen = screen
        # 在(0,0)创建表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
