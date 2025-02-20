def min_length_segment_A(D_start, D_end, C_start, C_end):
    # Минимальная длина отрезка A
    # A должен начинаться после D и заканчиваться до C
    A_start = D_end
    A_end = C_start
    length_A = A_end - A_start
    
    # Если длина отрицательная, значит A не может существовать
    return max(0, length_A)

# Задаем отрезки D и C
D = (17, 58)
C = (29, 80)

# Вычисляем минимальную длину отрезка A
length_A = min_length_segment_A(D[0], D[1], C[0], C[1])
print(f"Минимальная длина отрезка A: {length_A}")
