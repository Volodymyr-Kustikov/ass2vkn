def decimal_to_binary(decimal_number):
    return bin(decimal_number)

def binary_to_decimal(binary_number):
    if(0 and 1 in binary_number):
        return int(binary_number, 2)
    else:
        return "incoreect"



def convert_number():
    while True:
        user_input = input("Введіть число (десяткове або двійкове з префіксом 0b): ")
        if user_input.startswith("0b"):
            
            decimal_result = binary_to_decimal(user_input)
            print(f"Число в десятковому форматі: {decimal_result}")
        else:
            try:
                decimal_number = int(user_input)
                binary_result = decimal_to_binary(decimal_number)
                print(f"Число в двійковому форматі: {binary_result}")
            except ValueError:
                print("Помилка: введено некоректне число. Спробуйте знову.")
                continue

        another = input("Бажаєте перевести ще одне число? (так/ні): ").lower()
        if another != "так":
            print("Окей, бай.")
            break

convert_number()
