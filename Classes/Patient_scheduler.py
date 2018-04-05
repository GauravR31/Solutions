import datetime

class Patient(object):
	"""docstring for ClassName"""
	def __init__(self, p_id, name, app_time):
		self.p_id = p_id
		self.name = name
		self.app_time = app_time

class Doctor(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.p_list = []

	def schedule_patient(self, p_id):
		p = Patient(0, "", "")
		p.p_id = p_id
		p.name = raw_input("Enter your name ")
		mins = (p_id * 30)
		p.app_time = datetime.time(9+(mins/60), (mins%60))
		self.p_list.append(p)

	def view_patients(self):
		for p in self.p_list:
			print("ID : {}\nName : {}\nTime : {}".format(p.p_id, p.name, p.app_time))

def main():
	p_count = 0
	d = Doctor()

	while True:
		print("1. Schedule a patient\n2. View patients\n3. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			if p_count > 15:
				print("No appointments available today!")
				break

			d.schedule_patient(p_count)
			p_count += 1

		elif ch == 2:
			d.view_patients()

		elif ch == 3:
			break

		else:
			print("Invalid choice!")

if __name__ == '__main__':
	main()




		
		
		