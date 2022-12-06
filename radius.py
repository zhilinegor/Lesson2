import math

def inp_radius(): # проверка ввода

    while True:
        
        try:
            radius = float(input("\nДля вычисления площади круга, введите его радиус: "))
            return radius
            break
            
        except ValueError:
            print("\nВы должны ввести число, попробуйте снова.")

print("\nПлощадь круга:", math.pi * (inp_radius()**2))    