# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def pass_parsing(the_pass: str)->tuple:
    *a, b = the_pass.split("\\")
    a = '\\'.join(a)
    *c, d = b.split('.')
    c = ' '.join(c)
    return (a, c, d)

res = pass_parsing("E:\Информационные технологии\Tecknological_specialization\Data_ingineer\Python\Seminar 5. Итераторы и генераторы.mp4")
print(*res, sep='\n')