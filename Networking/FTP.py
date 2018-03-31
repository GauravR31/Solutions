import ftplib

ftp = ftplib.FTP('ftp.novell.com', 'anonymous', 'b@n.com')
print "File list: "
files = ftp.dir()
print files

ftp.cwd('/pub')
file = open('readme.txt', 'wb')
ftp.retrbinary('RETR readme', file.write)
file.close()
ftp.quit()

file1 = open("readme.txt", 'r')
buff = file1.read()
print buff
file1.close()