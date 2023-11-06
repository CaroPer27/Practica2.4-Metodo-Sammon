#Distancia euclidiana
import math

n = len(new_data)
dist_m = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        p1 = new_data.iloc[i]
        p2 = new_data.iloc[j]

        sum = 0

        for col in new_data.columns:
            sum += (p1[col] - p2[col]) ** 2

        euclidiana_d = math.sqrt(sum)
        dist_m[i][j] = euclidiana_d
        dist_m[j][i] = euclidiana_d

dist_m