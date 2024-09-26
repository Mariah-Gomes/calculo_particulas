def abrir_simulacao(event):
                    def run_simulacao():
                        # Inicializa o Pygame
                        pygame.init()

                        # Configurações da tela
                        screen = pygame.display.set_mode((700, 700))
                        pygame.display.set_caption('Simulação da Partícula')

                        # Cores
                        WHITE = (255, 255, 255)
                        RED = (255, 0, 0)
                        BLACK = (0, 0, 0)
                        BLUE = (0, 0, 255)

                        # Valores para a ONDA 1
                        x_inicial1 = 200
                        x_final1 = 500
                        y_inicial1 = 520  # Limite superior para o nível n=1
                        y_final1 = 600    # Limite superior para o nível n=1
                        num_ciclos1 = 0.5 # Definir o número de ciclos (n = 1 neste caso)

                        # Calcular a amplitude e o centro da onda
                        amplitude1 = (y_final1 - y_inicial1) / 2
                        centerY1 = (y_inicial1 + y_final1) / 2

                        # Gerar a onda 1
                        onda1 = []
                        for i in range(301):
                            x1 = x_inicial1 + i * ((x_final1 - x_inicial1) / 300)
                            y1 = centerY1 + (amplitude1 * np.sin(2 * np.pi * num_ciclos1 * (i / 300)))
                            onda1.append((x1, y1))

                        # ReversoOnda1
                        onda1Reverso = []    
                        for i in range(301):
                            x1Reverso = x_inicial1 + i * ((x_final1 - x_inicial1) / 300)
                            y1Reverso = centerY1 - (amplitude1 * np.sin(2 * np.pi * num_ciclos1 * (i / 300)))
                            onda1Reverso.append((x1Reverso, y1Reverso)) 

                        # Valores para a ONDA 2
                        x_inicial2 = 200
                        x_final2 = 500
                        y_inicial2 = 520  # Limite inferior
                        y_final2 = 440    # Limite superior para o nível n=1
                        num_ciclos2 = 1 # Definir o número de ciclos (n = 1 neste caso)

                        # Calcular a amplitude e o centro da onda
                        amplitude2 = (y_final2 - y_inicial2) / 2
                        centerY2 = (y_inicial2 + y_final2) / 2

                        # Gerar a onda 2
                        onda2 = []
                        for i in range(301):
                            x2 = x_inicial2 + i * ((x_final2 - x_inicial1) / 300)
                            y2 = centerY2 + (amplitude2 * np.sin(2 * np.pi * num_ciclos2 * (i / 300)))
                            onda2.append((x2, y2))

                        # ReversoOnda2
                        onda2Reverso = []    
                        for i in range(301):
                            x2Reverso = x_inicial2 + i * ((x_final2 - x_inicial2) / 300)
                            y2Reverso = centerY2 - (amplitude2 * np.sin(2 * np.pi * num_ciclos2 * (i / 300)))
                            onda2Reverso.append((x2Reverso, y2Reverso)) 

                        # Valores para a ONDA 3
                        x_inicial3 = 200
                        x_final3 = 500
                        y_inicial3 = 360  # Limite superior para o nível n=1
                        y_final3 = 440    # Limite superior para o nível n=1
                        num_ciclos3 = 1.5 # Definir o número de ciclos (n = 1 neste caso)

                        # Calcular a amplitude e o centro da onda
                        amplitude3 = (y_final3 - y_inicial3) / 2
                        centerY3 = (y_inicial3 + y_final3) / 2

                        # Gerar a onda 3
                        onda3 = []
                        for i in range(301):
                            x3 = x_inicial3 + i * ((x_final3 - x_inicial3) / 300)
                            y3 = centerY3 + (amplitude3 * np.sin(2 * np.pi * num_ciclos3 * (i / 300)))
                            onda3.append((x3, y3))

                        # ReversoOnda3
                        onda3Reverso = []    
                        for i in range(301):
                            x3Reverso = x_inicial3 + i * ((x_final3 - x_inicial3) / 300)
                            y3Reverso = centerY3 - (amplitude3 * np.sin(2 * np.pi * num_ciclos3 * (i / 300)))
                            onda3Reverso.append((x3Reverso, y3Reverso)) 

                        # Valores para a ONDA 4
                        x_inicial4 = 200
                        x_final4 = 500
                        y_inicial4 = 360  # Limite superior para o nível n=1
                        y_final4 = 280    # Limite superior para o nível n=1
                        num_ciclos4 = 2.0 # Definir o número de ciclos (n = 1 neste caso)

                        # Calcular a amplitude e o centro da onda
                        amplitude4 = (y_final4 - y_inicial4) / 2
                        centerY4 = (y_inicial4 + y_final4) / 2

                        # Gerar a onda 4
                        onda4 = []
                        for i in range(301):
                            x4 = x_inicial4 + i * ((x_final4 - x_inicial4) / 300)
                            y4 = centerY4 + (amplitude4 * np.sin(2 * np.pi * num_ciclos4 * (i / 300)))
                            onda4.append((x4, y4))

                        # ReversoOnda4
                        onda4Reverso = []    
                        for i in range(301):
                            x4Reverso = x_inicial4 + i * ((x_final4 - x_inicial4) / 300)
                            y4Reverso = centerY4 - (amplitude4 * np.sin(2 * np.pi * num_ciclos4 * (i / 300)))
                            onda4Reverso.append((x4Reverso, y4Reverso)) 

                        # Valores para a ONDA 5
                        x_inicial5 = 200
                        x_final5 = 500
                        y_inicial5 = 280 # Limite superior para o nível n=1
                        y_final5 = 200    # Limite superior para o nível n=1
                        num_ciclos5 = 2.5 # Definir o número de ciclos (n = 1 neste caso)

                        # Calcular a amplitude e o centro da onda
                        amplitude5 = (y_final5 - y_inicial5) / 2
                        centerY5 = (y_inicial5 + y_final5) / 2

                        # Gerar a onda 5
                        onda5 = []
                        for i in range(301):
                            x5 = x_inicial5 + i * ((x_final5 - x_inicial5) / 300)
                            y5 = centerY5 + (amplitude5 * np.sin(2 * np.pi * num_ciclos5 * (i / 300)))
                            onda5.append((x5, y5))

                        # ReversoOnda5
                        onda5Reverso = []    
                        for i in range(301):
                            x5Reverso = x_inicial5 + i * ((x_final5 - x_inicial5) / 300)
                            y5Reverso = centerY5 - (amplitude5 * np.sin(2 * np.pi * num_ciclos5 * (i / 300)))
                            onda5Reverso.append((x5Reverso, y5Reverso)) 

                        # Valores alternado as ondas
                        onda_atual = 1  
                        contador = 0  
                        intervalo = 60 

                        # Desenhar Círculo
                        x_inicial = 0
                        y_inicial = 0

                        x_final = 200
                        y_final = 320

                        delta_x = x_final - x_inicial
                        delta_y = y_final - y_inicial

                        magnitude = sqrt(delta_x ** 2 + delta_y ** 2)

                        unit_x = delta_x / magnitude
                        unit_y = delta_y / magnitude

                        velocidade = 5

                        x_atual = 0
                        y_atual = 0
                        # Loop principal
                        while True:
                            for event in pygame.event.get():    
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            
                            contador += 5

                            if contador >= intervalo:
                                # Alterna entre a onda 1 (concavidade para baixo) e a reversa (concavidade para cima)
                                if onda_atual == 1:
                                    onda_atual = 2
                                else:
                                    onda_atual = 1
                                
                                # Reseta o contador
                                contador = 0

                            # Limpa a tela
                            screen.fill(WHITE)
                            
                            # Desenha na tela
                            # Estrutura do poço
                            pygame.draw.line(screen, BLACK, (200, 150), (200, 600), 5)
                            pygame.draw.line(screen, BLACK, (500, 150), (500, 600), 5)
                            pygame.draw.line(screen, BLACK, (200, 600), (500, 600), 5)
                            pygame.draw.polygon(screen, BLACK, [(180, 150), (220,150), (200, 130)])
                            pygame.draw.polygon(screen, BLACK, [(480,150), (520,150), (500, 130)])

                            # Letras
                            fonte = pygame.font.SysFont("Monospace", 30, True, False)
                            mensagem = '0'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (190, 610))
                            
                            fonte = pygame.font.SysFont("Monospace", 30, True, False)
                            mensagem = 'L'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (490, 610)) 

                            # Escrita de níveis
                            # Nível 1
                            fonte = pygame.font.SysFont("Monospace", 25, True, False)
                            mensagem = 'n = 1'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (530, 545))
                            
                            # Nível 2
                            fonte = pygame.font.SysFont("Monospace", 25, True, False)
                            mensagem = 'n = 2'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (530, 465)) 

                            # Nível 3
                            fonte = pygame.font.SysFont("Monospace", 25, True, False)
                            mensagem = 'n = 3'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (530, 385))
                            
                            # Nível 4
                            fonte = pygame.font.SysFont("Monospace", 25, True, False)
                            mensagem = 'n = 4'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (530, 305))
                            
                            # Nível 5
                            fonte = pygame.font.SysFont("Monospace", 25, True, False)
                            mensagem = 'n = 5'
                            formatacao_texto = fonte.render(mensagem, True, BLACK)   
                            screen.blit(formatacao_texto, (530, 225))

                            # Divisão de níveis
                            pygame.draw.line(screen, BLACK, (200, 520), (500, 520), 1)
                            pygame.draw.line(screen, BLACK, (200, 440), (500, 440), 1)
                            pygame.draw.line(screen, BLACK, (200, 360), (500, 360), 1)
                            pygame.draw.line(screen, BLACK, (200, 280), (500, 280), 1)
                            pygame.draw.line(screen, BLACK, (200, 200), (500, 200), 1)
                                
                            # Desenhando as ondas de níveis
                            
                            # Onda 1 e sua reversa, com base na variável onda_atual
                            if onda_atual == 1:
                                # Exibir a onda normal (concavidade para baixo)
                                for (x1, y1) in onda1:
                                    pygame.draw.circle(screen, RED, (int(x1), int(y1)), 1)
                            else:
                                # Exibir a onda reversa (concavidade para cima)
                                for (x1Reverso, y1Reverso) in onda1Reverso:
                                    pygame.draw.circle(screen, RED, (int(x1Reverso), int(y1Reverso)), 1)

                            # Onda 2 e sua reversa, com base na variável onda_atual
                            if onda_atual == 1:
                                for (x2, y2) in onda2:
                                    pygame.draw.circle(screen, RED, (int(x2), int(y2)), 1)
                            else:
                                for (x2Reverso, y2Reverso) in onda2Reverso:
                                    pygame.draw.circle(screen, RED, (int(x2Reverso), int(y2Reverso)), 1)
                            
                            # Onda 3 e sua reversa, com base na variável onda_atual
                            if onda_atual == 1:
                                for (x3, y3) in onda3:
                                    pygame.draw.circle(screen, RED, (int(x3), int(y3)), 1)
                            else:
                                for (x3Reverso, y3Reverso) in onda3Reverso:
                                    pygame.draw.circle(screen, RED, (int(x3Reverso), int(y3Reverso)), 1)

                            # Onda 4 e sua reversa, com base na variável onda_atual
                            if onda_atual == 1:
                                for (x4, y4) in onda4:
                                    pygame.draw.circle(screen, RED, (int(x4), int(y4)), 1)
                            else:
                                for (x4Reverso, y4Reverso) in onda4Reverso:
                                    pygame.draw.circle(screen, RED, (int(x4Reverso), int(y4Reverso)), 1)

                            # Onda 5 e sua reversa, com base na variável onda_atual
                            if onda_atual == 1:
                                for (x5, y5) in onda5:
                                    pygame.draw.circle(screen, RED, (int(x5), int(y5)), 1)
                            else:
                                for (x5Reverso, y5Reverso) in onda5Reverso:
                                    pygame.draw.circle(screen, RED, (int(x5Reverso), int(y5Reverso)), 1)

                            x_atual += unit_x * velocidade
                            y_atual += unit_y * velocidade

                            # Parte 6: Verifique se o ponto final foi alcançado
                            if abs(x_atual - x_final) < velocidade and abs(y_atual - y_final) < velocidade:
                                x_atual = x_final
                                y_atual = y_final
                                # Se desejar, pare o loop ou mude a lógica após alcançar o ponto final
                                # running = False

                            # Parte 7: Desenhe o círculo na nova posição
                            
                            pygame.draw.circle(screen, BLUE, (int(x_atual), int(y_atual)), 10)
                            
                            # Atualizar a exibição
                            pygame.display.flip()
                            
                            # Controlar a taxa de frames (60 FPS)
                            pygame.time.Clock().tick(60)
                        # Execute a simulação em uma nova thread
                    simulacao_thread = threading.Thread(target=run_simulacao)
                    simulacao_thread.start()