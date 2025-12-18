import pygame
import sys
from levels import Level
from tiles import WHITE, RED, BLACK

WIDTH = 1280
HEIGHT = 720
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dungeon Crawler")

        self.clock = pygame.time.Clock()
        self.level = Level()
        self.level.create_map()
        
        self.font = pygame.font.SysFont('arial', 24, bold=True)

    def draw_ui(self):
        bar_width = 200
        bar_height = 20
        ratio = self.level.player.health / self.level.player.max_health
        fill = ratio * bar_width
        
        border_rect = pygame.Rect(10, 10, bar_width, bar_height)
        fill_rect = pygame.Rect(10, 10, fill, bar_height)
        
        pygame.draw.rect(self.screen, (60, 60, 60), border_rect)
        pygame.draw.rect(self.screen, RED, fill_rect)
        pygame.draw.rect(self.screen, WHITE, border_rect, 2)

        hp_text = self.font.render(f"HP: {int(self.level.player.health)}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level.level_count}", True, WHITE)
        dmg_text = self.font.render(f"Dmg: {self.level.player.damage}", True, WHITE)
        
        self.screen.blit(hp_text, (15, 35))
        self.screen.blit(level_text, (15, 65))
        self.screen.blit(dmg_text, (15, 95))
        
        hint = self.font.render("WASD: Move | SPACE: Attack | ESC: Quit", True, (150, 150, 150))
        self.screen.blit(hint, (self.screen.get_width() - 450, 10))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill(BLACK)
            
            if self.level.player.health > 0:
                self.level.run()
                self.draw_ui()
            else:
                msg = self.font.render("GAME OVER - Press ESC to Quit", True, RED)
                rect = msg.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
                self.screen.blit(msg, rect)

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()