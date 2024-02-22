import sys
import pygame

pygame.init()

#Configuração de tela
Largura = 800
Altura = 600

tela = pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption("Pygame")

PRETO = (0,0,0)
BRANCO = (255,255,255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None,tamanho_fonte)

texto = fonte.render("Isa", True, BRANCO)
#texto_rect = texto.get_rect(center=(Largura/2, Altura/2)) #Centro
#texto_rect = texto.get_rect(center=(Largura/2, 25 )) #Top
texto_rect = texto.get_rect(center=(750,550))

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    tela.fill(PRETO)
    tela.blit(texto,texto_rect)
    pygame.display.flip()








