def get_cats_info(path):
    cats = []
    try:
        # Відкриваємо файл з менеджером контексту
        with open(path, 'r', encoding='utf-8') as file:
            # Зчитуємо кожен рядок у файлі
            for line in file:
                try:
                    # Розділяємо рядок на id, name та age
                    cat_id, name, age = line.strip().split(',')
                    # Створюємо словник для кожного кота і додаємо його до списку
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    # Якщо рядок некоректний (наприклад, неправильний формат)
                    print(f"Некоректні дані в рядку: {line.strip()}")
                    
        return cats

    except FileNotFoundError:
        # Обробка випадку, коли файл не знайдено
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        # Обробка інших можливих винятків
        print(f"Сталася помилка: {e}")
        return []

# Приклад використання функції:
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
