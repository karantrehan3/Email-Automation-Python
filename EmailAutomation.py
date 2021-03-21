# Loading all the packages required
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailAutomation:

    def __init__(self, user_mail, password, receiver_mail, subject):
        # Declaring and Initializing the User's Mail ID, User's Password, Receiver's Mail ID and Subject of the mail
        self.user_mail = user_mail
        self.password = password
        self.receiver_mail = receiver_mail
        self.subject = subject

        # Calling the Build Method
        self.build()

    def build(self):
        # Creating a Message and setting up the Headers
        mail = MIMEMultipart()
        mail['From'] = self.user_mail
        mail['To'] = self.receiver_mail
        mail['Subject'] = self.subject

        # Reading the Body of the E-mail to be sent from a text file
        textfile = 'textfile.txt'
        with open(textfile) as fp:
            body = fp.read()

        # Attaching body to the mail
        mail.attach(MIMEText(_text=body, _subtype='plain'))

        # Calling the Send Method
        self.send(mail)

    def send(self,mail):
        # Setting up the SMTP (Simple Mail Transfer Protocol) server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)

        # Putting the SMTP connection in TLS (Transport Layer Security) mode.
        # All SMTP commands that follow will be encrypted.
        server.starttls()

        # Logging in to the SMTP server
        server.login(user=self.user_mail, password=self.password)

        # Sending the mail
        server.send_message(from_addr=self.user_mail, to_addrs=self.receiver_mail, msg=mail)

        # Terminating the SMTP session and closing the connection
        server.quit()


if __name__ == '__main__':
    """
    To automate the process of sending emails, we can put up an If 
    condition on the basis of which we can trigger the instantiation of
    the object of the EmailAutomation class which in turn would send the
    automated mail to the destination email address.
    """
    
    # The condition below can be altered based on the requirements
    if True:
        email_object = EmailAutomation('YOUR EMAIL ADDRESS HERE',
                                       'YOUR PASSWORD HERE',
                                       'RECEIVER EMAIL ADDRESS HERE',
                                       'SUBJECT OF THE EMAIL')
        
