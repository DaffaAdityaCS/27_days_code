import smtplib
from getpass import getpass
import stdiomask

def send_email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    login_id = input(str("Enter Email: "))
    login_pass = stdiomask.getpass("Enter password: ")

    server.login(login_id, login_pass)
    email_receiver = input(str("Email Receiver: "))
    massage = input(str("Massage: "))
    server.sendmail(login_id, email_receiver, massage)


send_email()
