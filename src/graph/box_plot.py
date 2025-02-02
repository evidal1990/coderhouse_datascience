import matplotlib.pyplot as pyplot
import seaborn as sns

from seaborn import boxplot


class BoxPlot:
    '''
    Utilizado para especificar o conjunto de dados que será utilizado.
    '''
    data = None
    '''
    Variável que será plotada no eixo x.
    '''
    x = None
    '''
    Variável que será plotada no eixo y.
    '''
    y = None
    '''
    Permite adicionar uma terceira variável categórica
    que será usada para dividir as caixas por cor
    '''
    hue = None
    '''
    Ordem para plotar os níveis categóricos;
    Caso contrário, os níveis são inferidos a partir dos objetos de dados.
    '''
    order = None
    hue_order = None
    '''
    Orientação do gráfico (vertical ou horizontal).
    '''
    orient = None
    '''
    Cor única para os elementos no gráfico.
    '''
    color = None
    '''
    Cor única para os elementos no gráfico.
    '''
    palette = None
    '''
    Proporção da saturação original para desenhar as cores de preenchimento.
    '''
    saturation = 0.75
    '''
    Se True, usa um patch sólido. Caso contrário, desenha como arte linear.
    '''
    fill = True
    '''
    Quando o mapeamento hue é usado, se os elementos devem ser estreitados e
    deslocados ao longo do eixo orient para eliminar sobreposição.
    '''
    dodge = "auto"
    '''
    Largura atribuída a cada elemento no eixo orient.
    '''
    width = 0.8
    '''
    Reduzir no eixo orient por este fator para adicionar um espaço
    entre elementos deslocados.
    '''
    gap = 0
    '''
    Parâmetro que controla o comprimento das hastes (whiskers)
    '''
    whis = 1.5
    '''
    Cor a ser usada para elementos de linha, quando o preenchimento é True.
    '''
    linecolor = "auto"
    '''
    Largura das linhas que contornam os elementos do gráfico.
    '''
    linewidth = None
    '''
    Tamanho dos marcadores usados para indicar observações outliers.
    '''
    fliersize = None
    '''
    Normalização em unidades de dados para o colormap aplicado à variável hue
    quando ela é numérica.
    Não relevante se hue for categórica.
    '''
    hue_norm = None
    '''
    Quando True, valores numéricos ou datetime no eixo categórico manterão
    sua escala original em vez de serem convertidos em índices fixos.
    '''
    native_scale = False
    '''
    Define a escala(s) do eixo como logarítmica.
    '''
    log_scale = None
    '''
    Função para converter dados categóricos em strings.
    Afeta tanto agrupamentos quanto rótulos dos ticks.
    '''
    formatter = None
    '''
    Como desenhar a legenda.
    '''
    legend = "auto"
    '''
    Objeto Axes onde o gráfico será desenhado;
    Caso contrário, usa os Axes atuais.
    '''
    ax = None
