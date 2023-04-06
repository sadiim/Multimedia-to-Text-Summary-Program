import sqlite3

def connect():
    conn = sqlite3.connect('data1.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS table1 (Id INTEGER PRIMARY KEY, video_url text, text_url text, sound_url text)")
    conn.commit()
    conn.close()

def insert(video_url, text_url, audio_url):
    conn = sqlite3.connect('data1.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO table1 VALUES (NULL,?,?,?)",
                (video_url, text_url, audio_url))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('data1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM table1")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(idx):
    conn = sqlite3.connect('data1.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM table1 WHERE id=?", (idx,))
    conn.commit()
    conn.close()


connect()
