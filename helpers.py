import random
import data

# генерация номера телефона
def generated_phone():
    generated_phone = '+7'+str(random.randint(1000000000,9999999999))
    return generated_phone

# генерация строки (имени/фамилии/адреса)
def generated_str(list):
    generated_str = random.choice(list)
    return generated_str

# генерация номера станции метро
def generated_metro():
    generated_metro = str(random.randint(1,112))
    return generated_metro

# генерация числа даты
def generated_date():
    generated_date = str(random.randint(1,30))
    if len(generated_date) == 1:
        zero = '00'
    else:
        zero = '0'
    return zero+str(generated_date)

# генерация срока аренды
def generated_occupancy():
    generated_occupancy = random.choice(data.RENTAL_PERIOD)
    return generated_occupancy
