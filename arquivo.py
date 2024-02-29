import sys
import pygame
import random

pygame.init()

#Configuração de tela
Largura = 800
Altura = 600

tela = pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption("Pygame")

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
ROSA = (255,0,255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None,tamanho_fonte)

texto = fonte.render("Isa", True, BRANCO)
texto_rect = texto.get_rect(center=(Largura/2, Altura/2)) #Centro
#texto_rect = texto.get_rect(center=(Largura/2, 25 )) #Top
#texto_rect = texto.get_rect()
#texto_rect.left = 400
#texto_rect.top = 300
#texto_rect.right = 700
clock = pygame.time.Clock() #relogio para controlar velocidade

#velocidade_x = 1
#velocidade_y = 1

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint (-1, 1)

while velocidade_x == 0: 
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint (-1, 1)

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    texto_rect.x += velocidade_x  
    texto_rect.y += velocidade_y 
    
    if texto_rect.right >= Largura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("Isa", True, VERMELHO)    
    if texto_rect.left <=1:
         velocidade_x = random.randint(-1, 1)
         velocidade_y = random.randint(-1, 1)
         texto = fonte.render("Isa", True, VERMELHO)
    if texto_rect.top >= Altura:
        velocidade_y = random.randint (-1, 1)
        velocidade_x = random.randint (-1, 1)
        #velocidade_y = -velocidade_y
        texto = fonte.render("ISA", True, ROSA)   
    if texto_rect.bottom <=1:
        velocidade_y = random.randint (-1, 1)
        velocidade_x = random.randint (-1, 1)
        #velocidade_y = -velocidade_y   
        texto = fonte.render("ISA", True, ROSA)
        
        
    clock.tick(150)        
    tela.fill(PRETO)
    tela.blit(texto,texto_rect)
    pygame.display.flip()








