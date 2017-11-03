from datetime import timedelta
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version
    

credentials = Credentials(username='username', password='password')
my_account = Account(primary_smtp_address='username@lenovo.com', credentials=credentials,
                     autodiscover=True, access_type=DELEGATE)

m = Message(
    account=my_account,
    subject='Daily motivation',
    body='All bodies are beautiful',
    to_recipients=[Mailbox(email_address='chenxu6@lenovo.com'), Mailbox(email_address='kongyl4@lenovo.com')]
)
m.send()