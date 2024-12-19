import random
import matplotlib.pyplot as plt
import time

def generate_array(n, max_value, seed):
    random.seed(seed)  # Inisialisasi generator angka acak dengan seed
    return [random.randint(0, max_value) for _ in range(n)]

def is_unique(arr):
    # Memeriksa apakah semua elemen dalam array unik
    return len(arr) == len(set(arr))

def measure_time(arr):
    start_time = time.time()  # Catat waktu mulai
    is_unique(arr)  # Panggil fungsi is_unique
    return time.time() - start_time  # Hitung waktu yang diperlukan

def main():
    stambuk_last_3_digits = 1  # Ganti dengan digit terakhir stambuk Anda
    max_value = 250 - stambuk_last_3_digits  # Nilai maksimum untuk elemen array
    n_values = [100, 150, 200, 250, 300, 350, 400, 500]  # Ukuran array yang diuji
    seed = 42  # Nilai seed untuk random

    # List untuk menyimpan waktu pengukuran
    worst_case_times = []
    average_case_times = []

    for n in n_values:
        # Lakukan pengukuran waktu sebanyak 10 kali untuk rata-rata dan kasus terburuk
        times = [measure_time(generate_array(n, max_value, seed)) for _ in range(10)]
        worst_case_times.append(max(times))  # Waktu terburuk
        average_case_times.append(sum(times) / len(times))  # Waktu rata-rata
    
    # Plot hasil
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, worst_case_times, label='Worst Case', marker='o')
    plt.plot(n_values, average_case_times, label='Average Case', marker='o')
    plt.xlabel('n (Jumlah Elemen)')
    plt.ylabel('Waktu (Detik)')
    plt.title('Worst Case dan Average Case Waktu untuk Memeriksa Keunikan Elemen')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
