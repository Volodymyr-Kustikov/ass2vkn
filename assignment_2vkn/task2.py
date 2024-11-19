
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]  

def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:]

def binary_to_decimal(binary_string):
    
    return int(binary_string, 2) 


def hexadecimal_to_decimal(hexadecimal_string):
    return int(hexadecimal_string, 16)


def convert_number():
    while True:
        
        user_input = input("Введіть число (десяткове, двійкове з '0b' або шістнадцяткове з '0x'): ")
        
        if user_input.startswith("0b"):  
            binary_number = user_input[2:]  
            decimal_number = binary_to_decimal(binary_number)
            print(f"Двійкове число {user_input} дорівнює десятковому числу {decimal_number}")
        elif user_input.startswith("0x"):  
            hexadecimal_number = user_input[2:]  
            decimal_number = hexadecimal_to_decimal(hexadecimal_number)
            print(f"Шістнадцяткове число {user_input} дорівнює десятковому числу {decimal_number}")
        else:  
            try:
                decimal_number = int(user_input)  
            except ValueError:
                print("Помилка: введіть дійсне десяткове, двійкове або шістнадцяткове число.")
                continue

        users_system = input("У яку систему перевести число? (двійкова/шістнадцяткова): ").strip().lower()

        # переводжу у ту, котру хочу
        if users_system == "двійкова":
            binary_number = decimal_to_binary(decimal_number)
            print(f"Число у двійковій системі: 0b{binary_number}")
        elif users_system == "шістнадцяткова":
            hexadecimal_number = decimal_to_hexadecimal(decimal_number)
            print(f"Число у шістнадцятковій системі: 0x{hexadecimal_number}")
        else:
            print("Незрозуміла система числення. Трай аган.")


        repeat = input("Бажаєте конвертувати ще одне число? (так/ні): ").lower()
        if repeat != 'так':
            print("Си ю лейтер")
            break


convert_number()
