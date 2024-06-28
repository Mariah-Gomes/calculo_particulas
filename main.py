from tkinter import *
from tkinter import messagebox
from math import *
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

janela = None


def entradas_tema1_eletron():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("PPU (elétrons)")
  janela.geometry("400x400")

  rotulo_largura_caixa = Label(janela, text="Largura da caixa (L):")
  rotulo_n_inicial_particula = Label(janela,
                                     text="n inicial da partícula(ni):")
  rotulo_n_final_particula = Label(janela, text="n final da partícula(nf):")
  rotulo_calcular = Label(janela, text="Calcular:")
  rotulo_voltar = Label(janela, text="Voltar para a página anterior:")

  entrada_largura_caixa = Entry(janela)
  entrada_n_inicial_particula = Entry(janela)
  entrada_n_final_particula = Entry(janela)

  def clique():
    resposta_largura_caixa = entrada_largura_caixa.get()
    resposta_largura_caixa = float(resposta_largura_caixa)
    resposta_n_inicial_particula = entrada_n_inicial_particula.get()
    resposta_n_inicial_particula = float(resposta_n_inicial_particula)
    resposta_n_final_particula = entrada_n_final_particula.get()
    resposta_n_final_particula = float(resposta_n_final_particula)

    # Constantes
    h = 6.626E-34

    # Massa do eletrón
    m = 9.11E-31

    # Cálculos para a fórmula de onda
    a = 2 / resposta_largura_caixa
    a = sqrt(a)
    k_funcao_onda_n_inicial = (resposta_n_inicial_particula *
                               pi) / resposta_largura_caixa
    k_funcao_onda_n_final = (resposta_n_final_particula *
                             pi) / resposta_largura_caixa

    # Cálculos para o cálculo de energia
    energia_inicial_j = ((resposta_n_inicial_particula**2) *
                         (h**2)) / (8 * m * (resposta_largura_caixa**2))
    energia_final_j = ((resposta_n_final_particula**2) *
                       (h**2)) / (8 * m * (resposta_largura_caixa**2))
    energia_inicial_ev = energia_inicial_j / 1.602E-19
    energia_final_ev = energia_final_j / 1.602E-19

    # Cálculos para o fóton
    energia_foton_ev = energia_final_ev - energia_inicial_ev
    energia_foton_j = energia_final_j - energia_inicial_j

    # Cálculos para o comprimento de onda do fóton
    comprimento_de_onda_foton = (4.136E-15 * 3E8) / energia_foton_ev

    # Cálculos para a frequência do fóton
    frequencia_foton = energia_foton_ev / 4.136E-15

    # Cálculos para a velocidade
    velocidade_inicial = (2 * energia_inicial_j) / m
    velocidade_inicial = sqrt(velocidade_inicial)

    velocidade_final = (2 * energia_final_j) / m
    velocidade_final = sqrt(velocidade_final)

    # Comprimento de onda
    comprimento_de_onda_inicial = (
        2 * resposta_largura_caixa) / resposta_n_inicial_particula
    comprimento_de_onda_final = (
        2 * resposta_largura_caixa) / resposta_n_final_particula

    global janela

    if janela:
      janela.destroy()

    janela = Tk()
    janela.title("PPU (saídas)")
    janela.geometry("400x400")

    rotulo_funcao_onda_quantica_si_dois_niveis = Label(
        janela, text="Função de onda quântica no SI dos dois níveis")
    rotulo_nivel_inicial = Label(janela, text="Nível inicial:")
    rotulo_resposta_nivel_inicial = Label(
        janela,
        text=
        f"ψ2(x)={format(a, '.3E')}sin({format(k_funcao_onda_n_inicial, '.3E')}*x)",
        fg='green')
    rotulo_nivel_final = Label(janela, text="Nível final:")
    rotulo_resposta_nivel_final = Label(
        janela,
        text=
        f"ψ2(x)={format(a, '.3E')}sin({format(k_funcao_onda_n_final, '.3E')}*x)",
        fg='green')
    rotulo_proxima_pagina = Label(janela, text="Próxima página:")

    def clique2():
      global janela

      if janela:
        janela.destroy()

      janela = Tk()
      janela.title("PPU (saídas)")
      janela.geometry("400x400")

      rotulo_energia_nivel_quantico_inicial_e_final = Label(
          janela, text="Energia do nível quântico inicial (Ei) e final (Ef): ")
      rotulo_Ei_eV = Label(janela, text="Ei (eV):")
      rotulo_resposta_Ei_eV = Label(janela,
                                    text=format(energia_inicial_ev, '.3E'),
                                    fg='green')
      rotulo_Ef_eV = Label(janela, text="Ef (eV):")
      rotulo_resposta_Ef_eV = Label(janela,
                                    text=format(energia_final_ev, '.3E'),
                                    fg='green')
      rotulo_Ei_J = Label(janela, text="Ei (J):")
      rotulo_resposta_Ei_J = Label(janela,
                                   text=format(energia_inicial_j, '.3E'),
                                   fg='green')
      rotulo_Ef_J = Label(janela, text="Ef (J):")
      rotulo_resposta_Ef_J = Label(janela,
                                   text=format(energia_final_j, '.3E'),
                                   fg='green')
      rotulo_proxima_pagina = Label(janela, text="Próxima página:")

      def clique3():
        global janela

        if janela:
          janela.destroy()

        janela = Tk()
        janela.title("PPU (saídas)")
        janela.geometry("400x400")

        rotulo_foton_absorvido_emitido_transicao_niveis = Label(
            janela,
            text=
            "Fóton absorvido ou emitido pela partícula na transição entre os níveis",
            font=("Arial", 8))
        rotulo_energia = Label(janela, text="Energia (𝐸𝑓ó𝑡𝑜𝑛):")
        rotulo_resposta_energia = Label(janela,
                                        text=format(energia_foton_ev, '.3E'),
                                        fg='green')
        rotulo_frequencia = Label(janela, text="Frequência (𝑓):")
        rotulo_resposta_frequencia = Label(janela,
                                           text=format(frequencia_foton,
                                                       '.3E'),
                                           fg='green')
        rotulo_comprimento_onda = Label(janela,
                                        text="Comprimento de onda (λ):")
        rotulo_resposta_comprimento_onda = Label(janela,
                                                 text=format(
                                                     comprimento_de_onda_foton,
                                                     '.3E'),
                                                 fg='green')
        rotulo_proxima_pagina = Label(janela, text="Próxima página:")

        def clique4():
          global janela

          if janela:
            janela.destroy()

          janela = Tk()
          janela.title("PPU (saídas)")
          janela.geometry("400x400")

          rotulo_velocidade_particula_nivel_quantico_inicial_final = Label(
              janela,
              text=
              "Velocidade (𝑣) da partícula no nível quântico inicial e final")
          rotulo_velocidade_inicial = Label(janela, text="Velocidade inicial:")
          rotulo_resposta_velocidade_inicial = Label(janela,
                                                     text=format(
                                                         velocidade_inicial,
                                                         '.3E'),
                                                     fg='green')
          rotulo_velocidade_final = Label(janela, text="Velocidade final:")
          rotulo_resposta_velocidade_final = Label(janela,
                                                   text=format(
                                                       velocidade_final,
                                                       '.3E'),
                                                   fg='green')
          rotulo_proxima_pagina = Label(janela, text="Próxima página:")

          def clique5():
            global janela

            if janela:
              janela.destroy()

            janela = Tk()
            janela.title("PPU (saídas)")
            janela.geometry("400x400")

            rotulo_comprimento_onda_DeBroglie = Label(
                janela, text="Comprimento de onda de De Broglie (λn)")
            rotulo_particula_nivel_quantico_inicial = Label(
                janela, text="Partícula nível quântico inicial:")
            rotulo_resposta_particula_nivel_quantico_inicial = Label(
                janela,
                text=format(comprimento_de_onda_inicial, '.3E'),
                fg='green')
            rotulo_particula_nivel_quantico_final = Label(
                janela, text="Partícula nível quântico final:")
            rotulo_resposta_particula_nivel_quantico_final = Label(
                janela,
                text=format(comprimento_de_onda_final, '.3E'),
                fg='green')
            rotulo_proxima_pagina = Label(janela, text="Próxima página:")

            def clique6():
              global janela

              if janela:
                janela.destroy()

              janela = Tk()
              janela.title("PPU (probabilidade)")
              janela.geometry("400x400")

              rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final = Label(
                  janela,
                  text=
                  "Probabilidade (𝑃(𝑎≤𝑥≤𝑏)) de encontrar a partícula no nível inicial e final",
                  font=("Arial", 8))
              rotulo_particula_em_a = Label(janela, text="a:")
              entrada_a = Entry(janela)
              rotulo_particula_em_b = Label(janela, text="b:")
              entrada_b = Entry(janela)
              rotulo_calcular = Label(janela, text="Calcular:")

              def clique7():
                resposta_entrada_a = entrada_a.get()
                resposta_entrada_a = float(resposta_entrada_a)
                resposta_entrada_b = entrada_b.get()
                resposta_entrada_b = float(resposta_entrada_b)

                # Probabilidade
                if resposta_entrada_b <= resposta_largura_caixa:
                  # Função a ser integrada: sen^2(x)
                  def integrand(x):
                    # Cálculo para o número quântico inicial
                    constante_inicial = (2 / resposta_n_inicial_particula * pi)
                    return constante_inicial * np.sin(x)**2

                  # Defina os limites de integração
                  a_inicial = ((resposta_n_inicial_particula * pi) /
                               resposta_largura_caixa
                               ) * resposta_entrada_a  # Limite inferior
                  b_inicial = (
                      (resposta_n_inicial_particula * pi) /
                      resposta_largura_caixa
                  ) * resposta_entrada_b  # Limite superior (por exemplo, pi para uma única onda completa)

                  # Realize a integração
                  result, _ = quad(integrand, a_inicial, b_inicial)
                  resultado_inicial = round(result, 4)
                  resultado_inicial = resultado_inicial * 10
                  resultado_inicial = round(resultado_inicial)

                def integrand(x):
                  # Cálculo para o número quântico inicial
                  constante_final = (2 / resposta_n_final_particula * pi)
                  return constante_final * np.sin(x)**2

                # Defina os limites de integração
                a_final = (
                    (resposta_n_final_particula * pi) / resposta_largura_caixa
                ) * resposta_entrada_a  # Limite inferior
                b_final = (
                    (resposta_n_final_particula * pi) / resposta_largura_caixa
                ) * resposta_entrada_b  # Limite superior (por exemplo, pi para uma única onda completa)

                # Realize a integração
                result, _ = quad(integrand, a_final, b_final)
                resultado_final = round(result, 4)
                resultado_final = resultado_final * 10
                resultado_final = round(resultado_final)

                global janela

                if janela:
                  janela.destroy()

                janela = Tk()
                janela.title("PPU (saídas probabilidade)")
                janela.geometry("400x400")

                rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final = Label(
                    janela,
                    text=
                    "Probabilidade (𝑃(𝑎≤𝑥≤𝑏)) de encontrar a partícula no nível inicial e final",
                    font=("Arial", 8))
                rotulo_probabilidade_nivel_inicial = Label(
                    janela, text="Nível inicial:")
                rotulo_resposta_probabilidade_nivel_inicial = Label(
                    janela, text=f"{resultado_inicial}%", fg='green')
                rotulo_probabilidade_nivel_final = Label(janela,
                                                         text="Nível final:")
                rotulo_resposta_probabilidade_nivel_final = Label(
                    janela, text=f"{resultado_final}%", fg='green')
                rotulo_proxima_pagina = Label(janela, text="Próxima página:")

                def clique8():

                  from matplotlib.widgets import Button

                  def wave_function_inicial(x):
                    return a * np.sin(k_funcao_onda_n_inicial * x)

                  def wave_function_final(x):
                    return a * np.sin(k_funcao_onda_n_final * x)

                  def wave_function_probabilidade_inicial(x):
                    return wave_function_inicial(x)**2

                  def wave_function_probabilidade_final(x):
                    return wave_function_final(x)**2

                  L = resposta_largura_caixa
                  n_inicial = resposta_n_inicial_particula
                  n_final = resposta_n_final_particula

                  x = np.linspace(0, L, 1000)

                  fig, ax = plt.subplots()

                  def plot_inicial(event):
                    ax.clear()
                    ax.plot(x,
                            wave_function_inicial(x),
                            label=f'Nível Inicial')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ(x)")
                    ax.set_title(
                        "Gráfico da Função de Onda para o Poço de Potencial Infinito (nível inicial)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  def plot_final(event):
                    ax.clear()
                    ax.plot(x, wave_function_final(x), label=f'Nível Final')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ(x)")
                    ax.set_title(
                        "Gráfico da Função de Onda para o Poço de Potencial Infinito (nível final)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  def plot_inicial_squared(event):
                    ax.clear()
                    ax.plot(x,
                            wave_function_probabilidade_inicial(x),
                            label=f'Probabilidade nível inicial')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ^2(x)")
                    ax.set_title(
                        "Gráfico da função distribuição de probabilidade (nível inicial)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  def plot_final_squared(event):
                    ax.clear()
                    ax.plot(x,
                            wave_function_probabilidade_final(x),
                            label=f'Probabilidade nível final')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ^2(x)")
                    ax.set_title(
                        "Gráfico da função distribuição de probabilidade (nível final)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  axinicial = plt.axes([0.15, 0.01, 0.1, 0.05])
                  axfinal = plt.axes([0.3, 0.01, 0.1, 0.05])
                  axprobinicial = plt.axes([0.45, 0.01, 0.1, 0.05])
                  axprobfinal = plt.axes([0.6, 0.01, 0.1, 0.05])
                  binicial = Button(axinicial, 'Inicial')
                  bfinal = Button(axfinal, 'Final')
                  bprobinicial = Button(axprobinicial, 'P. Inicial')
                  bprobfinal = Button(axprobfinal, 'P. Final')

                  binicial.on_clicked(plot_inicial)
                  bfinal.on_clicked(plot_final)
                  bprobinicial.on_clicked(plot_inicial_squared)
                  bprobfinal.on_clicked(plot_final_squared)

                  plot_inicial(None)

                  plt.show()

                botao_proxima_pagina = Button(janela,
                                              text="Next",
                                              command=clique8)

                rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final.place(
                    x=200, y=10, anchor=CENTER)
                rotulo_probabilidade_nivel_inicial.place(x=200,
                                                         y=70,
                                                         anchor=CENTER)
                rotulo_resposta_probabilidade_nivel_inicial.place(
                    x=200, y=100, anchor=CENTER)
                rotulo_probabilidade_nivel_final.place(x=200,
                                                       y=170,
                                                       anchor=CENTER)
                rotulo_resposta_probabilidade_nivel_final.place(x=200,
                                                                y=200,
                                                                anchor=CENTER)
                rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

                botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

              botao_ok = Button(janela, text="OK", command=clique7)

              rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final.place(
                  x=200, y=10, anchor=CENTER)
              rotulo_particula_em_a.place(x=200, y=70, anchor=CENTER)
              entrada_a.place(x=200, y=100, anchor=CENTER)
              rotulo_particula_em_b.place(x=200, y=170, anchor=CENTER)
              entrada_b.place(x=200, y=200, anchor=CENTER)
              rotulo_calcular.place(x=200, y=270, anchor=CENTER)

              botao_ok.place(x=200, y=300, anchor=CENTER)

            botao_proxima_pagina = Button(janela, text="Next", command=clique6)

            rotulo_comprimento_onda_DeBroglie.place(x=200, y=10, anchor=CENTER)
            rotulo_particula_nivel_quantico_inicial.place(x=200,
                                                          y=70,
                                                          anchor=CENTER)
            rotulo_resposta_particula_nivel_quantico_inicial.place(
                x=200, y=100, anchor=CENTER)
            rotulo_particula_nivel_quantico_final.place(x=200,
                                                        y=170,
                                                        anchor=CENTER)
            rotulo_resposta_particula_nivel_quantico_final.place(x=200,
                                                                 y=200,
                                                                 anchor=CENTER)
            rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

            botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

          botao_proxima_pagina = Button(janela, text="Next", command=clique5)

          rotulo_velocidade_particula_nivel_quantico_inicial_final.place(
              x=200, y=10, anchor=CENTER)
          rotulo_velocidade_inicial.place(x=200, y=70, anchor=CENTER)
          rotulo_resposta_velocidade_inicial.place(x=200, y=100, anchor=CENTER)
          rotulo_velocidade_final.place(x=200, y=170, anchor=CENTER)
          rotulo_resposta_velocidade_final.place(x=200, y=200, anchor=CENTER)
          rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

          botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

        botao_proxima_pagina = Button(janela, text="Next", command=clique4)

        rotulo_foton_absorvido_emitido_transicao_niveis.place(x=200,
                                                              y=10,
                                                              anchor=CENTER)
        rotulo_energia.place(x=200, y=60, anchor=CENTER)
        rotulo_resposta_energia.place(x=200, y=80, anchor=CENTER)
        rotulo_frequencia.place(x=200, y=140, anchor=CENTER)
        rotulo_resposta_frequencia.place(x=200, y=160, anchor=CENTER)
        rotulo_comprimento_onda.place(x=200, y=220, anchor=CENTER)
        rotulo_resposta_comprimento_onda.place(x=200, y=240, anchor=CENTER)
        rotulo_proxima_pagina.place(x=200, y=300, anchor=CENTER)

        botao_proxima_pagina.place(x=200, y=325, anchor=CENTER)

      botao_proxima_pagina = Button(janela, text="Next", command=clique3)

      rotulo_energia_nivel_quantico_inicial_e_final.place(x=200,
                                                          y=10,
                                                          anchor=CENTER)
      rotulo_Ei_eV.place(x=200, y=50, anchor=CENTER)
      rotulo_resposta_Ei_eV.place(x=200, y=70, anchor=CENTER)
      rotulo_Ef_eV.place(x=200, y=110, anchor=CENTER)
      rotulo_resposta_Ef_eV.place(x=200, y=130, anchor=CENTER)
      rotulo_Ei_J.place(x=200, y=170, anchor=CENTER)
      rotulo_resposta_Ei_J.place(x=200, y=190, anchor=CENTER)
      rotulo_Ef_J.place(x=200, y=230, anchor=CENTER)
      rotulo_resposta_Ef_J.place(x=200, y=250, anchor=CENTER)
      rotulo_proxima_pagina.place(x=200, y=290, anchor=CENTER)

      botao_proxima_pagina.place(x=200, y=315, anchor=CENTER)

    botao_proxima_pagina = Button(janela, text="Next", command=clique2)

    rotulo_funcao_onda_quantica_si_dois_niveis.place(x=200,
                                                     y=10,
                                                     anchor=CENTER)
    rotulo_nivel_inicial.place(x=200, y=70, anchor=CENTER)
    rotulo_resposta_nivel_inicial.place(x=200, y=100, anchor=CENTER)
    rotulo_nivel_final.place(x=200, y=170, anchor=CENTER)
    rotulo_resposta_nivel_final.place(x=200, y=200, anchor=CENTER)
    rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

    botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

  botao_calcular = Button(janela, text="OK", command=clique)
  botao_voltar = Button(janela, text="Voltar", command=tema1)

  rotulo_largura_caixa.place(x=200, y=30, anchor=CENTER)
  rotulo_n_inicial_particula.place(x=200, y=100, anchor=CENTER)
  rotulo_n_final_particula.place(x=200, y=170, anchor=CENTER)
  rotulo_calcular.place(x=200, y=240, anchor=CENTER)
  rotulo_voltar.place(x=200, y=310, anchor=CENTER)

  entrada_largura_caixa.place(x=200, y=60, anchor=CENTER)
  entrada_n_inicial_particula.place(x=200, y=130, anchor=CENTER)
  entrada_n_final_particula.place(x=200, y=200, anchor=CENTER)

  botao_calcular.place(x=200, y=270, anchor=CENTER)
  botao_voltar.place(x=200, y=340, anchor=CENTER)


def entradas_tema1_pronton():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("PPU (prótons)")
  janela.geometry("400x400")

  rotulo_largura_caixa = Label(janela, text="Largura da caixa (L):")
  rotulo_n_inicial_particula = Label(janela,
                                     text="n inicial da partícula(ni):")
  rotulo_n_final_particula = Label(janela, text="n final da partícula(nf):")
  rotulo_calcular = Label(janela, text="Calcular:")
  rotulo_voltar = Label(janela, text="Voltar para a página anterior:")

  entrada_largura_caixa = Entry(janela)
  entrada_n_inicial_particula = Entry(janela)
  entrada_n_final_particula = Entry(janela)

  def clique():
    resposta_largura_caixa = entrada_largura_caixa.get()
    resposta_largura_caixa = float(resposta_largura_caixa)
    resposta_n_inicial_particula = entrada_n_inicial_particula.get()
    resposta_n_inicial_particula = float(resposta_n_inicial_particula)
    resposta_n_final_particula = entrada_n_final_particula.get()
    resposta_n_final_particula = float(resposta_n_final_particula)

    # Constantes
    h = 6.626E-34

    # Massa do próton
    m = 1.674E-24

    # Cálculos para a fórmula de onda
    a = 2 / resposta_largura_caixa
    a = sqrt(a)
    k_funcao_onda_n_inicial = (resposta_n_inicial_particula *
                               pi) / resposta_largura_caixa
    k_funcao_onda_n_final = (resposta_n_final_particula *
                             pi) / resposta_largura_caixa

    # Cálculos para o cálculo de energia
    energia_inicial_j = ((resposta_n_inicial_particula**2) *
                         (h**2)) / (8 * m * (resposta_largura_caixa**2))
    energia_final_j = ((resposta_n_final_particula**2) *
                       (h**2)) / (8 * m * (resposta_largura_caixa**2))
    energia_inicial_ev = energia_inicial_j / 1.602E-19
    energia_final_ev = energia_final_j / 1.602E-19

    # Cálculos para o fóton
    energia_foton_ev = energia_final_ev - energia_inicial_ev
    energia_foton_j = energia_final_j - energia_inicial_j

    # Cálculos para o comprimento de onda do fóton
    comprimento_de_onda_foton = (4.136E-15 * 3E8) / energia_foton_ev

    # Cálculos para a frequência do fóton
    frequencia_foton = energia_foton_ev / 4.136E-15

    # Cálculos para a velocidade
    velocidade_inicial = (2 * energia_inicial_j) / m
    velocidade_inicial = sqrt(velocidade_inicial)

    velocidade_final = (2 * energia_final_j) / m
    velocidade_final = sqrt(velocidade_final)

    # Comprimento de onda
    comprimento_de_onda_inicial = (
        2 * resposta_largura_caixa) / resposta_n_inicial_particula
    comprimento_de_onda_final = (
        2 * resposta_largura_caixa) / resposta_n_final_particula

    global janela

    if janela:
      janela.destroy()

    janela = Tk()
    janela.title("PPU (saídas)")
    janela.geometry("400x400")

    rotulo_funcao_onda_quantica_si_dois_niveis = Label(
        janela, text="Função de onda quântica no SI dos dois níveis")
    rotulo_nivel_inicial = Label(janela, text="Nível inicial:")
    rotulo_resposta_nivel_inicial = Label(
        janela,
        text=
        f"ψ2(x)={format(a, '.3E')}sin({format(k_funcao_onda_n_inicial, '.3E')}*x)",
        fg='green')
    rotulo_nivel_final = Label(janela, text="Nível final:")
    rotulo_resposta_nivel_final = Label(
        janela,
        text=
        f"ψ2(x)={format(a, '.3E')}sin({format(k_funcao_onda_n_final, '.3E')}*x)",
        fg='green')
    rotulo_proxima_pagina = Label(janela, text="Próxima página:")
    rotulo_voltar = Label(janela, text="Voltar para a página anterior:")

    def clique2():
      global janela

      if janela:
        janela.destroy()

      janela = Tk()
      janela.title("PPU (saídas)")
      janela.geometry("400x400")

      rotulo_energia_nivel_quantico_inicial_e_final = Label(
          janela, text="Energia do nível quântico inicial (Ei) e final (Ef): ")
      rotulo_Ei_eV = Label(janela, text="Ei (eV):")
      rotulo_resposta_Ei_eV = Label(janela,
                                    text=format(energia_inicial_ev, '.3E'),
                                    fg='green')
      rotulo_Ef_eV = Label(janela, text="Ef (eV):")
      rotulo_resposta_Ef_eV = Label(janela,
                                    text=format(energia_final_ev, '.3E'),
                                    fg='green')
      rotulo_Ei_J = Label(janela, text="Ei (J):")
      rotulo_resposta_Ei_J = Label(janela,
                                   text=format(energia_inicial_j, '.3E'),
                                   fg='green')
      rotulo_Ef_J = Label(janela, text="Ef (J):")
      rotulo_resposta_Ef_J = Label(janela,
                                   text=format(energia_final_j, '.3E'),
                                   fg='green')
      rotulo_proxima_pagina = Label(janela, text="Próxima página:")

      def clique3():
        global janela

        if janela:
          janela.destroy()

        janela = Tk()
        janela.title("PPU (saídas)")
        janela.geometry("400x400")

        rotulo_foton_absorvido_emitido_transicao_niveis = Label(
            janela,
            text=
            "Fóton absorvido ou emitido pela partícula na transição entre os níveis",
            font=("Arial", 8))
        rotulo_energia = Label(janela, text="Energia (𝐸𝑓ó𝑡𝑜𝑛):")
        rotulo_resposta_energia = Label(janela,
                                        text=format(energia_foton_ev, '.3E'),
                                        fg='green')
        rotulo_frequencia = Label(janela, text="Frequência (𝑓):")
        rotulo_resposta_frequencia = Label(janela,
                                           text=format(frequencia_foton,
                                                       '.3E'),
                                           fg='green')
        rotulo_comprimento_onda = Label(janela,
                                        text="Comprimento de onda (λ):")
        rotulo_resposta_comprimento_onda = Label(janela,
                                                 text=format(
                                                     comprimento_de_onda_foton,
                                                     '.3E'),
                                                 fg='green')
        rotulo_proxima_pagina = Label(janela, text="Próxima página:")

        def clique4():
          global janela

          if janela:
            janela.destroy()

          janela = Tk()
          janela.title("PPU (saídas)")
          janela.geometry("400x400")

          rotulo_velocidade_particula_nivel_quantico_inicial_final = Label(
              janela,
              text=
              "Velocidade (𝑣) da partícula no nível quântico inicial e final")
          rotulo_velocidade_inicial = Label(janela, text="Velocidade inicial:")
          rotulo_resposta_velocidade_inicial = Label(janela,
                                                     text=format(
                                                         velocidade_inicial,
                                                         '.3E'),
                                                     fg='green')
          rotulo_velocidade_final = Label(janela, text="Velocidade final:")
          rotulo_resposta_velocidade_final = Label(janela,
                                                   text=format(
                                                       velocidade_final,
                                                       '.3E'),
                                                   fg='green')
          rotulo_proxima_pagina = Label(janela, text="Próxima página:")

          def clique5():
            global janela

            if janela:
              janela.destroy()

            janela = Tk()
            janela.title("PPU (saídas)")
            janela.geometry("400x400")

            rotulo_comprimento_onda_DeBroglie = Label(
                janela, text="Comprimento de onda de De Broglie (λn)")
            rotulo_particula_nivel_quantico_inicial = Label(
                janela, text="Partícula nível quântico inicial:")
            rotulo_resposta_particula_nivel_quantico_inicial = Label(
                janela,
                text=format(comprimento_de_onda_inicial, '.3E'),
                fg='green')
            rotulo_particula_nivel_quantico_final = Label(
                janela, text="Partícula nível quântico final:")
            rotulo_resposta_particula_nivel_quantico_final = Label(
                janela,
                text=format(comprimento_de_onda_final, '.3E'),
                fg='green')
            rotulo_proxima_pagina = Label(janela, text="Próxima página:")

            def clique6():
              global janela

              if janela:
                janela.destroy()

              janela = Tk()
              janela.title("PPU (probabilidade)")
              janela.geometry("400x400")

              rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final = Label(
                  janela,
                  text=
                  "Probabilidade (𝑃(𝑎≤𝑥≤𝑏)) de encontrar a partícula no nível inicial e final",
                  font=("Arial", 8))
              rotulo_particula_em_a = Label(janela, text="a:")
              entrada_a = Entry(janela)
              rotulo_particula_em_b = Label(janela, text="b:")
              entrada_b = Entry(janela)
              rotulo_calcular = Label(janela, text="Calcular:")

              def clique7():
                resposta_entrada_a = entrada_a.get()
                resposta_entrada_a = float(resposta_entrada_a)
                resposta_entrada_b = entrada_b.get()
                resposta_entrada_b = float(resposta_entrada_b)

                # Probabilidade
                if resposta_entrada_b <= resposta_largura_caixa:
                  # Função a ser integrada: sen^2(x)
                  def integrand(x):
                    # Cálculo para o número quântico inicial
                    constante_inicial = (2 / resposta_n_inicial_particula * pi)
                    return constante_inicial * np.sin(x)**2

                  # Defina os limites de integração
                  a_inicial = ((resposta_n_inicial_particula * pi) /
                               resposta_largura_caixa
                               ) * resposta_entrada_a  # Limite inferior
                  b_inicial = (
                      (resposta_n_inicial_particula * pi) /
                      resposta_largura_caixa
                  ) * resposta_entrada_b  # Limite superior (por exemplo, pi para uma única onda completa)

                  # Realize a integração
                  result, _ = quad(integrand, a_inicial, b_inicial)
                  resultado_inicial = round(result, 4)
                  resultado_inicial = resultado_inicial * 10
                  resultado_inicial = round(resultado_inicial)

                def integrand(x):
                  # Cálculo para o número quântico inicial
                  constante_final = (2 / resposta_n_final_particula * pi)
                  return constante_final * np.sin(x)**2

                # Defina os limites de integração
                a_final = (
                    (resposta_n_final_particula * pi) / resposta_largura_caixa
                ) * resposta_entrada_a  # Limite inferior
                b_final = (
                    (resposta_n_final_particula * pi) / resposta_largura_caixa
                ) * resposta_entrada_b  # Limite superior (por exemplo, pi para uma única onda completa)

                # Realize a integração
                result, _ = quad(integrand, a_final, b_final)
                resultado_final = round(result, 4)
                resultado_final = resultado_final * 10
                resultado_final = round(resultado_final)

                global janela

                if janela:
                  janela.destroy()

                janela = Tk()
                janela.title("PPU (saídas probabilidade)")
                janela.geometry("400x400")

                rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final = Label(
                    janela,
                    text=
                    "Probabilidade (𝑃(𝑎≤𝑥≤𝑏)) de encontrar a partícula no nível inicial e final",
                    font=("Arial", 8))
                rotulo_probabilidade_nivel_inicial = Label(
                    janela, text="Nível inicial:")
                rotulo_resposta_probabilidade_nivel_inicial = Label(
                    janela, text=f"{resultado_inicial}%", fg='green')
                rotulo_probabilidade_nivel_final = Label(janela,
                                                         text="Nível final:")
                rotulo_resposta_probabilidade_nivel_final = Label(
                    janela, text=f"{resultado_final}%", fg='green')
                rotulo_proxima_pagina = Label(janela, text="Próxima página:")

                def clique8():

                  from matplotlib.widgets import Button

                  def wave_function_inicial(x):
                    return a * np.sin(k_funcao_onda_n_inicial * x)

                  def wave_function_final(x):
                    return a * np.sin(k_funcao_onda_n_final * x)

                  def wave_function_probabilidade_inicial(x):
                    return wave_function_inicial(x)**2

                  def wave_function_probabilidade_final(x):
                    return wave_function_final(x)**2

                  L = resposta_largura_caixa
                  n_inicial = resposta_n_inicial_particula
                  n_final = resposta_n_final_particula

                  x = np.linspace(0, L, 1000)

                  fig, ax = plt.subplots()

                  def plot_inicial(event):
                    ax.clear()
                    ax.plot(x,
                            wave_function_inicial(x),
                            label=f'Nível Inicial')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ(x)")
                    ax.set_title(
                        "Gráfico da Função de Onda para o Poço de Potencial Infinito (nível inicial)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  def plot_final(event):
                    ax.clear()
                    ax.plot(x, wave_function_final(x), label=f'Nível Final')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ(x)")
                    ax.set_title(
                        "Gráfico da Função de Onda para o Poço de Potencial Infinito (nível final)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  def plot_inicial_squared(event):
                    ax.clear()
                    ax.plot(x,
                            wave_function_probabilidade_inicial(x),
                            label=f'Probabilidade nível inicial')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ^2(x)")
                    ax.set_title(
                        "Gráfico da função distribuição de probabilidade (nível inicial)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  def plot_final_squared(event):
                    ax.clear()
                    ax.plot(x,
                            wave_function_probabilidade_final(x),
                            label=f'Probabilidade nível final')
                    ax.set_xlabel("x")
                    ax.set_ylabel("ψ^2(x)")
                    ax.set_title(
                        "Gráfico da função distribuição de probabilidade (nível final)"
                    )
                    ax.legend()
                    ax.grid(True)
                    plt.draw()

                  axinicial = plt.axes([0.15, 0.01, 0.1, 0.05])
                  axfinal = plt.axes([0.3, 0.01, 0.1, 0.05])
                  axprobinicial = plt.axes([0.45, 0.01, 0.1, 0.05])
                  axprobfinal = plt.axes([0.6, 0.01, 0.1, 0.05])
                  binicial = Button(axinicial, 'Inicial')
                  bfinal = Button(axfinal, 'Final')
                  bprobinicial = Button(axprobinicial, 'P. Inicial')
                  bprobfinal = Button(axprobfinal, 'P. Final')

                  binicial.on_clicked(plot_inicial)
                  bfinal.on_clicked(plot_final)
                  bprobinicial.on_clicked(plot_inicial_squared)
                  bprobfinal.on_clicked(plot_final_squared)

                  plot_inicial(None)

                  plt.show()

                botao_proxima_pagina = Button(janela,
                                              text="Next",
                                              command=clique8)

                rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final.place(
                    x=200, y=10, anchor=CENTER)
                rotulo_probabilidade_nivel_inicial.place(x=200,
                                                         y=70,
                                                         anchor=CENTER)
                rotulo_resposta_probabilidade_nivel_inicial.place(
                    x=200, y=100, anchor=CENTER)
                rotulo_probabilidade_nivel_final.place(x=200,
                                                       y=170,
                                                       anchor=CENTER)
                rotulo_resposta_probabilidade_nivel_final.place(x=200,
                                                                y=200,
                                                                anchor=CENTER)
                rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

                botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

              botao_ok = Button(janela, text="OK", command=clique7)

              rotulo_probabilidade_encontrar_particula_entre_a_e_b_nivel_inicial_final.place(
                  x=200, y=10, anchor=CENTER)
              rotulo_particula_em_a.place(x=200, y=70, anchor=CENTER)
              entrada_a.place(x=200, y=100, anchor=CENTER)
              rotulo_particula_em_b.place(x=200, y=170, anchor=CENTER)
              entrada_b.place(x=200, y=200, anchor=CENTER)
              rotulo_calcular.place(x=200, y=270, anchor=CENTER)

              botao_ok.place(x=200, y=300, anchor=CENTER)

            botao_proxima_pagina = Button(janela, text="Next", command=clique6)

            rotulo_comprimento_onda_DeBroglie.place(x=200, y=10, anchor=CENTER)
            rotulo_particula_nivel_quantico_inicial.place(x=200,
                                                          y=70,
                                                          anchor=CENTER)
            rotulo_resposta_particula_nivel_quantico_inicial.place(
                x=200, y=100, anchor=CENTER)
            rotulo_particula_nivel_quantico_final.place(x=200,
                                                        y=170,
                                                        anchor=CENTER)
            rotulo_resposta_particula_nivel_quantico_final.place(x=200,
                                                                 y=200,
                                                                 anchor=CENTER)
            rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

            botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

          botao_proxima_pagina = Button(janela, text="Next", command=clique5)

          rotulo_velocidade_particula_nivel_quantico_inicial_final.place(
              x=200, y=10, anchor=CENTER)
          rotulo_velocidade_inicial.place(x=200, y=70, anchor=CENTER)
          rotulo_resposta_velocidade_inicial.place(x=200, y=100, anchor=CENTER)
          rotulo_velocidade_final.place(x=200, y=170, anchor=CENTER)
          rotulo_resposta_velocidade_final.place(x=200, y=200, anchor=CENTER)
          rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

          botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

        botao_proxima_pagina = Button(janela, text="Next", command=clique4)

        rotulo_foton_absorvido_emitido_transicao_niveis.place(x=200,
                                                              y=10,
                                                              anchor=CENTER)
        rotulo_energia.place(x=200, y=60, anchor=CENTER)
        rotulo_resposta_energia.place(x=200, y=80, anchor=CENTER)
        rotulo_frequencia.place(x=200, y=140, anchor=CENTER)
        rotulo_resposta_frequencia.place(x=200, y=160, anchor=CENTER)
        rotulo_comprimento_onda.place(x=200, y=220, anchor=CENTER)
        rotulo_resposta_comprimento_onda.place(x=200, y=240, anchor=CENTER)
        rotulo_proxima_pagina.place(x=200, y=300, anchor=CENTER)

        botao_proxima_pagina.place(x=200, y=325, anchor=CENTER)

      botao_proxima_pagina = Button(janela, text="Next", command=clique3)

      rotulo_energia_nivel_quantico_inicial_e_final.place(x=200,
                                                          y=10,
                                                          anchor=CENTER)
      rotulo_Ei_eV.place(x=200, y=50, anchor=CENTER)
      rotulo_resposta_Ei_eV.place(x=200, y=70, anchor=CENTER)
      rotulo_Ef_eV.place(x=200, y=110, anchor=CENTER)
      rotulo_resposta_Ef_eV.place(x=200, y=130, anchor=CENTER)
      rotulo_Ei_J.place(x=200, y=170, anchor=CENTER)
      rotulo_resposta_Ei_J.place(x=200, y=190, anchor=CENTER)
      rotulo_Ef_J.place(x=200, y=230, anchor=CENTER)
      rotulo_resposta_Ef_J.place(x=200, y=250, anchor=CENTER)
      rotulo_proxima_pagina.place(x=200, y=290, anchor=CENTER)

      botao_proxima_pagina.place(x=200, y=315, anchor=CENTER)

    botao_proxima_pagina = Button(janela, text="Next", command=clique2)

    rotulo_funcao_onda_quantica_si_dois_niveis.place(x=200,
                                                     y=10,
                                                     anchor=CENTER)
    rotulo_nivel_inicial.place(x=200, y=70, anchor=CENTER)
    rotulo_resposta_nivel_inicial.place(x=200, y=100, anchor=CENTER)
    rotulo_nivel_final.place(x=200, y=170, anchor=CENTER)
    rotulo_resposta_nivel_final.place(x=200, y=200, anchor=CENTER)
    rotulo_proxima_pagina.place(x=200, y=270, anchor=CENTER)

    botao_proxima_pagina.place(x=200, y=300, anchor=CENTER)

  botao_calcular = Button(janela, text="OK", command=clique)
  botao_voltar = Button(janela, text="Voltar", command=tema1)

  rotulo_largura_caixa.place(x=200, y=30, anchor=CENTER)
  rotulo_n_inicial_particula.place(x=200, y=100, anchor=CENTER)
  rotulo_n_final_particula.place(x=200, y=170, anchor=CENTER)
  rotulo_calcular.place(x=200, y=240, anchor=CENTER)
  rotulo_voltar.place(x=200, y=310, anchor=CENTER)

  entrada_largura_caixa.place(x=200, y=60, anchor=CENTER)
  entrada_n_inicial_particula.place(x=200, y=130, anchor=CENTER)
  entrada_n_final_particula.place(x=200, y=200, anchor=CENTER)

  botao_calcular.place(x=200, y=270, anchor=CENTER)
  botao_voltar.place(x=200, y=340, anchor=CENTER)


def tema1():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("PPU")
  janela.geometry("400x400")

  rotulo_ppu = Label(janela, text="Poço de potencial unidimensional")
  rotulo_confinando_eletron = Label(janela, text="Confinando um elétron:")
  rotulo_confinando_proton = Label(janela, text="Confinando um próton:")
  rotulo_voltar = Label(janela, text="Voltar para o menu:")

  botao_confinando_eletron = Button(janela,
                                    text="Entrar",
                                    command=entradas_tema1_eletron)
  botao_confinando_proton = Button(janela,
                                   text="Entrar",
                                   command=entradas_tema1_pronton)
  botao_voltar = Button(janela, text="Voltar", command=menu)

  rotulo_ppu.place(x=200, y=10, anchor=CENTER)
  rotulo_confinando_eletron.place(x=200, y=70, anchor=CENTER)
  rotulo_confinando_proton.place(x=200, y=170, anchor=CENTER)
  rotulo_voltar.place(x=200, y=270, anchor=CENTER)

  botao_confinando_eletron.place(x=200, y=100, anchor=CENTER)
  botao_confinando_proton.place(x=200, y=200, anchor=CENTER)
  botao_voltar.place(x=200, y=300, anchor=CENTER)


def entradas_tema2_eletrons():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("Função de onda (elétrons)")
  janela.geometry("400x400")

  rotulo_A = Label(janela, text="A:")
  rotulo_k = Label(janela, text="k:")
  rotulo_xp = Label(janela, text="xp:")
  rotulo_calcular = Label(janela, text="Calcular:")
  rotulo_voltar = Label(janela, text="Voltar para a página anterior:")

  entrada_A = Entry(janela)
  entrada_k = Entry(janela)
  entrada_xp = Entry(janela)

  #cálculos dentro dessa função
  def clique():
    resposta_A = entrada_A.get()
    resposta_A = float(resposta_A)
    resposta_k = entrada_k.get()
    resposta_k = float(resposta_k)
    resposta_xp = entrada_xp.get()
    resposta_xp = float(resposta_xp)

    # Massa do eletrón
    m = 9.11E-31

    # Largura do poço
    largura_poco = 2 / (resposta_A**2)

    # Nível Quântico
    nivel_quantico = (largura_poco * resposta_k) / pi
    nivel_quantico = round(nivel_quantico, 2)

    # Probabilidade
    xp = resposta_xp * largura_poco
    probabilidade = (resposta_A**2) * round((sin(resposta_k * xp)**2), 4)

    global janela

    if janela:
      janela.destroy()

    janela = Tk()
    janela.title("Função de onda (saídas)")
    janela.geometry("400x400")

    rotulo_largura_poco = Label(janela, text="Largura do poço:")
    rotulo_resultado_lp = Label(janela,
                                text=format(largura_poco, '.3E'),
                                fg='green')
    rotulo_nivel_quantico = Label(janela, text="Nível quântico:")
    rotulo_resultado_nq = Label(janela,
                                text=format(nivel_quantico, '.3E'),
                                fg='green')
    rotulo_probabilidade = Label(janela, text="Probabilidade:")
    rotulo_resultado_p = Label(janela,
                               text=format(probabilidade, '.3E'),
                               fg='green')

    rotulo_largura_poco.place(x=200, y=70, anchor=CENTER)
    rotulo_resultado_lp.place(x=200, y=100, anchor=CENTER)
    rotulo_nivel_quantico.place(x=200, y=170, anchor=CENTER)
    rotulo_resultado_nq.place(x=200, y=200, anchor=CENTER)
    rotulo_probabilidade.place(x=200, y=270, anchor=CENTER)
    rotulo_resultado_p.place(x=200, y=300, anchor=CENTER)

  botao_calcular = Button(janela, text="OK", command=clique)
  botao_voltar = Button(janela, text="Voltar", command=tema2)

  rotulo_A.place(x=200, y=30, anchor=CENTER)
  rotulo_k.place(x=200, y=100, anchor=CENTER)
  rotulo_xp.place(x=200, y=170, anchor=CENTER)
  rotulo_calcular.place(x=200, y=240, anchor=CENTER)
  rotulo_voltar.place(x=200, y=310, anchor=CENTER)

  entrada_A.place(x=200, y=60, anchor=CENTER)
  entrada_k.place(x=200, y=130, anchor=CENTER)
  entrada_xp.place(x=200, y=200, anchor=CENTER)

  botao_calcular.place(x=200, y=270, anchor=CENTER)
  botao_voltar.place(x=200, y=340, anchor=CENTER)


def entradas_tema2_protons():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("Função de onda (prótons)")
  janela.geometry("400x400")

  rotulo_A = Label(janela, text="A:")
  rotulo_k = Label(janela, text="k:")
  rotulo_xp = Label(janela, text="xp:")
  rotulo_calcular = Label(janela, text="Calcular:")
  rotulo_voltar = Label(janela, text="Voltar para a página anterior:")

  entrada_A = Entry(janela)
  entrada_k = Entry(janela)
  entrada_xp = Entry(janela)

  #cálculos dentro dessa função
  def clique():
    resposta_A = entrada_A.get()
    resposta_A = float(resposta_A)
    resposta_k = entrada_k.get()
    resposta_k = float(resposta_k)
    resposta_xp = entrada_xp.get()
    resposta_xp = float(resposta_xp)

    # Massa do próton
    m = 1.674E-24

    # Largura do poço
    largura_poco = 2 / (resposta_A**2)

    # Nível Quântico
    nivel_quantico = (largura_poco * resposta_k) / pi
    nivel_quantico = round(nivel_quantico, 2)

    # Probabilidade
    xp = resposta_xp * largura_poco
    probabilidade = (resposta_A**2) * round((sin(resposta_k * xp)**2), 4)

    global janela

    if janela:
      janela.destroy()

    janela = Tk()
    janela.title("Função de onda (saídas)")
    janela.geometry("400x400")

    rotulo_largura_poco = Label(janela, text="Largura do poço:")
    rotulo_resultado_lp = Label(janela,
                                text=format(largura_poco, '.3E'),
                                fg='green')
    rotulo_nivel_quantico = Label(janela, text="Nível quântico:")
    rotulo_resultado_nq = Label(janela,
                                text=format(nivel_quantico, '.3E'),
                                fg='green')
    rotulo_probabilidade = Label(janela, text="Probabilidade:")
    rotulo_resultado_p = Label(janela,
                               text=format(probabilidade, '.3E'),
                               fg='green')

    rotulo_largura_poco.place(x=200, y=70, anchor=CENTER)
    rotulo_resultado_lp.place(x=200, y=100, anchor=CENTER)
    rotulo_nivel_quantico.place(x=200, y=170, anchor=CENTER)
    rotulo_resultado_nq.place(x=200, y=200, anchor=CENTER)
    rotulo_probabilidade.place(x=200, y=270, anchor=CENTER)
    rotulo_resultado_p.place(x=200, y=300, anchor=CENTER)

  botao_calcular = Button(janela, text="OK", command=clique)
  botao_voltar = Button(janela, text="Voltar", command=tema2)

  rotulo_A.place(x=200, y=30, anchor=CENTER)
  rotulo_k.place(x=200, y=100, anchor=CENTER)
  rotulo_xp.place(x=200, y=170, anchor=CENTER)
  rotulo_calcular.place(x=200, y=240, anchor=CENTER)
  rotulo_voltar.place(x=200, y=310, anchor=CENTER)

  entrada_A.place(x=200, y=60, anchor=CENTER)
  entrada_k.place(x=200, y=130, anchor=CENTER)
  entrada_xp.place(x=200, y=200, anchor=CENTER)

  botao_calcular.place(x=200, y=270, anchor=CENTER)
  botao_voltar.place(x=200, y=340, anchor=CENTER)


def tema2():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("Função de onda")
  janela.geometry("400x400")

  rotulo_confinando_eletron = Label(janela, text="Confinando um elétron:")
  rotulo_confinando_proton = Label(janela, text="Confinando um próton:")
  rotulo_voltar = Label(janela, text="Voltar para o menu:")

  botao_confinando_eletron = Button(janela,
                                    text="Entrar",
                                    command=entradas_tema2_eletrons)
  botao_confinando_proton = Button(janela,
                                   text="Entrar",
                                   command=entradas_tema2_protons)
  botao_voltar = Button(janela, text="Voltar", command=menu)

  rotulo_confinando_eletron.place(x=200, y=70, anchor=CENTER)
  rotulo_confinando_proton.place(x=200, y=170, anchor=CENTER)
  rotulo_voltar.place(x=200, y=270, anchor=CENTER)

  botao_confinando_eletron.place(x=200, y=100, anchor=CENTER)
  botao_confinando_proton.place(x=200, y=200, anchor=CENTER)
  botao_voltar.place(x=200, y=300, anchor=CENTER)


def sair():
  global janela

  res = messagebox.showinfo('Aviso', 'Programa encerrado!')
  janela.destroy()


def menu():
  global janela

  if janela:
    janela.destroy()

  janela = Tk()
  janela.title("Menu")
  janela.geometry('400x400')

  rotulo_tema1 = Label(janela, text="Poço de potencial unidimensional:")
  rotulo_tema2 = Label(janela, text="Função de onda:")
  rotulo_sair = Label(janela, text="Encerramento:")

  botao_tema1 = Button(janela, text="Entrar", command=tema1)
  botao_tema2 = Button(janela, text="Entrar", command=tema2)
  botao_sair = Button(janela, text="Sair", command=sair)

  rotulo_tema1.place(x=200, y=70, anchor=CENTER)
  rotulo_tema2.place(x=200, y=170, anchor=CENTER)
  rotulo_sair.place(x=200, y=270, anchor=CENTER)

  botao_tema1.place(x=200, y=100, anchor=CENTER)
  botao_tema2.place(x=200, y=200, anchor=CENTER)
  botao_sair.place(x=200, y=300, anchor=CENTER)

  janela.mainloop()


menu()
