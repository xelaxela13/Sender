# Sender
Simple python module for sending emails

import sender

param = ['smtp.gmail.com',
         'from@gmail.com',
         'to@gmail.com',
         'Subject',
         '<H1>My perfect text</H1>',
         'username',
         'password',
         465,
         True,
         True,
         True]
sender.send_email(*param)
