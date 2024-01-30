import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from perguntas import perguntas

def colisao_ponto_retangulo(x_ponto, y_ponto, x_retangulo, y_retangulo, largura_retangulo, altura_retangulo):
    
    # Calcula as coordenadas do canto inferior direito do retângulo
    x_retangulo_direito = x_retangulo + largura_retangulo
    y_retangulo_inferior = y_retangulo + altura_retangulo
    
    # Verifica se o ponto está dentro do retângulo
    if x_ponto >= x_retangulo and x_ponto <= x_retangulo_direito and y_ponto >= y_retangulo and y_ponto <= y_retangulo_inferior:
        return True
    else:
        return False

def desenhar_retangulos(window, pergunta_atual):
    cor_branca = (255, 255, 255)
    cor_preta = (0, 0, 0)

    # Ajuste da largura dos retângulos
    largura_retangulo = 1000
    altura_retangulo = 50

    # Posições iniciais dos retângulos
    pos_x = (WIDTH - largura_retangulo) // 2
    pos_y = (HEIGHT - (altura_retangulo + 20) * (len(pergunta_atual['alternativas']) + 1)) // 2

    # Desenha o primeiro retângulo esticado na parte superior centralizada
    pygame.draw.rect(window, cor_branca, (pos_x, 0, largura_retangulo, altura_retangulo * 3))

    # Adiciona o texto da pergunta no retângulo
    fonte = pygame.font.Font(None, 36)
    texto_pergunta = fonte.render(pergunta_atual['enunciado'], True, cor_preta)
    text_rect = texto_pergunta.get_rect(center=(pos_x + largura_retangulo // 2, altura_retangulo * 1.5))
    window.blit(texto_pergunta, text_rect)

    # Ajusta a posição vertical para as alternativas
    pos_y += altura_retangulo + 20  

    # Desenha os retângulos das alternativas
    for i, alternativa in enumerate(pergunta_atual['alternativas']):
        pygame.draw.rect(window, cor_branca, (pos_x, pos_y, largura_retangulo, altura_retangulo))

        # Adiciona o texto da alternativa no retângulo
        texto_alternativa = fonte.render(alternativa, True, cor_preta)
        text_rect = texto_alternativa.get_rect(center=(pos_x + largura_retangulo // 2, pos_y + altura_retangulo // 2))
        window.blit(texto_alternativa, text_rect)

        # Ajusta a posição vertical para a próxima alternativa
        pos_y += altura_retangulo + 20  

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    pergunta_atual_index = 0
    pergunta_atual = perguntas[pergunta_atual_index]

    # Pergunta atual
    count = 0
    pergunta_atual = perguntas[count]

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_click, y_click = pygame.mouse.get_pos()

                for i, alternativa in enumerate(pergunta_atual['alternativas']):
                    pos_x = (WIDTH - 500) // 2  # Largura atualizada dos retângulos
                    pos_y = (HEIGHT - (50 + 20) * (len(pergunta_atual['alternativas']) + 1)) // 2 + (50 + 20) * i
                    if colisao_ponto_retangulo(x_click, y_click, pos_x, pos_y, 500, 50):
                        print (i)
                        # Verifica se a resposta está correta
                        # if i == pergunta_atual['correta']:
                        #     # Resposta correta, avança para a próxima pergunta
                        #     pergunta_atual_index += 1
                        #     if pergunta_atual_index < len(perguntas):
                        #         pergunta_atual = perguntas[pergunta_atual_index]
                            
                        #     else:
                        #         # O jogador respondeu todas as perguntas corretamente, encerra o jogo
                        #         count +=1
                        #         pergunta_atual = perguntas[count]
                        
                        # else:
                        #     # Resposta incorreta, encerra o jogo
                        #     state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca

        # Desenha os retângulos na tela com base na pergunta atual
        desenhar_retangulos(window, pergunta_atual)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
