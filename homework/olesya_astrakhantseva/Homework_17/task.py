import os
import argparse
import re


def search_logs(folder_path, search_text):
    results = []

    # Регулярка выражение для фильтрации строк с координатами
    coordinate_pattern = re.compile(r'\[-?\d+\.\d+,\s*-?\d+\.\d+]')

    # Перебираем все файлы в папке
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                for line_number, line in enumerate(file, 1):
                    # Тут пропускаем строки содержащие координаты
                    if coordinate_pattern.search(line):
                        continue

                    # Ищем текст
                    if search_text in line:
                        words = line.strip().split()
                        start_index = None
                        for i, word in enumerate(words):
                            if search_text.lower() in word.lower():
                                start_index = i
                                break

                        if start_index is None:
                            continue

                        context_start = max(0, start_index - 5)
                        context_end = min(len(words), start_index + len(search_text.split()) + 5)

                        context_words = words[context_start:context_end]
                        context = " ".join(context_words)

                        results.append((file_name, line_number, context))

    return results


def main():
    # Парсер аргументов для командной строки
    parser = argparse.ArgumentParser(description="Программа для анализа логов")
    parser.add_argument("folder", help="Полный путь к папке с логами")
    parser.add_argument("--text", required=True, help="Текст для поиска в логах")

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Ошибка: Папка '{args.folder}' не существует.")
        return

    results = search_logs(args.folder, args.text)

    if results:
        for file_name, line_number, context in results:
            print(f"Файл: {file_name}")
            print(f"Строка: {line_number}")
            print(f"Контекст: {context}\n{'=' * 40}")
    else:
        print(f"Не найдено совпадений для '{args.text}' в логах.")


if __name__ == "__main__":
    main()
