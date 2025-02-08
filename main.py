import pygame

# inicializar
pygame.init()
tamanho_tela = (400, 400)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Meu primeiro Jogo Python')

# configuraçãp do jogo
tamanho_bola = 20
bola = pygame.Rect(100, 200, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(100, 300, tamanho_jogador, 15)

# outras variáveis
fim_jogo = False
movimento_bola = [7, -7]


cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}


# Desenhar os elementos na tela
def desenhar_inicio_jogo():
    tela.fill(cores["branca"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["verde"], bola)


def movimentobola(bola):
    bola.x += movimento_bola[0]
    bola.y += movimento_bola[1]

    if bola.x <= 0:
        movimento_bola[0] = - movimento_bola[0]
    if bola.x >= tamanho_tela[0] - tamanho_bola:
        movimento_bola[0] = - movimento_bola[0]
    if bola.y <= 0:
        movimento_bola[1] = - movimento_bola[1]
    if bola.y >= tamanho_tela[1] - tamanho_bola:
        movimento_bola[1] = - movimento_bola[1]

    if jogador.collidepoint(bola.x, bola.y):
        movimento_bola[1] = - movimento_bola[1]


def movimento_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT and jogador.x > 0:
            jogador.x -= 100
        if evento.key == pygame.K_RIGHT and (jogador.x + tamanho_jogador) < 400:
            jogador.x += 100


while not fim_jogo:
    desenhar_inicio_jogo()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
        movimento_jogador(evento)
    movimentobola(bola)
    pygame.time.wait(20)
    pygame.display.update()

pygame.quit()
