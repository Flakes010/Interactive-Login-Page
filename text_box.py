import pygame
from os.path import join

pygame.init()


COLOR_INACTIVE = (109, 130, 141)
COLOR_ACTIVE = (86, 174, 208)
TEXT_COLOR = (20, 20, 20)
EMAIL_COLOR = (190, 190, 190)
UP_EMAIL_COLOR = (73, 123, 152)
FONT = pygame.font.Font(None, 26)
FONT2 = pygame.font.Font(None, 22)
FONT3 = pygame.font.Font(None, 16)
FONT4 = pygame.font.Font(None, 21)


class InputBox:

    def __init__(self, x, y, width, height, text='', email=False, password=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = COLOR_INACTIVE
        self.text = text
        self.email = email
        self.password = password
        if self.email: 
            self.email_text = "email@domain.com"
            self.up_email_text = "E-Mail"
            self.email_text_surface = FONT.render(self.email_text, True, EMAIL_COLOR)
            self.up_email_text_surface = FONT2.render(self.up_email_text, True, UP_EMAIL_COLOR)
        if self.password:
            self.password_text = "Password"
            self.show_psw_text = "Show"
            self.password_text_surface = FONT2.render(self.password_text, True, UP_EMAIL_COLOR)
            self.show_rect = pygame.Rect(self.rect.x + 1, self.rect.y + 55, 18, 18)
            self.show_text_surface = FONT4.render(self.show_psw_text, True, UP_EMAIL_COLOR)
            self.show_text_surface_rect = self.show_text_surface.get_rect()
            self.show_text_surface_rect.center = (self.rect.x + 40, self.rect.y + 70)
            self.tick = False
            self.tick_image = pygame.image.load(join("assets", "tick.png"))
            self.tick_image = pygame.transform.scale(self.tick_image, (16, 16))
        self.txt_surface = FONT.render(text, True, TEXT_COLOR)
        self.active = False
        self.lock = True
        self.hided_password = ""
        self.hided_password_surface = FONT.render(self.hided_password, True, TEXT_COLOR)

    def handle_event(self, event):        
        if event.type == pygame.MOUSEBUTTONDOWN:   
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.lock = False
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            if self.password:
                if self.show_rect.collidepoint(event.pos) or self.show_text_surface_rect.collidepoint(event.pos):
                    if self.tick: 
                        self.tick = False
                    else: 
                        self.tick = True
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    print(self.hided_password)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    if self.password != True: self.text = self.text[:-1]
                    elif self.password:
                        self.text = self.text[:-1]
                        self.hided_password = self.hided_password[:-1]
                else:
                    if self.password != True: self.text += event.unicode
                    elif self.password: 
                        self.text += "*"
                        self.hided_password += event.unicode
                self.txt_surface = FONT.render(self.text, True, TEXT_COLOR)
                self.hided_password_surface = FONT.render(self.hided_password, True, TEXT_COLOR)
                
                

    def update(self):
        width = max(200, self.txt_surface.get_width() + 20)
        self.rect.w = width

    def draw(self, screen, dx, dy):
        if self.email: screen.blit(self.txt_surface, (self.rect.x + dx, self.rect.y + dy))
        if self.password:    
            if self.tick != True: 
                screen.blit(self.txt_surface, (self.rect.x + dx, self.rect.y + dy))
            else:
                screen.blit(self.hided_password_surface, (self.rect.x + dx, self.rect.y + dy - 5))

        if self.password:
            if self.tick:
                screen.blit(self.tick_image, (self.rect.x + 2, self.rect.y + 55))
            screen.blit(self.password_text_surface, (self.rect.x + 1, self.rect.y - 20))
            screen.blit(self.show_text_surface, (self.rect.x + 23, self.rect.y + 58))
            
            pygame.draw.rect(screen, COLOR_INACTIVE, self.show_rect, 3, 3)
            
        if self.email:     
            screen.blit(self.up_email_text_surface, (self.rect.x + 1, self.rect.y - 20))
            if self.lock:
                screen.blit(self.email_text_surface, (self.rect.x + dy, self.rect.y + 15))
            else:
                self.email_text_surface = FONT3.render(self.email_text, True, UP_EMAIL_COLOR)
                screen.blit(self.email_text_surface, (self.rect.x + 13, self.rect.y + 6))
                
        pygame.draw.rect(screen, self.color, self.rect, 3, 3)