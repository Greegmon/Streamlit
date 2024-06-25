import streamlit as st
from menu import menu
from models import User

st.header("Login", divider="blue")
Username = st.text_input("Username").lower().strip()
Password = st.text_input("Password", type='password').lower().strip()
col1, col2 = st.columns(2)
log = col1.button("Login", type='primary', use_container_width=True)
sign = col2.button("Signup")

if sign:
	st.switch_page('pages/signup.py')
if log:
	if not Username or not Password:
		st.warning("Missing input")
	else:
		res = User.login(Username, Password)
		if res['status'] == False:
			st.error(res['message'])
		else:
			i = res['data']
			user_data = {
				"id": i['id'],
				"username": i['username'],
				"password": i['password']
			}
			st.session_state.data = user_data
			st.session_state.role = i['role']
			st.switch_page('pages/home.py')
menu()