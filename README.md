# Email Automation In Python

Email Automation makes the process of sending information easy and less arduous.

So, to implement this approach, we are going to follow the procedure mentioned below:

1. Configuring Gmail Account Settings
2. Loading the Dependencies required.
3. Creating a mail object using MIMEMultipart.
4. Sending the mail through smtplib.
5. Process of Email Automation

## Configuring Gmail Account Settings

1. Login to your Gmail Account.

2. Further, go to the top right and click on the Manage your Google Account option.
![image](https://drive.google.com/uc?export=view&id=1szkVCn7EaVhqqMOQ0-lhkYedv5JgRCxH)

3. Then click on the Security Tab in the Menu Bar present on the left side of the webpage.
![image](https://drive.google.com/uc?export=view&id=1gMnpfwHJpaZRgyhrpNPD17f4TxioriT_)

4. After that, scroll to the option “Signing in to Google” and turn off both the options. (Use your phone to sign in and 2-Step Verification)
![image](https://drive.google.com/uc?export=view&id=1NDq86j1eQ5kkmHTBHBlLWcBpFuMx29iu)

5. Now scroll further down to the option “Less secure app access” and turn this option on.
![image](https://drive.google.com/uc?export=view&id=1CgSrnwE3XGQ0ZClGjuscjzdHaiWPxlo6)


## Loading the Required Libraries
The smtplib (Simple Mail Transfer Protocol Library) is a python module used in sending basic emails. In other words, emails consisting of only text body without any subject or any attachments.

If we want to send an email having a subject or any attachment, we will have to use smtplib in combination with email module.

We will be importing :

* smtplib module
* MIMEMultipart module from email.mime.multipart
* MIMEText module from email.mime.text

```
# Loading all the packages required
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
```

## Creating a mail object using MIMEMultipart
After importing the required modules, we create a class ‘EmailAutomation’. Subsequently, we declare and initialize variables in the constructor which would store the:

* User’s Email Address
* User’s Account Password
* Receiver’s Email Address
* The subject of the Email

The next step is to call the build method of the class.

```
class EmailAutomation:
    def __init__(self, user_mail, password, receiver_mail, subject):
        # Declaring and Initializing the User's Mail ID, 
        # User's Password, Receiver's Mail ID and Subject of the mail
        self.user_mail = user_mail
        self.password = password
        self.receiver_mail = receiver_mail
        self.subject = subject
        
        # Calling the Build Method
        self.build()
```

In the build method, we firstly create a MIMEMultipart object. After that, we assign the ‘From’ email address, ‘To’ email address, and ‘Subject’ content-type headers as a keyword dictionary.

In the next step, we read the body of the email (message to be sent) through a text file and we store it in the ‘body’ variable. After that, we attach the body to the MIMEMultipart object as plain text using MIMEText module. Then, we call the send method of the class.

```
class EmailAutomation:
        
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
```

## Sending the mail through smtplib
At the penultimate step, we create an object of SMTP in the send method which encapsulates an SMTP connection. Then, we pass the host address and a port number as parameters to the object.

In our case, Gmail’s SMTP host address is smtp.gmail.com and the port number for TLS connection is 587.

After that, we start a TLS connection and then log in using the user email address and password specified in the instance variables. Then, we send the email using the ‘send_message()’ method and lastly, we terminate and close the SMTP connection.

```
class EmailAutomation:
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
```

## Process of Email Automation
To completely automate the process of sending emails, we can put up an If the condition on the basis of which we can trigger the instantiation of the object of the EmailAutomation class which in turn would send the automated mail to the destination email address.

```
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
```

## Input Text File:

```
Hello!
This is a test email.
This email is sent through a python script.
```

## Ouput:
![image](https://drive.google.com/uc?export=view&id=1aNOZgRWUxV6RjQaAjPKlwWpNNQHAw-Et)
