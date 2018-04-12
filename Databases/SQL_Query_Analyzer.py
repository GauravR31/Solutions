import sqlite3

def main():
	conn = sqlite3.connect("myTable.db")
	crsr = conn.cursor()

	while True:
		print("1. Create table\n2. Update table\n3. Read table\n4. Delete table\n5. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			create_query = "CREATE TABLE emp (staff_id INTEGER PRIMARY KEY,\
			fname TEXT NOT NULL,\
			lname TEXT NOT NULL,\
			gender CHAR(1));"

			crsr.execute(create_query)

			conn.commit()

		elif ch == 2:
			s_id = input("Enter the employee id ")
			f_name = raw_input("Enter the employee's first name ")
			l_name = raw_input("Enter the employee's last name ")
			e_gender = raw_input("Enter employee's gender(M/F/O)")

			params = (s_id, f_name, l_name, e_gender)
			update_query = '''INSERT INTO emp (staff_id, fname, lname, gender)
			VALUES (?,?,?,?)'''

			crsr.execute(update_query, params)

			conn.commit()

		elif ch == 3:
			read_query = "SELECT * FROM emp"

			crsr.execute(read_query)

			ans = crsr.fetchall()

			for i in ans:
				print i

		elif ch == 4:
			drop_query = "DROP TABLE emp;"

			crsr.execute(drop_query)
			
			conn.commit()

		elif ch == 5:
			conn.close()
			break

		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()