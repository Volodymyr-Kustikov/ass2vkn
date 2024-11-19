def all_to_decimal(hexadecimal_string, number):
    return int(hexadecimal_string, number)
  
def convert_number():
    while True:
        
        user_input = input("Введіть число (десяткове, двійкове з 'x4' або шістнадцяткове з 'x16'): ")
        user_input_binSys = int(input("Введіть число, яке належить системі"))
        
        if 'x' in user_input:  
            binary_number = user_input[-2:]  
            decimal_number = all_to_decimal(binary_number, user_input_binSys)
            print(f" {user_input} дорівнює числу {decimal_number}")
        else:  
                print("Помилка: введіть дійсне десяткове, двійкове або шістнадцяткове число.")
                continue

        user_input_binSys = input("У яку систему перевести число? (двійкова/шістнадцяткова): ").strip().lower()

        # переводжу у ту, котру хочу
        if user_input_binSys == "двійкова":
            binary_number = decimal_to_binary(decimal_number)
            print(f"Число у двійковій системі: 0b{binary_number}")
        elif user_input_binSys == "шістнадцяткова":
            hexadecimal_number = decimal_to_hexadecimal(decimal_number)
            print(f"Число у шістнадцятковій системі: 0x{hexadecimal_number}")
        else:
            print("Незрозуміла система числення. Трай аган.")


        repeat = input("Бажаєте конвертувати ще одне число? (так/ні): ").lower()
        if repeat != 'так':
            print("Си ю лейтер")
            break


convert_number()
