#!/usr/bin/python


# useful error messages for cgi
import cgitb
cgitb.enable()

import cgi # cgi for the form processing
import smtplib # smtplib for the actual sending function

# Import the email modules we'll need
from email.mime.text import MIMEText

form = cgi.FieldStorage()

if "name" not in form or "address" not in form:
    print "Content-type: text/html\n";
    print 
    print "<H1>Error</H1>"
    print "Please fill in the name and address fields."
    
address  = form.getfirst("address", "--")
names = form.getlist("name")
data = "  Names:\n"+'\n'.join(names) + "\n\n  Address:\n"+address

message = """Hi Pie! 

A web form was just submitted! Here's the data:
%s

*hugggggs*
Your nifty web server :-)
"""%data
# Create a text/plain message
msg = MIMEText(message)

me = "Psychard Website <webform@psychard.com>"
you = "Psychard Wedding <wedding@psychard.com>"
sender = "rwest@mit.edu"
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Wedding web form from %s'%(', '.join(names))
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.connect()
s.sendmail(sender, [you], msg.as_string())
s.quit()


print "Location: http://www.psychard.com/thankyou.html\n\n";
