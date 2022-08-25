from PyEmail import PyEmail

if __name__ == "__main__":
    #
    test = PyEmail('a*******@gmail.com','****************')
    test.writePlainText('a******@outlook.com','Test Script','Hi This is an automated test message')
    test.addAttachments(r"filepath")
    test.sendMail()
    pass