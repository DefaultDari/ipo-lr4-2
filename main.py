numbers = input("Введите список чисел через запятую: ").split(',')  #Исходный список чисел
sqr = [int(number)**2 for number in numbers] #Генератор списка для создания списка с квадратами чисел
print(sqr) #Вывод нового списка
