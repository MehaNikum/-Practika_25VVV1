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
