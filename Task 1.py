def total_salary(path):
    try:
        with open(path, "r", encoding= "utf-8") as file:
            salaries = []
            for line in file:
                name,salary = line.strip().split(",")
                salaries.append(int(salary))
        total = sum(salaries)
        averadge = total/len(salaries)if salaries else 0

        return total, averadge

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



