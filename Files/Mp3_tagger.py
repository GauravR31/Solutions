import mutagen
from mutagen.easyid3 import EasyID3

def main():
	path = raw_input("Enter the path of the file to modify ID3 tags ")
	tag = EasyID3(path)

	while True:
		print("1. Edit title\n2. Edit artist\n3. Edit album\n4. Edit genre\n5. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			title = raw_input("Enter the new title ")
			tag['title'] = title
			tag.save(v2_version=3)
		elif ch == 2:
			artist = raw_input("Enter the new artist ")
			tag['artist'] = artist
			tag.save(v2_version=3)
		elif ch == 3:
			album = raw_input("Enter the new album ")
			tag['album'] = album
			tag.save(v2_version=3)
		elif ch == 4:
			genre = raw_input("Enter the new genre ")
			tag['genre'] = genre
			tag.save(v2_version=3)
		elif ch == 5:
			break
		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()