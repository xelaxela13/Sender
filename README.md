# Sender
Simple python module for sending emails

Waiting params:
    :param host: string
    :param sender: string - sender email
    :param recipients: string - recipients email
    :param subject: string
    :param massage: string
    :param username: string - username from email server
    :param password: string - password
    :param port: int - 25 (default), 465 gmail ssl, 587 gmail ttl, or your any port
    :param ssl: bool - False (default)
    :param debug: bool - False (default)
    :param log_file: string - None (default), use '/var/log/sender.log' if you want create log file
    :return: True

Example:
<code>from sender import Sender</code>

<code>param = ['smtp.gmail.com',
         'from@gmail.com',
         'to@gmail.com',
         'Subject',
         'My perfect text',
         'username',
         'password',
         465,
         True,
         True,
         'sender.log']</code>
<code>sender = Sender()</code>
<code>sender.send_email(*param)</code>

