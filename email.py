import smtplib
from email.message import EmailMessage

def draft_email_from_file(sender_email, recipient_email, subject, file_path):
    """
    Reads content from an ASCII text file and drafts an email.

    Args:
        sender_email (str): The email address of the sender.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        file_path (str): The path to the ASCII text file containing the email body.
    """
    try:
        with open(file_path, 'r', encoding='ascii') as f:
            email_body = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    except UnicodeDecodeError:
        print(f"Error: The file {file_path} is not a valid ASCII file.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(email_body)

    # In a real application, you would configure an SMTP server to send the email.
    # For drafting, we're just constructing the message.
    print("\n--- Email Draft ---")
    print(f"From: {msg['From']}")
    print(f"To: {msg['To']}")
    print(f"Subject: {msg['Subject']}")
    print("\nBody:")
    print(msg.get_content())
    print("-------------------\n")

    # To send the email, you would use smtplib:
    # try:
    #     with smtplib.SMTP('your_smtp_server.com', 587) as s:
    #         s.starttls()
    #         s.login('your_username', 'your_password')
    #         s.send_message(msg)
    #     print("Email sent successfully!")
    # except Exception as e:
    #     print(f"Error sending email: {e}")

if __name__ == "__main__":
    sender = "pyurov@techsquare.com"  # Replace with your email
    recipient = "pyurov@techsquare.com"  # Replace with recipient's email
    email_subject = "Important Update"
    text_file = "email_content.txt"  # Create this file with your email body

    # Example: Create a dummy email_content.txt file
    with open(text_file, 'w', encoding='ascii') as f:
        f.write("Dear Recipient,\n\nThis is a test email drafted from an ASCII text file.\n\nSincerely,\nYour Script")

    draft_email_from_file(sender, recipient, email_subject, text_file)
