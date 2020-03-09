from ftplib import FTP

ftp = FTP(
    "192.168.83.74",
    "pi",
    passwd="raspberry"
)

d = ftp.dir("./")
print(d)
