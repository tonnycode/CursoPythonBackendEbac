
import random
import pygame

LARGURA, ALTURA = 480, 640
FPS = 60
GRAVIDADE = 0.42
FORCA_PULO = -7.6
LARGURA_CANO = 76
ESPACO_CANOS = 170
VELOCIDADE_CANO = 3

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird em Python")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 32, bold=True)

passaro_x = 110
passaro_y = ALTURA // 2
velocidade_passaro = 0
canos = []
pontuacao = 0
fim_do_jogo = False


def novo_cano():
    altura_cima = random.randint(90, ALTURA - ESPACO_CANOS - 120)

    return {
        "x": LARGURA + 40,
        "topo": altura_cima,
        "pontuou": False
    }


def reiniciar_jogo():
    global passaro_y, velocidade_passaro, canos, pontuacao, fim_do_jogo

    passaro_y = ALTURA // 2
    velocidade_passaro = 0
    canos = [novo_cano()]
    pontuacao = 0
    fim_do_jogo = False


def pular():
    global velocidade_passaro
    velocidade_passaro = FORCA_PULO


def desenhar_passaro():
    pygame.draw.circle(tela, (255, 225, 80), (passaro_x, int(passaro_y)), 22)
    pygame.draw.circle(tela, (255, 255, 255), (passaro_x + 8, int(passaro_y) - 8), 4)
    pygame.draw.circle(tela, (20, 20, 20), (passaro_x + 10, int(passaro_y) - 8), 2)


def desenhar_cano():
    for cano in canos:
        x = int(cano["x"])

        cano_cima = pygame.Rect(x, 0, LARGURA_CANO, cano["topo"])

        inicio_baixo = cano["topo"] + ESPACO_CANOS

        cano_baixo = pygame.Rect(
            x, inicio_baixo, LARGURA_CANO, ALTURA - inicio_baixo
        )

        pygame.draw.rect(tela, (78, 201, 99), cano_cima)
        pygame.draw.rect(tela, (78, 201, 99), cano_baixo)


def mover_canos():
    global pontuacao

    if not canos or canos[-1]["x"] < LARGURA - 220:
        canos.append(novo_cano())

    for cano in canos:
        cano["x"] -= VELOCIDADE_CANO

        if not cano["pontuou"] and cano["x"] + LARGURA_CANO < passaro_x:
            cano["pontuou"] = True
            pontuacao += 1

    while canos and canos[0]["x"] < -LARGURA_CANO:
        canos.pop(0)


def bateu():
    retangulo_passaro = pygame.Rect(
        passaro_x - 18, int(passaro_y) - 18, 36, 36
    )

    for cano in canos:
        x = int(cano["x"])

        cano_cima = pygame.Rect(x, 0, LARGURA_CANO, cano["topo"])

        inicio_baixo = cano["topo"] + ESPACO_CANOS

        cano_baixo = pygame.Rect(
            x, inicio_baixo, LARGURA_CANO, ALTURA - inicio_baixo
        )

        if retangulo_passaro.colliderect(cano_cima) or retangulo_passaro.colliderect(cano_baixo):
            return True

    return passaro_y < 0 or passaro_y > ALTURA


def desenhar_interface():
    texto_pontos = fonte.render(str(pontuacao), True, (255, 255, 255))

    tela.blit(
        texto_pontos,
        (LARGURA // 2 - texto_pontos.get_width() // 2, 28)
    )

    if fim_do_jogo:
        mensagem = fonte.render("Espaco para reiniciar", True, (255, 255, 255))

        tela.blit(
            mensagem,
            (LARGURA // 2 - mensagem.get_width() // 2, ALTURA // 2)
        )


reiniciar_jogo()

rodando = True

while rodando:

    relogio.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:

            if fim_do_jogo:
                reiniciar_jogo()
            else:
                pular()

    if not fim_do_jogo:

        velocidade_passaro += GRAVIDADE
        passaro_y += velocidade_passaro

        mover_canos()

        if bateu():
            fim_do_jogo = True

    tela.fill((18, 28, 45))

    desenhar_cano()
    desenhar_passaro()
    desenhar_interface()

    pygame.display.flip()

pygame.quit()