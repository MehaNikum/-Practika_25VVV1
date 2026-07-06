import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import random
import time
from selection_sort import selection_sort
from file_io import read_csv, write_csv, write_results

class App:
    def __init__(self, root):
        self.root = root
        root.title("Сортировка выбором")
        root.geometry("800x600")

        # Переменные
        self.arr = []
        self.sorted_arr = []
        self.comparisons = 0
        self.swaps = 0
        self.elapsed = 0.0
        self.std_elapsed = 0.0
        self.is_sorted = False

        # Фреймы
        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)
        mid_frame = tk.Frame(root)
        mid_frame.pack(pady=5)
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(pady=5)

        # Генерация
        tk.Label(top_frame, text="Размер:").grid(row=0, column=0, padx=5)
        self.size_entry = tk.Entry(top_frame, width=10)
        self.size_entry.grid(row=0, column=1, padx=5)
        self.size_entry.insert(0, "10")

        tk.Label(top_frame, text="Мин:").grid(row=0, column=2, padx=5)
        self.min_entry = tk.Entry(top_frame, width=10)
        self.min_entry.grid(row=0, column=3, padx=5)
        self.min_entry.insert(0, "0")

        tk.Label(top_frame, text="Макс:").grid(row=0, column=4, padx=5)
        self.max_entry = tk.Entry(top_frame, width=10)
        self.max_entry.grid(row=0, column=5, padx=5)
        self.max_entry.insert(0, "100")

        self.gen_btn = tk.Button(top_frame, text="Сгенерировать", command=self.generate)
        self.gen_btn.grid(row=0, column=6, padx=5)

        self.load_btn = tk.Button(top_frame, text="Загрузить из CSV", command=self.load)
        self.load_btn.grid(row=0, column=7, padx=5)

        self.save_btn = tk.Button(top_frame, text="Сохранить в CSV", command=self.save_csv)
        self.save_btn.grid(row=0, column=8, padx=5)

        # Массивы
        tk.Label(mid_frame, text="Исходный массив:").grid(row=0, column=0, sticky="w")
        self.orig_text = scrolledtext.ScrolledText(mid_frame, width=60, height=8)
        self.orig_text.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(mid_frame, text="Отсортированный массив:").grid(row=0, column=1, sticky="w")
        self.sorted_text = scrolledtext.ScrolledText(mid_frame, width=60, height=8)
        self.sorted_text.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка сортировки
        self.sort_btn = tk.Button(mid_frame, text="Выполнить сортировку", command=self.sort)
        self.sort_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Статистика
        self.stats_label = tk.Label(mid_frame, text="Статистика: ожидание...")
        self.stats_label.grid(row=3, column=0, columnspan=2, pady=5)

        # Сохранение отчёта
        self.save_report_btn = tk.Button(mid_frame, text="Сохранить отчёт", command=self.save_report, state=tk.DISABLED)
        self.save_report_btn.grid(row=4, column=0, columnspan=2, pady=5)
    def generate(self):
        try:
            size = int(self.size_entry.get())
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())
            if size <= 0:
                messagebox.showerror("Ошибка", "Размер должен быть положительным.")
                return
            if min_val > max_val:
                messagebox.showerror("Ошибка", "Минимум не может быть больше максимума.")
                return
            self.arr = [random.randint(min_val, max_val) for _ in range(size)]
            self.display_array(self.arr, self.orig_text)
            self.sorted_text.delete(1.0, tk.END)
            self.stats_label.config(text="Статистика: массив сгенерирован, сортировка не выполнена")
            self.is_sorted = False
            self.save_report_btn.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные целые числа.")

    def load(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not filename:
            return
        arr = read_csv(filename)
        if arr is None:
            messagebox.showerror("Ошибка", "Не удалось прочитать файл или неверный формат.")
            return
        if len(arr) == 0:
            messagebox.showwarning("Предупреждение", "Файл пуст.")
        self.arr = arr
        self.display_array(self.arr, self.orig_text)
        self.sorted_text.delete(1.0, tk.END)
        self.stats_label.config(text="Статистика: массив загружен, сортировка не выполнена")
        self.is_sorted = False
        self.save_report_btn.config(state=tk.DISABLED)

    def save_csv(self):
        if not self.arr:
            messagebox.showerror("Ошибка", "Нет данных для сохранения.")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not filename:
            return
        if write_csv(filename, self.arr):
            messagebox.showinfo("Успех", f"Массив сохранён в {filename}")
        else:
            messagebox.showerror("Ошибка", "Не удалось сохранить файл.")
    def sort(self):
        if not self.arr:
            messagebox.showerror("Ошибка", "Массив пуст.")
            return
        # Собственная сортировка
        start = time.perf_counter()
        self.sorted_arr, self.comparisons, self.swaps = selection_sort(self.arr)
        self.elapsed = time.perf_counter() - start

        # Стандартная сортировка
        start = time.perf_counter()
        _ = sorted(self.arr)
        self.std_elapsed = time.perf_counter() - start

        self.display_array(self.sorted_arr, self.sorted_text)
        self.stats_label.config(
            text=f"Сравнений: {self.comparisons}, Перестановок: {self.swaps}, "
                 f"Время (собств.): {self.elapsed:.6f} с, Время (sorted): {self.std_elapsed:.6f} с"
        )
        self.is_sorted = True
        self.save_report_btn.config(state=tk.NORMAL)

    def save_report(self):
        if not self.is_sorted:
            messagebox.showerror("Ошибка", "Сначала выполните сортировку.")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not filename:
            return
        if write_results(filename, self.arr, self.sorted_arr, self.comparisons, self.swaps, self.elapsed, self.std_elapsed):
            messagebox.showinfo("Успех", f"Отчёт сохранён в {filename}")
        else:
            messagebox.showerror("Ошибка", "Не удалось сохранить отчёт.")

    def display_array(self, arr, widget):
        widget.delete(1.0, tk.END)
        if len(arr) > 0:
            widget.insert(tk.END, ' '.join(str(x) for x in arr))
        else:
            widget.insert(tk.END, "(пусто)")

def run_gui():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
