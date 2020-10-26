# 3: Создайте программу “Медицинская анкета”,
# где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

# Ввод дааных пользователем

name = input('Введите ваше имя - ')
surname = input('Введите вашу фамилию - ')
height = int(input('Введите ваш рост - '))
weight = int(input('Введите ваш вес - '))

# Перевод роста к нужному виду
height = height / 100

# Расчет BMI
bmi = round(weight / (height ** 2), 2)

if bmi < 16:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас выраженный дефицит массы')
elif bmi >= 16 and bmi <= 18.5:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас недостаточная масса тела')
elif bmi > 18.5 and bmi <= 24.99:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас нормальная масса тела')
elif bmi > 25 and bmi <= 30:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас избыточная масса тела (предожирение)')
elif bmi > 30 and bmi <= 35:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас ожирение 1й степени')
elif bmi > 35 and bmi <= 40:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас ожирение 2й степени')
elif bmi > 40:
    print(name, surname, 'ваш индекс массы тела = ', bmi, 'У вас ожирение 3й степени')

print('Следи за собой, будь осторожен!')
