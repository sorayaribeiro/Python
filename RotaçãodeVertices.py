import glfw
from OpenGL.GL import *
import numpy as np
import time


def desenho_quadrado():
    giro = 0
    #cria a variavel giro com o valor 0
    glfw.init()
    # iniciar glfw
    window = glfw.create_window(800, 600, "", None, None)
    # Criar Janela com 800 de largura por 600 de altura
    glfw.set_window_pos(window, 400, 50)
    #define a posição na tela onde a imagerm irá aparecer
    glfw.make_context_current(window)
    vertices = [-0.5, 0.5, 0.0,
                0.5, 0.5, 0.0,
                0.5, -0.5, 0.0,
                -0.5, -0.5, 0.0]
    v = np.array(vertices, dtype=np.float32)
    # Uma constante para a matriz que queremos habilitar
    glEnableClientState(GL_VERTEX_ARRAY)
    # define uma matriz de dados de vértice
    glVertexPointer(3, GL_FLOAT, 0, v)
    # limpa os buffers de cor
    glClearColor(0, 0, 0, 0)
    #define as cores da forma

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        # define primitivos a serem renderizados
        glDrawArrays(GL_QUADS, 0, 4)
        #renderiza o vetor em quads
        glfw.swap_buffers(window)
        if (giro == 0) :
            time.sleep(3)
            #aguarda 3 segundos
            glRotate(30.0, 30.0, 30.0, 30.0);
            #gira cada vertice 30 graus no sentido anti horario
            giro = 1
            #poe o giro como 1 para que ele não se repita uma segunda vez
    glfw.terminate()
    #termina o glfw


if __name__ == '__main__':
    desenho_quadrado()
    #chama a função

