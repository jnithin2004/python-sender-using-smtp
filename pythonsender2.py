import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def read_recipients():
    """Read recipient emails from the hardcoded text file."""
    file_path = 'recipients.txt'
    with open(file_path, 'r') as file:
        recipients = file.readlines()
    recipients = [email.strip() for email in recipients]
    return recipients

def send_email(sender_email, sender_password, recipients, subject, message):
    """Send an email to a list of recipients."""
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender_email, sender_password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            smtp_server.send_message(msg)
            print(f'Email sent to {recipient}')
        except Exception as e:
            print(f'Failed to send email to {recipient}: {e}')

    smtp_server.quit()

def main():
    """Main function to input email details and send emails."""
    sender_email = input("Enter your email: ")
    sender_password = getpass.getpass("Enter your email password: ")
    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")

    try:
        recipients = read_recipients()
        send_email(sender_email, sender_password, recipients, subject, message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
