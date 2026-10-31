""" Проект FitLife - MVP версия 1.0 """

ML_TO_LITRE = 1 / 1000
WATER_PER_KG = 30

# 1. Знакомство
user_name = input("Введите ваше имя - ")
user_age = int(input("Укажите ваш возраст - "))

# 2. Сбор данных
user_weight = float(input("Укажите свой вес в килограммах, например: 68.5 - "))
user_height = float(input("Укажите свой рост в метрах, например: 1.68 - "))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_l = water_ml * ML_TO_LITRE

# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("Расчет окончен. Будьте здоровы!")
