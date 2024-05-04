import socket

response = 'Y'
while response=='Y':
    url = input("Type a URL:")
    ip = socket.gethostbyname(url)
    print("The reference IP of passed URL is:", ip)
    response=input("Type <Y> to continue:").toUpper()