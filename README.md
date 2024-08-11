# E-Library

Deskripsi singkat tentang E-Library.

## Prerequisites

- Python 3.10+
- pip
- Virtualenv (opsional)

## Installation

1. Clone repositori:
    ```bash
    git clone https://github.com/mluqi/online-test-ciheultech-3.git
    cd repository
    ```

2. Buat lingkungan virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Instal dependensi:
    ```bash
    pip install -r requirements.txt
    ```
    
4. Pindah ke direktori elibrary
    cd ./elibrary

5. Jalankan migrasi:
    ```bash
    python manage.py migrate
    ```

6. Jalankan server pengembangan:
    ```bash
    python manage.py runserver
    ```

7. Akses aplikasi di `http://127.0.0.1:8000/`

## License

mluqi12@gmail.com
