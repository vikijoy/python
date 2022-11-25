# Задача 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 

# Задача 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            left = not (x or y or z)
            right = not x and not y and not z
            result = left == right
            if result == True:
                print(f"X = {x}, Y = {y}, Z = {z}. ¬(X ⋁ Y ⋁ Z) = {not (x or y or z)}. ¬X ⋀ ¬Y ⋀ ¬Z = {not x and not y and not z}. Утверждение истинно")
            else:
                print(f"X = {x}, Y = {y}, Z = {z}. ¬(X ⋁ Y ⋁ Z) = {not (x or y or z)}. ¬X ⋀ ¬Y ⋀ ¬Z = {not x and not y and not z}. Утверждение ложно")