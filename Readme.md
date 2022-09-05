# This is an application to automate sending emails process



## How to use this program:



### First, prepare the necessary files for the program to work.

1) The file "license.txt" contains the license that you purchased from us. If you don't have one, contact us at ===== .

1) The "list.txt" file contains a list of email addresses that you want to send emails to .

2) The file "name.txt" contains a list of names to be used as FromName .

3) The file "FromEmail.txt" contains a list of email to display in the emails you sent as a from email .

4) The "subject.txt" file contains a list of subjects to list of Subjects to be used as Subject


5) The "smtp.txt" file contains the smtp list to send messages with . the format of each smtp should be like (smtp|host|port|tls/ssl|user/email|password)

6) The file "body.txt" contains the body of the messages you want to send

### how the program works.

Lets say
 
smtp.txt has 10 smtp server
 
mailfrom.txt has 1000 from mail 
 
list.txt has 2000 emails
 
 
1- smtp-1 will send to Email-1 with from mail 
2- smtp-2 will send to Email-2 with from mail -2
 .....
 ....
smtp-10 will send to Email-10 with from mail -10
 
Repeat Process
 
smtp-1 will send to Email-11 with from mail -11


### how to run the program

all you have to do is double click on the program. the program will ask you how many threads you want just type number between 1 and 10 and it will start sending .
so, what is the threads ?
threads in basicaly how many emails you want to send in the same time , for exemple if you typed 5 the program will send 5 email each time until the end of the list