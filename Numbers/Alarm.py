import time, pygame

pygame.init()
pygame.mixer.init()

n = input("Enter time in seconds ")

def main():
	pygame.mixer.music.load("0897.wav")
	time.sleep(n)
	pygame.mixer.music.play()
	time.sleep(5)

if __name__ == '__main__':
	main()
