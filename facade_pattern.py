"""
The facade pattern is designed to provide a simple interface
to a complex system of components.

It's pretty similar to the adapter pattern, but here's the main difference:
- the facade is trying to abstract a simpler interface out of a complex one.
- the adapter is only trying to map one existing interface to another.

For eg: The requests library is a facade over the less readable HTTP library.

"""

import smtplib
import imaplib


class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        if not "@" in self.username:
            from_email = f"{self.username}@{self.host}"
        else:
            from_email = self.username

        message = (f"From: {from_email}"
                   f"To: {to_email}\r\n"
                   f"Subject: {subject}\r\n\r\n{message}")

        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(bytes(self.username, 'utf8'), bytes(self.password, 'utf8'))
        mailbox.select()
        x, data = mailbox.search(None, 'ALL')
        messages = []

        for num in data[0].split():
            x, message = mailbox.fetch(num, '(RFC822)')
            messages.append(message[0][1])

        return messages