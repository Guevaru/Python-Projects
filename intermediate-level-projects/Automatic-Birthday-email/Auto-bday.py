import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage

def send_email(recipient, subject, msg, sender_email, sender_password):
    # Send an email with the given subject and message
    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = sender_email
    email['To'] = recipient
    email.set_content(msg)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
        gmail_obj.ehlo()
        gmail_obj.login(sender_email, sender_password)
        gmail_obj.send_message(email)
    print('Email sent to ' + str(recipient) + ' with Subject: \''
          + str(subject) + '\' and Message: \'' + str(msg) + '\'')

def send_birthday_emails(birthday_file, sender_email, sender_password):
    # Send birthday emails to recipients from the provided Excel file
    bdays_df = pd.read_excel(birthday_file)
    today = datetime.now().strftime('%m-%d')
    year_now = datetime.now().strftime('%Y')
    sent_index = []

    for idx, item in bdays_df.iterrows():
        bday = item['Birthday'].to_pydatetime().strftime('%m-%d')
        if (today == bday) and year_now not in str(item['Last Sent']):
            msg = 'Happy Birthday ' + str(item['Name'] + '!!')
            send_email(item['Email'], 'Happy Birthday', msg, sender_email, sender_password)
            sent_index.append(idx)

    for idx in sent_index:
        bdays_df.loc[bdays_df.index[idx], 'Last Sent'] = str(year_now)

    bdays_df.to_excel(birthday_file, index=False)

if __name__ == '__main__':
    sender_email = 'your_email_here'
    sender_password = 'your_password_here'
    birthday_file = 'your_bdays_list.xlsx'
    send_birthday_emails(birthday_file, sender_email, sender_password)
