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
