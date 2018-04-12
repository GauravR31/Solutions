import turtle

def main():
	turtle.bgcolor("black")
	turtle.color("white")
	steps = 0

	while True:
		print("1. Move forward\n2. Move back\n3. Move right\n4. Move left\n5. Set position\n6. Make circle\
			\n7. Make stamp\n8. Delete stamp\n9. Get current positon\n10. Clear\n11. Exit")

		ch = input("Enter your choice ")

		if ch == 1:
			steps = input("Enter steps to go forward ")
			turtle.forward(steps)
		elif ch == 2:
			steps = input("Enter steps to go back ")
			turtle.backward(steps)
		elif ch == 3:
			angle = input("Enter angle to turn right ")
			turtle.right(steps)
		elif ch == 4:
			angle = input("Enter angle to turn left ")
			turtle.left(steps)
		elif ch == 5:
			x, y = input("Enter co-ordinates(x,y) to move the turtle to ")
			turtle.goto(x, y)
		elif ch == 6:
			radius = input("Enter radius for circle ")
			turtle.circle(radius)
		elif ch == 7:
			s_id = turtle.stamp()
			print s_id
		elif ch == 8:
			s_id = input("Enter the stamp id to delete ")
			turtle.clearstamp(s_id)
		elif ch == 9:
			x,y = turtle.pos()
			print(x,y)
		elif ch == 10:
			turtle.clear()
		elif ch == 11:
			break
		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()