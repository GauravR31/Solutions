import os
import zipfile

directory = raw_input("Enter the directory path to zip ")

dir_zip = zipfile.ZipFile('zip_directory.zip', 'w')

if os.path.isdir(directory):
	for folder, subfolders, files in os.walk(directory):
		for file in files:
			dir_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), directory),\
				compress_type = zipfile.ZIP_DEFLATED)

	dir_zip.close()
	print("{} zipped successfully".format(directory))

else:
	print("Directory not found")
