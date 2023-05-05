from numpy.core.numeric import True_
from sklearn import metrics
import streamlit as st
import pandas as pd
import numpy as np

import time
import pyperclip

from smtplib import SMTP
from poplib import POP3_SSL
from time import sleep
import getpass
import email


def main():
    st.title("Mass Mailer")

if __name__ == '__main__':
    main()

class Mailer:
    def __init__(self,sender_id="",password="",recv_id="",subject="",body=""):
    
        self.sender_id=sender_id
        self.password=password
        self.recv_id=recv_id
        self.subject=subject
        self.body=body
    
    
def inputing(g):
    
    
    g.sender_id = st.text_input("Enter Sender's mail ID:", '')
    st.write('', g.sender_id)

    #use the passowrd key generated by google for "less secure app access" using the link here
    # https://www.google.com/settings/security/lesssecureapps
    
    g.password = st.text_input("Enter Password:", type="password")
    # st.write('', password)
    
    g.recv_id = st.text_input("Enter Reciever's mail ID:", '')

    st.write('', g.recv_id)

    g.subject = st.text_input("Subject:")
    # st.write('', subject)

    st.write('Message Body:')
    g.body = st.text_area('''
    ''')


def function_send_mail(g):
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()

    server.login(g.sender_id, g.password)

    sent_from = g.sender_id

    if len(g.recv_id.split(","))>1:
        to=g.recv_id.split(",")
    else:
        to = [g.recv_id]    
    
    subject = g.subject
    body = str(g.body)

    
    email_text = """\
    %s
    """ % ("From: "+sent_from+"\n"+"To: "+", ".join(to)+"\n"+"Subject: "+subject+"\n"+body)
    for i in to:
        server.sendmail(sent_from, i, email_text)
    print ('Email sent!')

    server.quit()
    
    return True



g=Mailer()
inputing(g)

if st.sidebar.button("Send Mail", key="send"):
    with st.spinner('Wait for it...'):
        y=function_send_mail(g)
        # time.sleep(10)
    st.balloons()
    st.success('Done!')
    
    
default_id= "example@gmail.com"

# Create a button that copies the text when clicked
if st.sidebar.button('Default ID'):
    pyperclip.copy(default_id)
    st.sidebar.write('Text copied to clipboard!')
    
#Create a password for less secure app access
default_pw= "XXXXXXXXXXXX"

if st.sidebar.button('Default Password'):
    pyperclip.copy(default_pw)
    st.sidebar.write('Text copied to clipboard!')


import streamlit as st

uploaded_files = st.sidebar.file_uploader("Choose a file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.sidebar.write("filename:", uploaded_file.name)
    # st.sidebar.write(bytes_data)






