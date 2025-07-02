import sys 
import pygame

def run_game():
    #inicializa o jogo e cria um objeto para a tela 
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("alien Invasion")
    #define a cor de fundo
    bg_color = (230,230,230)
    
    while True:
        # observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        #Deixa a tela mais recente visivel
        pygame.display.flip()
    
run_game()