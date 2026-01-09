import sqlite3
# ---- zadanie 1 ----
conn = sqlite3.connect("chinook.db")
print("Polaczenie jest gotowe")
# ---- --------- ----

# ---- zadanie 2 ----
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(cur.fetchall())
# ---- --------- ----

# ---- zadanie 3 ----
cur.execute("PRAGMA table_info(customers);")
#print(cur.fetchall())
# ---- zadanie 3 ----

# ---- zadanie 4 ----
cur.execute("SELECT * from customers;")
rows = cur.fetchall()
#for row in rows[:5]: # tylko pierwsze 5 wywodow
#    print(row)
# ---- --------- ----

# ---- zadanie 5 ----
cur.execute("SELECT firstname, lastname from customers;")
rows = cur.fetchall()
for row in rows[:5]: # tylko pierwsze 5 wywodow
    print(row)


conn.close()