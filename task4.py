# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти координатной плоскости: '))

if quarter == 1:
    print(f'К {quarter} четверти координатной плоскости принадлежат все точки с диапазоном координат х(0; +∞), y(0; +∞)')

elif quarter == 2:
    print(f'К {quarter} четверти координатной плоскости принадлежат все точки с диапазоном координат x(0; +∞), y(0; -∞)')

elif quarter == 3:
    print(f'К {quarter} четверти координатной плоскости принадлежат все точки с диапазоном координат x(0; -∞), y(0; -∞)')

elif quarter == 4:
    print(f'К {quarter} четверти координатной плоскости принадлежат все точки с диапазоном координат x(0; -∞), y(0; +∞)')

else:
    print('Неверное значение, четвертей всего 4.')



