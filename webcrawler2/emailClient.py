import smtplib, ssl

class EmailClient():
    def __init__(self):
        self.__smtp_server = "smtp.gmail.com"
        self.__port = 587  # For starttls
        self.__sender_email = "swagifywebscrapererrors@gmail.com"
        self.__receiver_email = "swagifywebscrapererrors@gmail.com"
        self.__password = "syde322!"
        # Create a secure SSL context
        self.__context = ssl.create_default_context()

    def sendMessage(self, message):
        try:
            server = smtplib.SMTP(self.__smtp_server,self.__port)
            server.ehlo() # Can be omitted
            server.starttls(context=self.__context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, self.__receiver_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 
    