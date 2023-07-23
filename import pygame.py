import pygame
import sys
import glob
import random

def main():
    pygame.init()

    # Configuração da tela cheia
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Lista de caminhos para as imagens que você deseja exibir no carrossel
    image_paths = glob.glob("U:\ESPI\ESPBug-master\ESPBug-master\web_converter\img\*.png")  # Substitua pelo padrão de nome de arquivo correto
    images = [pygame.image.load(path) for path in image_paths]

    # Redimensionar as imagens para se ajustar à tela
    images = [pygame.transform.scale(image, (screen_width, screen_height)) for image in images]

    # Definir o título da janela
    pygame.display.set_caption("Carrossel de Imagens")

    # Definir o intervalo de troca de imagem (em milissegundos)
    intervalo_troca_imagem = 5000  # 5 segundos

    # Variável para controlar a troca de imagem
    tempo_ultima_troca = pygame.time.get_ticks()

    # Índice da imagem atual
    indice_imagem_atual = 0

    # Loop principal do carrossel
    while True:
   

        # Obter o tempo atual
        tempo_atual = pygame.time.get_ticks()

        # Verificar se é hora de trocar a imagem
        if tempo_atual - tempo_ultima_troca >= intervalo_troca_imagem:
            # Escolher uma imagem aleatoriamente (ou avançar para a próxima, se preferir em ordem)
            indice_imagem_atual = random.randint(0, len(images) - 1)

            # Atualizar o tempo da última troca
            tempo_ultima_troca = tempo_atual

        # Desenhar a imagem atual na tela
        screen.blit(images[indice_imagem_atual], (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()