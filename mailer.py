import time
from mail_sender import mail_sender
import threading
import os
import requests


def check_file_exist(file):
    return os.path.isfile(file)


def is_license_valid(license_key):
    try:
        url = "https://salty-falls-75869.herokuapp.com/verify/" + license_key + "/" + str(requests.get('https://api.ipify.org').text)
        res = requests.get(url)
        if res.json()["status"] == 'ok':
            return True
    except:
        return False


def main():
    threads_input = input("how many threads you want ? ")

    names = "name.txt"
    FromEmail = "mailfrom.txt"
    subject = "subject.txt"
    recipient = "list.txt"
    license = "license.txt"
    smtp = "smtp.txt"
    body = "body.txt"
    smtps_list = None
    FromEmails_list = None
    subjects_list = None
    license_key = None
    body_msg = None
    try:
        with open(smtp, 'r+') as sm:
            smtps_list = sm.read().splitlines()
        with open(names, 'r+') as sm:
            names_list = sm.read().splitlines()

        with open(FromEmail, 'r+') as sm:
            FromEmails_list = sm.read().splitlines()

        with open(subject, 'r+') as sm:
            subjects_list = sm.read().splitlines()

        with open(recipient, 'r+') as sm:
            recipients_list = sm.read().splitlines()

        with open(license, 'r+') as sm:
            license_key = sm.read().splitlines()

        with open(body, 'r+') as sm:
            body_msg = sm.read()
    except:
        print("please double check entry files")
        time.sleep(2)
        exit()

    if not is_license_valid(license_key[0]):
        print(f"invalid license {license_key[0]}")
        time.sleep(2)
        exit()

    subject_tracker = 0
    names_tracker = 0
    from_email_tracker = 0
    smtp_tracker = 0
    threads_tracker = 0
    threads = []
    thread_number = 1
    if int(threads_input) > 10:
        thread_number = 10
    elif int(threads_input) < 1:
        thread_number = 1
    else:
        thread_number = threads_input
    for recept in recipients_list:
        if subject_tracker == len(subjects_list):
            subject_tracker = 0
        if names_tracker == len(names_list):
            names_tracker = 0
        if from_email_tracker == len(FromEmails_list):
            from_email_tracker = 0
        if smtp_tracker == len(smtps_list):
            smtp_tracker = 0
        smtp_server = smtps_list[smtp_tracker].split("|")[0]
        smtp_port = smtps_list[smtp_tracker].split("|")[1]
        smtp_encryption = None
        if smtps_list[smtp_tracker].split("|")[1].lower() == 'ssl':
            smtp_encryption = 'SSL'
        elif smtps_list[smtp_tracker].split("|")[1].lower() == 'tls':
            smtp_encryption = 'TLS'
        smtp_email = smtps_list[smtp_tracker].split("|")[3]
        smtp_password = smtps_list[smtp_tracker].split("|")[4]
        data = {
            'from_email': FromEmails_list[from_email_tracker],
            'from_name': names_list[names_tracker],
            'to_email': recept,
            'subject': subjects_list[subject_tracker],
            'smtp_server': smtp_server,
            'smtp_port': int(smtp_port),
            'smtp_email': smtp_email,
            'smtp_password': smtp_password,
            'smtp_encryption': smtp_encryption
        }
        if "</html>" in body_msg.lower():
            data["html_message"] = body_msg
        else:
            data["text_message"] = body_msg
        tt = threading.Thread(target=mail_sender,args=(data,))
        tt.start()
        threads.append(tt)
        if len(threads) == thread_number:
            for t in threads:
                t.join()
            threads = []
        subject_tracker += 1
        names_tracker += 1
        from_email_tracker += 1
        smtp_tracker += 1
        threads_tracker += 1
    print("done")

if __name__ == "__main__":
    main()