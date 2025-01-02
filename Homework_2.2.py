# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число. Вам необхідно "перевернути" цє число
# задом наперед, тобто щоб у результаті вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.

# Вам не потрібно перевіряти, що користувач ввів правильне число - зробіть вигляд, що користувач завжди вводить
#  5 значне число. Тобто введене користувачем число завжди складатиметься з 5 цифр.

# Якщо користувач ввів інше число, це проблема користувача, а не вашої програми.

# Використовуються лише цілі числа.

# Для розв'язання задачі потрібно використовувати лише той зріз даних, який було пройдено.
# Тобто використовувати строки не можна.

while True:
    try:
        entered_number = int(input("Enter a 5-digit positive integer: "))

        if 10000 <= entered_number <= 99999:
            break
        else:
            print("Error: Enter exactly a 5-digit positive integer.")
    except ValueError:
        print("Error: Enter a valid number without letters, spaces, or symbols.")

list_of_entered_numbers = []
for _ in range(5):
    list_of_entered_numbers.append(entered_number % 10)
    entered_number //= 10

reversed_number = 0
for digit in list_of_entered_numbers:
    reversed_number = reversed_number * 10 + digit

print("Reversed number: ", reversed_number)
