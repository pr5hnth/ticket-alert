import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("mashrajnetflix@gmail.com", "geqsqyjooaesgqvo")
# message to be sent
message = "Test Kafka"
# sending the mail
s.sendmail("mashrajnetflix@gmail.com", "mashrajnetflix@gmail.com", message)
# terminating the session
s.quit()
