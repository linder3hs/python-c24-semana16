# importamos matplotlib con el alias plt
import matplotlib.pyplot as plt

ganacias = [1000, 2500, 1200, 2200]
tiempo = ['2018', '2019', '2020', '2021']


def chart_basic():
    plt.plot(ganacias, tiempo)
    plt.ylabel('Tiempo')
    plt.xlabel('Ganancias')
    plt.show()


def chart_points():
    plt.plot(ganacias, tiempo, 'ro')
    # plt.axis([1000, 1200, 1400, 1500])
    plt.show()


def chart_bar():
    fig, ax = plt.subplots()
    rects1 = ax.bar(tiempo, ganacias, color="green")
    ax.set_title('Tiempo X Ganancias del 2018 - 2021')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Ganancias')
    ax.bar_label(rects1, padding=3)
    plt.savefig('chart_bar_green.svg')
    # plt.show()


def chart_pie():
    labels = 'Producto1', 'Producto2', 'Producto3', 'Producto4'
    sizes = [15, 30, 5, 50]
    explode = (0, 0.1, 0, 0)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, shadow=True, startangle=90,
           autopct='%1.1f%%', explode=explode, textprops=dict(color="b"))
    ax.legend()

    plt.show()


chart_pie()


