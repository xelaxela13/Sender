#!/usr/bin/env python3

import smtplib
import logging
from datetime import datetime
import os


class __Sender:
    __CURRENT_DATE = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def __init__(self, log=False, log_filename='./sender.log'):
        self.__log = log
        self.__log_filename = log_filename

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
            mode = 'a' if os.path.isfile(self.__log_filename) else 'w'
            logging.basicConfig(filename=self.__log_filename, level=eval('logging.' + action), filemode=mode)
            eval("logging." + action.lower())('{0} - {1}'.format(self.__CURRENT_DATE, text))

    def send_email(self, host, sender, recipients, subject, msg, user=None, password=None, port=25, ssl=False,
                   debug=False):
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
        :return: True
        """
        try:
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
        except smtplib.SMTPException as err:
            self.__to_log('Error send email: {}'.format(err), 'error')
        except ConnectionRefusedError as err:
            self.__to_log('Connection refused error: {}'.format(err), 'error')
        except TimeoutError as err:
            self.__to_log('Time out error: {}'.format(err), 'error')


def send_email(host, sender, recipients, subject, massage, username=None, password=None, port=25, ssl=False,
               debug=False, logging=False):
    """
    Send email, message will be text or html format.
    Example:
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

    :param host: string
    :param sender: string - sender email
    :param recipients: string - recipients email
    :param subject: string
    :param massage: string
    :param username: string - username from email server
    :param password: string - password
    :param port: int - 25 default, 465 gmail ssl, 587 gmail ttl
    :param ssl: bool - False default
    :param debug: bool - False default
    :param logging: bool - False default
    :return: True
    """
    send = __Sender(logging)
    send.send_email(host, sender, recipients, subject, massage, username, password, port, ssl,
                    debug)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
