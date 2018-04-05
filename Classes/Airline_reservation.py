class AirlineTicket(object):
	"""docstring for AirlineTicket"""
	def __init__(self, passenger_name, ticket_no, ticket_class, price):
		self.passenger_name = passenger_name
		self.ticket_no = ticket_no
		self.ticket_class = ticket_class
		self.price = price

	def display_ticket(self):
		print("Name : {}\nTicket No : {}\nClass : {}\nPrice: {}".format(self.passenger_name, 
			self.ticket_no, self.ticket_class, self.price))

class Reservation(object):
	"""docstring for Reservation"""
	def __init__(self):
		self.no = 0
		self.list = []

	def book(self):
		name = raw_input("Enter the passenger's name ")
		self.no += 1
		c = input("1. First-class\n2. Economy ")
		if c == 1:
			t_class = "First"
			price = 10000
		elif c == 2:
			t_class = "Eco"
			price = 8000
		else:
			print("Invalid entry")
			t_class = "None"
			price = 0

		ticket = AirlineTicket(name, self.no, t_class, price)

		if ticket.ticket_class != "None":
			print("Booking confirmed!")
			ticket.display_ticket()
			self.list.append(ticket)

		else:
			print("No ticket booked")

	def upgrade(self):
		num = input("Enter the ticket number ")
		name = raw_input("Enter the passenger name ")
		flag = 0

		for tick in self.list:
			if tick.ticket_no == num and tick.passenger_name == name:
				flag = 1
				if tick.ticket_class == "Eco":
					tick.ticket_class = "First"
					print("You have been upgraded successfully!")
				else:
					print("You are already in First Class")

		if flag == 0:
			print("Invalid ticket number or passenger name!")

	def cancel(self):
		num = input("Enter the ticket number ")
		name = raw_input("Enter the passenger name ")
		flag = 0

		for tick in self.list:
			if tick.ticket_no == num and tick.passenger_name == name:
				flag = 1
				self.list.remove(tick)

		if flag == 0:
			print("Invalid ticket number or passenger name!")

	def view(self):
		for tick in self.list:
			tick.display_ticket()

def main():
	reserve = Reservation()

	while True:
		print("1. Book a ticket\n2. Upgrade your ticket\n3. Cancel your ticket\n4. View current bookings\n5. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			reserve.book()

		elif ch == 2:
			reserve.upgrade()

		elif ch == 3:
			reserve.cancel()

		elif ch == 4:
			reserve.view()

		elif ch == 5:
			break

		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()

		
		
	