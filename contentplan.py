import os
import calendar
from datetime import date
import tkinter as tk
from tkinter import messagebox

def generate_content_plan():
    content_plan_folder = "Контент план"
    os.makedirs(content_plan_folder, exist_ok=True)
    
    months = [
        "Январь", "Февраль", "Март", "Апрель",
        "Май", "Июнь", "Июль", "Август",
        "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]
    
    days = [
        "Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"
    ]

    for month in range(1, 13):
        month_name = months[month - 1]
        month_folder = os.path.join(content_plan_folder, month_name)
        os.makedirs(month_folder, exist_ok=True)
        
        _, last_day = calendar.monthrange(date.today().year, month)
        for day in range(1, last_day + 1):
            current_date = date(date.today().year, month, day)
            day_name = days[current_date.weekday()]
            day_folder_name = f"{current_date.strftime('%d-%m-%Y')} - {day_name}"
            day_folder = os.path.join(month_folder, day_folder_name)
            os.makedirs(day_folder, exist_ok=True)
            
            article_file = os.path.join(day_folder, "Статья.txt")
            with open(article_file, "w", encoding="utf-8") as f:
                f.write("Здесь ваша статья")
    
    messagebox.showinfo("Генерация завершена", "Генерация контент плана завершена.")

# Создание главного окна
root = tk.Tk()
root.title("Генератор контент плана")

# Установка размеров окна
root.geometry("200x200")

# Создание кнопки для запуска генерации и размещение с помощью grid
generate_button = tk.Button(root, text="Сгенерировать контент план", command=generate_content_plan)
generate_button.grid(row=1, column=1, padx=10, pady=10)

# Создание кнопки для выхода из программы и размещение с помощью grid
exit_button = tk.Button(root, text="Выход", command=root.quit)
exit_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
