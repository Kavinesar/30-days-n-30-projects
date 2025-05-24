import smtplib

email = "sender email"
receiver_email = input("receiver email: ") 

subject = input("sub: ")
message = input("msg: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "google app password ")

server.sendmail(email, receiver_email, text)

print("email sent to " + receiver_email)
