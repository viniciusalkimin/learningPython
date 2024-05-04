from ftplib import *

ftp = FTP('ftp.ibiblio.org')

user=input("type username: ")
password=input("type password: ")

ftp.login()
print("Your localpath: ", ftp.pwd())

ftp.cwd('pub')

print("Actual directory: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()