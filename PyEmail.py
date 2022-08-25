from email.message import EmailMessage
import smtplib
import mimetypes
import ssl
from os import path

class PyEmail:
    def __init__(self,sender,ePass):
        """Class initialize with sender's email and password"""
        self.sender = sender
        self.ePass = ePass
        self.msg = EmailMessage()
    
    def writePlainText(self,reciever, SUBJECT, BODY,cc = None):
        """Function expects the recipient's email or list[] of emails, Subject and Body. CC is set to none by default and follow the same format as recipient."""
        self.msg['FROM'] = self.sender
        if type(reciever) == list:
            self.msg['To'] = ", ".join(reciever)
        else:
            self.msg['To'] = reciever
        if cc != None:
            if type(cc) == list:
                self.msg['CC'] = ", ".join(cc)
            else:
                self.msg['CC'] = cc
        self.msg['Subject'] = SUBJECT
        self.msg.set_content(BODY)

    
    def addAttachments(self,file):
        """Adds a single file to email. Expects a single raw file path."""
        if path.exists(file):
            ctype, encoding = mimetypes.guess_type(file)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            with open(file,'rb') as c_f:
                content = c_f.read()
                maintype, subtype = ctype.split('/', 1)
                _, tail = path.split(file)
                self.msg.add_attachment(content,
                            maintype=maintype,
                            subtype =subtype,
                            filename = tail)
        else:
            print("File: " + file + " could not be found.")
        
    def sendMail(self):
        """Sends email to recipient"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(self.sender,self.ePass)
            smtp.sendmail(self.sender,self.msg['To'],self.msg.as_string())


