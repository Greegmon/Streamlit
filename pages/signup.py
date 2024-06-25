import streamlit as st
import time
from models import User
from menu import menu

st.header("Signup", divider='blue')
username = st.text_input('Username').lower().strip()
password = st.text_input('Password', type='password').lower().strip()
password2 = st.text_input('Retype Password', type='password').lower().strip()
col1, col2 = st.columns(2)
sign = col1.button("Signup", type='primary', use_container_width=True)
log = col2.button("Login")
if log:
	st.switch_page('pages/login.py')
if sign:
	ku = username.split()
	pal = password.split()
	if  not username or not password or not password2:
		st.warning('Missing Input Value')
	elif password != password2:
		st.error("Password don't match")
	elif len(username) < 3 and len(username) > 0:
		st.error('Username min length is :red-background[3]')
	elif password == password2 and len(password) < 6:
		st.error('Password minimum length is 6')
	elif len(username) > 16:
		st.error('Username max length is 16')
	elif password == password2 and len(password) > 16:
		st.error('Password max length is 16')
	elif ' ' in ku or ' ' in pal:
		st.error('Space is not allowed')
	else:
		signup = User.signup(username, password)
		if signup['status'] == False:
			st.error(signup['message'])
		else:
			st.success(signup['message'])
			time.sleep(1.4)
			st.switch_page('pages/login.py')

menu()
