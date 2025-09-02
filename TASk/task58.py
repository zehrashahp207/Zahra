import sqlite3

# 1. Verilənlər bazasına qoşul
conn = sqlite3.connect('example.db')  # 'example.db' adlı fayl yaradılır və ya açılır
cursor = conn.cursor()

# 2. Cədvəl yaratmaq (yeni rəf yaratmaq)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL CHECK (completed IN (0,1))
)
''')

# 3. Yeni tapşırıq əlavə etmək (məlumat qoymaq)
cursor.execute('''
INSERT INTO tasks (title, completed) VALUES (?, ?)
''', ("Məsələn, Python öyrən", False))

# 4. Məlumatları oxumaq (rəfdəki kitabları göstərmək)
cursor.execute('SELECT * FROM tasks')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. Dəyişiklikləri yadda saxlamaq
conn.commit()

# 6. Bağlantını bağlamaq
conn.close()