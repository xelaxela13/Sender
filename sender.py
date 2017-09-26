#!/usr/bin/env python3

import smtplib
import logging
from datetime import datetime
import os


class Sender:
    """
    Send email, message will be text or html format.
    Example:
        from sender import Sender
        param = ['smtp.gmail.com',
             'from@gmail.com',
             'to@gmail.com',
             'Subject',
             '<H1>My perfect text</H1>',
             'username',
             'password',
             465,
             True,
             True]
         sender = Sender()
         sender.send_email(*param)
    >>> from sender import Sender
    >>> sender = Sender()
    >>> sender.send_email('smtp.gmail.com', 'from@mail.com', 'to@gmail.com', 'My subject', 'Text',\
    'username', 'password', 465, True)
    False
    """
    __CURRENT_DATE = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    __LOG_DEFAULT_FILENAME = 'sender.log'

    def __init__(self):
        self.__log = False
        self.__log_filename = None

    @property
    def __get_log_filename(self):
        return self.__log_filename

    def __set_log_file(self, log_file):
        if log_file is not None:
            self.__log = True
            self.__log_filename = log_file

    def __to_log(self, text, action):
        """
        :type text: str
        :type action: str
        :param text: your text
        :param action: string from actions dict
        """
        actions = [
            'DEBUG',
            'INFO',
            'WARNING',
            'ERROR',
            'CRITICAL',
        ]
        action = str(action).upper()
        if self.__log and action in actions:
            try:
                mode = 'a' if os.path.isfile(self.__get_log_filename) else 'w'
                logging.basicConfig(filename=self.__get_log_filename, level=eval('logging.' + action), filemode=mode)
                eval("logging." + action.lower())('{0} - {1}'.format(self.__CURRENT_DATE, text))
            except FileNotFoundError:
                self.__set_log_file(self.__LOG_DEFAULT_FILENAME)
                self.__to_log(text, action)
            except PermissionError as err:
                print(err)

    def send_email(self, host, sender, recipients, subject, msg, user=None, password=None, port=25, ssl=False,
                   debug=False, log_file=None):
        """
        :param host: string
        :param sender: string - sender email
        :param recipients: string - recipients email
        :param subject: string
        :param msg: string
        :param user: string - username from email server
        :param password: string - password
        :param port: int - 25 default, 465 gmail ssl, 587 gmail ttl
        :param ssl: bool - False default
        :param debug: bool - False default
        :param log_file: string - log file path /var/log/sender.log
        :return: True
        """
        try:
            self.__set_log_file(log_file)
            msg = """From: <{0}>
    To: <{1}> 
    MIME-Version: 1.0
    Content-type: text/html
    Subject: {2}
    {3}""".format(sender, recipients, subject, msg)
            if ssl:
                with smtplib.SMTP_SSL(host, port=int(port)) as s:
                    s.set_debuglevel(debug)
                    s.ehlo()
                    if user and password: s.login(user, password)
                    s.sendmail(sender, recipients, msg)
                    self.__to_log('Email from {} to {} was sent successful'.format(sender, recipients), 'info')
                    return True
            else:
                with smtplib.SMTP(host, port=int(port)) as s:
                    s.set_debuglevel(debug)
                    s.ehlo()
                    s.starttls()
                    if user and password: s.login(user, password)
                    s.sendmail(sender, recipients, msg)
                    self.__to_log('Email from {} to {} was sent successful'.format(sender, recipients), 'info')
                    return True
        except smtplib.SMTPAuthenticationError as err:
            self.__to_log('The server did not accept the username/password combination: {}'.format(err), 'error')
            return False
        except smtplib.SMTPException as err:
            self.__to_log('Error send email: {}'.format(err), 'error')
            return False
        except ConnectionRefusedError as err:
            self.__to_log('Connection refused error: {}'.format(err), 'error')
            return False
        except TimeoutError as err:
            self.__to_log('Time out error: {}'.format(err), 'error')
            return False

if __name__ == '__main__':
    import doctest

    doctest.testmod()
