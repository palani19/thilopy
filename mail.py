import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pthilothy@gmail.com", "password")
msg = "Hiiiiiiiii!"
server.sendmail("pthilothy@gmail.com", "poojitha202@gmail.com", msg)
server.quit()

