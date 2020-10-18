import sys
from datetime import datetime
import requests

from formatting import format_msg
from send_mail import send_mail

def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None

    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website, to_email)

    try:
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
    return sent



if __name__ == "__main__":
    name = 'Unknown'
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    website = None
    if len(sys.argv) > 3:
        website = sys.argv[3]


    response = send(name, to_email=email, website=website, verbose=True)
    print(response)
