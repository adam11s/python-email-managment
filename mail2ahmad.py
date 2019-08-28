# This code developed by Ahmad from Amin & Saeid codes
import smtplib

li = ["a@gmail.com", "b@gmail.com","c@gmail.com"]
details={"a@gmail.com":"nameA","b@gmail.com":"nameB","c@gmail.com":"nameC"}
#sender= "myemail@gmail.com"
sender = input('please enter the sender email:')
#password = "12345"
subject = "This is subject"
password = input('please enter the password:')
if 'gmail' in sender.lower():
    s = smtplib.SMTP('smtp.gmail.com', 587)
elif 'outlook' in sender.lower():
    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.starttls() 
s.login(sender, password) 
for i in range(len(li)):
    b = list(details.values())
    message = "Subject: {}\n\nDear {}\n This is an email with subject which composed by smtplib in python.".format(subject,b[i])
    s.sendmail(sender, li[i], message) 
s.quit() 
