from ftplib import FTP
ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('//specific location/') # cwd stands for current working directory

def grabFile():
    filename = 'filename.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filema,e , localfile.write, 1024) #1024 is buffer. shows the speed of transfer.
    ftp.quit()
    localfile.close()
def placeFile():
    fileName = 'filename.txt'
    ftp.storbinary( 'STOR' + filename, open(filename, 'rb'))
    ftp.quit()
