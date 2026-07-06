import csv

def read_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            parts = content.split(',')
            arr = []
            for p in parts:
                p = p.strip()
                if p == '':
                    continue
                try:
                    arr.append(int(p))
                except ValueError:
                    return None
            return arr
    except FileNotFoundError:
        return None
    except Exception:
        return None

def write_csv(filename, arr):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(','.join(str(x) for x in arr))
        return True
    except Exception:
        return False
def write_results(filename, original, sorted_arr, comparisons, swaps, elapsed, std_elapsed):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=== ОТЧЁТ О СОРТИРОВКЕ ===\n\n")
            f.write("Исходный массив:\n")
            f.write(' '.join(str(x) for x in original) + "\n\n")
            f.write("Отсортированный массив:\n")
            f.write(' '.join(str(x) for x in sorted_arr) + "\n\n")
            f.write(f"Количество сравнений: {comparisons}\n")
            f.write(f"Количество перестановок: {swaps}\n")
            f.write(f"Время выполнения собственной реализации: {elapsed:.6f} с\n")
            f.write(f"Время выполнения sorted(): {std_elapsed:.6f} с\n")
        return True
    except Exception:
        return False
