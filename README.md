# Sender
Simple python module for sending emails

Waiting params:<br>
    :param host: string<br>
    :param sender: string - sender email<br>
    :param recipients: string - recipients email<br>
    :param subject: string<br>
    :param massage: string<br>
    :param username: string - username from email server<br>
    :param password: string - password<br>
    :param port: int - 25 (default), 465 gmail ssl, 587 gmail ttl, or your any port<br>
    :param ssl: bool - False (default)<br>
    :param debug: bool - False (default)<br>
    :param log_file: string - None (default), use '/var/log/sender.log' if you want create log file<br>
    :return: True<br>

Example:<br>
<code>from sender import Sender</code><br>

<code>param = ['smtp.gmail.com',<br>
         'from@gmail.com',<br>
         'to@gmail.com',<br>
         'Subject',<br>
         'My perfect text',<br>
         'username',<br>
         'password',<br>
         465,<br>
         True,<br>
         True,<br>
         'sender.log']</code><br>
<code>sender = Sender()</code><br>
<code>sender.send_email(*param)</code><br>

