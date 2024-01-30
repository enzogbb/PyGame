import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from perguntas import perguntas

def desenhar_retangulos(window, pergunta_atual):
    cor_branca = (255, 255, 255)
    cor_preta = (0, 0, 0)

    # Tamanho dos retângulos
    largura_retangulo = 300
    altura_retangulo = 50

    # Posições dos retângulos
    pos_x = 50
    pos_y = 50

    # Desenha o retângulo da pergunta
    pygame.draw.rect(window, cor_branca, (pos_x, pos_y, largura_retangulo, altura_retangulo))

    # Adiciona o texto da pergunta no retângulo
    fonte = pygame.font.Font(None, 36)
    texto_pergunta = fonte.render(pergunta_atual['pergunta'], True, cor_preta)
    window.blit(texto_pergunta, (pos_x + 10, pos_y + 10))

    # Desenha os retângulos das alternativas
    for i, alternativa in enumerate(pergunta_atual['alternativas']):
        pos_y += altura_retangulo + 20  # Ajusta a posição vertical para a próxima alternativa
        pygame.draw.rect(window, cor_branca, (pos_x, pos_y, largura_retangulo, altura_retangulo))

        # Adiciona o texto da alternativa no retângulo
        texto_alternativa = fonte.render(alternativa, True, cor_preta)
        window.blit(texto_alternativa, (pos_x + 10, pos_y + 10))

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

        # Pergunta atual
    pergunta_atual = perguntas[0]

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca

        # Desenha os retângulos na tela com base na pergunta atual
        desenhar_retangulos(window, pergunta_atual)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
