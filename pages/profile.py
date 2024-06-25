import streamlit as st
from menu import memu;memu()
import time
from models import User
import time
#from streamlit_server_state import server_state#, server_state_lock

st.header("Account Setting")
st.divider()
# XvvX
user = st.session_state.data
def role():
	if st.session_state.role == 'admin':
		return ":blue-background[Admin]"
	return ":green-background[User]"

# Chnage username function
def new_username_exe(userr, passw, new):
	x = userr
	y = passw
	z = new
	if passw != user['password']:
		st.error(":red-background[error] Incorrect password")
		return
	i = User.update_username(x,y,z)
	o = i['message']
	if i['status']:
		user['username'] = new.lower().strip()
		st.success(":green-background[success] New username change")
		time.sleep(1.4)
		st.switch_page('pages/profile.py')
	else:
		st.error(f':red-background[error] {o}')
		return

# Change Password function
def new_password_exe(current_pass, new_pass):
	x = current_pass
	y = new_pass
	if x != user['password']:
		st.error(":red-background[error] Current password don't match")
		return
	II = User.change_password(new_pass)
	z = II['message']
	if II['status']:
		st.success(':green-background[success] Change password')
		user['password'] = new_pass
		return
	else:
		st.error(f':red-background[error] {z}')
		return
# Profile Info
A1, A2 = st.columns(2)
with A1:
	cont = st.container(border=True)
	with cont:
		st.write("""
		Username : :red[{}]\n
		Role : {}
		""".format(user['username'], role()))
		if st.button("Logout"):
			time.sleep(0.2)
			st.session_state.role = None
			st.session_state.data = {}
			st.switch_page('pages/login.py')

# Account Settings
with A2:
	with st.form('change username', clear_on_submit=True):#st.container(border=True):
		with st.expander("Change username"):
			new_user = st.text_input("New Username")
			confirm = st.text_input("Enter your password", type='password')
			btn = st.form_submit_button('Change', type='primary', use_container_width=True)
			if btn:
				if not new_user or not confirm:
					st.warning(":orange-background[Failed] Missing input value")
				elif len(new_user) > 16:
					st.warning(':orange-background[Failed] Maximum length is **16**')
				elif len(new_user) < 3 and len(new_user) > 0:
					st.warning(":orange-background[Failed] Minimum length is **3**")
				else:
					new_username_exe(user['username'], confirm, new_user)
		with st.expander("Change Password"):
			current = st.text_input("Current Password", type='password').strip()
			new_pass = st.text_input("New Password", type='password').lower().strip()
			btnn = st.form_submit_button('change', type='primary', use_container_width=True)
			if btnn:
				if not current or not new_pass:
					st.warning(":orange-background[Failed] Missing input value")
				elif len(new_pass) > 16:
					st.warning(':orange-background[Failed] Maximum length is **16**')
				elif len(new_pass) < 6 and len(new_pass) > 0:
					st.warning(":orange-background[Failed] Minimum length is **6**")
				else:
					new_password_exe(current, new_pass)