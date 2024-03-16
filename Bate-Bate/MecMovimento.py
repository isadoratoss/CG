import pygame
import random


class MovendoTexto:
    def __init__(self, texto, fonte_tamanho, largura, altura):
        self.fonte = pygame.font.SysFont(None, fonte_tamanho) #Determinar o tamanho da fonte do texto
        self.texto = texto #Determinar o texto em tela
        self.largura = largura #Definir largura da janela
        self.altura = altura #Definir altura da janela
        self.texto_surf = self.fonte.render(texto, True, (255, 255, 255)) #Renderiza a exibição do texto
        self.rect = self.texto_surf.get_rect(center=(largura / 2, altura / 2)) #Estabelece um retangulo para determinar o ponto da renderização no centro 

        self.velocidade_x = self.gerar_numero_nao_zero() #Determina a velocidade do texto na direção x
        self.velocidade_y = self.gerar_numero_nao_zero() #Determina a velocidade do texto na direção y

    def gerar_numero_nao_zero(self): #Sorteio entre os número -1 e 1
        numero = 0
        while numero == 0:
            numero = random.randint(-1, 1)
        return numero

    def move(self): #Move o texto na direção X e Y
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

#Sorteia um número para que o texto não ultrapasse as margens da janela na direita, esquerda, topo e bordas inferiores:

        if self.rect.left <= 0: 
            self.velocidade_x = random.randint(0, 1)  
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.right >= self.largura:
            self.velocidade_x = random.randint(-1, 0)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.top <= 0:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(0, 1)
            self.change_color()

        if self.rect.bottom >= self.altura:
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self): #Sortear a cor do texto todas as vezes que ele encostas nas bordas da janela
        cor_texto = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto) #Renderização da cor do texto
