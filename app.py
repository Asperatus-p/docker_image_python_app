import os
import sys
from datetime import datetime

# Задаем путь. Если закомментировано, используется корневой каталог.
# path = "/some/custom/directory"  # Uncomment and set your custom path here
path = "/"


def get_file_list(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                file_size = os.path.getsize(file_path)
                file_list.append((file_size, file_path))
            except OSError:
                pass  # Ignore files that cannot be accessed
    return file_list


def main():
    # Проверяем аргументы командной строки
    if len(sys.argv) >= 2:
        user_name = sys.argv[1]
    else:
        user_name = "User"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Приветствие
    print(f"Привет, {user_name}!")
    print(f"Текущая дата и время: {current_time}\n")

    # Получаем список файлов и их размеры
    file_list = get_file_list(path)

    # Количество файлов
    num_files = len(file_list)
    print(f"Количество файлов в каталоге '{path}': {num_files}\n")

    # Сортируем список файлов по размеру (в порядке убывания)
    file_list.sort(reverse=True, key=lambda x: x[0])

    # Выводим топ-10 файлов по размеру
    print("Топ-10 файлов по размеру (в Кб):")
    for i, (size, file_path) in enumerate(file_list[:10]):
        print(f"{i + 1}. {file_path} - {size / 1024:.2f} Кб")


if __name__ == "__main__":
    main()

