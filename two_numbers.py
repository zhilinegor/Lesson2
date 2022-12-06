import math

def inp_num_1(): # проверка ввода

    while True:
        
        try:
            num1 = float(input("\nВведите первое число: "))
            return num1
            break
            
        except ValueError:
            print("\nВы должны ввести число, попробуйте снова.")
            

def inp_num_2(): # проверка ввода
    while True:
        try:
            num2 = float(input("\nВведите второе число: "))
            return num2
            break
        except ValueError:
            print("\nВы должны ввести число, попробуйте снова.")
numb1 = inp_num_1()
numb2 = inp_num_2()

print("\nСумма чисел: ", numb1 + numb2)
print("\nРазность чисел: ", numb1 - numb2)
print("\nПроизведение чисел: ", numb1 * numb2)
print("\nЧастное чисел: ", numb1 / numb2)
print("\n",numb1 ,"в степени", numb2,": ", numb1 ** numb2)
print("\n",numb2 ,"в степени", numb1,": ", numb2 ** numb1)
print("\n",numb1 ,"по модулю", numb2,": ", numb1 % numb2)
print("\n",numb2 ,"по модулю", numb1,": ", numb2 % numb1)
print("\nЧастное по модулю: ", numb1 % numb2)
print("\nЧастное целочисленное: ", numb1 % numb2)


