import numpy as np
import pandas as pd

# Список стран
countries = [
    "AL", "AND", "A", "BY", "B", "BIH", "BG", "HR", "CY", "CZ", "DK", "EST", "FIN", "F", "D", "GR", "H", "IS", "IRL", "I", "LV", "FL", "LT", "L", "M", "MD", "MC", "MNE", "NL", "NMK", "N", "PL", "P", "RO", "RUS", "RSM", "SRB", "SK", "SLO", "E", "S", "CH", "TR", "UA", "UK", "V"
]

# Создание матрицы расстояний, и заполнение бесконечностями (inf), кроме главной диагонали
size = len(countries)
distance_matrix = np.full((size, size), np.inf)
np.fill_diagonal(distance_matrix, 0)

# Добавления ребра с весом в матрицу расстояний
def add_edge(c1, c2, weight):
    i, j = countries.index(c1), countries.index(c2)
    distance_matrix[i, j] = distance_matrix[j, i] = weight

# Добавление границы с расстояниями
add_edge("AL", "MNE", 1)
add_edge("AL", "GR", 1)
add_edge("AND", "F", 1)
add_edge("A", "CH", 1)
add_edge("A", "D", 1)
add_edge("A", "CZ", 1)
add_edge("A", "SK", 1)
add_edge("A", "H", 1)
add_edge("BY", "PL", 1)
add_edge("BY", "LT", 1)
add_edge("BY", "LV", 1)
add_edge("BY", "RUS", 1)
add_edge("BY", "UA", 1)
add_edge("B", "F", 1)
add_edge("B", "NL", 1)
add_edge("B", "D", 1)
add_edge("BIH", "HR", 1)
add_edge("BIH", "SRB", 1)
add_edge("BIH", "MNE", 1)
add_edge("BG", "RO", 1)
add_edge("BG", "GR", 1)
add_edge("HR", "SLO", 1)
add_edge("HR", "H", 1)
add_edge("HR", "SRB", 1)
add_edge("CZ", "D", 1)
add_edge("CZ", "PL", 1)
add_edge("CZ", "SK", 1)
add_edge("DK", "D", 1)
add_edge("EST", "LV", 1)
add_edge("FIN", "S", 1)
add_edge("FIN", "RUS", 1)
add_edge("F", "E", 1)
add_edge("F", "D", 1)
add_edge("F", "L", 1)
add_edge("F", "CH", 1)
add_edge("GR", "TR", 1)
add_edge("GR", "NMK", 1)
add_edge("H", "SK", 1)
add_edge("H", "RO", 1)
add_edge("H", "SRB", 1)
add_edge("I", "CH", 1)
add_edge("I", "A", 1)
add_edge("I", "F", 1)
add_edge("LV", "LT", 1)
add_edge("LT", "PL", 1)
add_edge("L", "B", 1)
add_edge("L", "D", 1)
add_edge("MD", "UA", 1)
add_edge("MD", "RO", 1)
add_edge("MC", "F", 1)
add_edge("MNE", "SRB", 1)
add_edge("NL", "D", 1)
add_edge("NMK", "SRB", 1)
add_edge("NMK", "BG", 1)
add_edge("PL", "D", 1)
add_edge("PL", "SK", 1)
add_edge("PL", "UA", 1)
add_edge("RO", "UA", 1)
add_edge("RUS", "EST", 1)
add_edge("RUS", "LV", 1)
add_edge("RUS", "UA", 1)
add_edge("S", "N", 1)
add_edge("SRB", "RO", 1)
add_edge("SRB", "BG", 1)
add_edge("SLO", "A", 1)
add_edge("SLO", "H", 1)
add_edge("SLO", "HR", 1)
add_edge("CH", "D", 1)
add_edge("TR", "BG", 1)
add_edge("I", "V", 1)
add_edge("I", "RSM", 1)
add_edge("I", "SLO", 1)
add_edge("E", "P", 1)
add_edge("E", "AND", 1)
add_edge("CH", "FL", 1)
add_edge("FL", "A", 1)
add_edge("SK", "UA", 1)
add_edge("H", "UA", 1)
add_edge("PL", "RUS", 1)
add_edge("LT", "RUS", 1)
add_edge("RUS", "N", 1)
add_edge("HR", "MNE", 1)
add_edge("AL", "NMK", 1)
add_edge("AL", "SRB", 1)

# Алгоритм Флойда-Уоршелла
for k in range(size):
    for i in range(size):
        for j in range(size):
            distance_matrix[i, j] = min(distance_matrix[i, j], distance_matrix[i, k] + distance_matrix[k, j])

# Вывод в .csv
df = pd.DataFrame(distance_matrix, index=countries, columns=countries)
df.to_csv("distance_matrix.csv")


