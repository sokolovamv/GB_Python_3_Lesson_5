# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция  возвращает кортеж из трех элементов: путь, имя файла, расширение файла

def path_to_file(in_link: str) -> tuple:
    *path, original_file = in_link.split('/')
    name_of_file, file_extension = original_file.split('.')
    return '/'.join(path), name_of_file, file_extension

print(path_to_file('/Users/vladislav/Desktop/Masha/GB/Python_3/Lesson5/task_1.py'))