import challenge_11

conn = challenge_11.get_conection()
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM users")

result_list = cursor.fetchall()
print(result_list)

# not execute this program mysql comand 
cursor.execute(
    "INSERT INTO users (name) VALUES (%S)",
    ("rahul",)
)
conn.commit

cursor.close
conn.close
