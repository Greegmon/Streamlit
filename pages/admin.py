import streamlit as st
from menu import memu
import pandas as pd
from models import User
import time
memu()
if st.session_state.role != 'admin':
	st.warning("You don't have permission to access this page.")
	st.stop()

st.header("Admin Panel")
st.divider()

data = User.fetch_all()
with st.container():
	st.write('**:gear: Account List**')
	df = pd.DataFrame(
		{
			"id": [x['id'] for x in data],
			"created": [x['created'].split('T')[0] for x in data],
			"username": [x['username'] for x in data],
			"password": [x['password'] for x in data],
			"role": [x['role'] for x in data]
		}
	)
	st.dataframe(df, hide_index=True, width=1000)

A2,B2 = st.columns(2)
with A2:
	with st.form('delete user', clear_on_submit=True):
		st.write('**:blue[Delete user]**')
		target = st.text_input('Target username').lower().strip()
		confirm = st.text_input('Enter your password', type='password').strip()
		if st.form_submit_button('Delete', type='primary', use_container_width=True):
			if not target or not confirm:
				st.warning(':orange-background[failed] Missing input value')
			elif confirm != st.session_state.data['password']:
				st.error(':red-background[error] Invalid password')
			else:
				c = User.delete_user(target)
				if c['status']:
					st.success(":green-background[success] {}".format(c['message']))
					time.sleep(1.4)
					st.switch_page('pages/admin.py')
				else:
					st.error(":red-background[error] %s" % (c['message'],))

with B2:
	with st.form("promote", clear_on_submit=True):
		st.write("**:blue[Manage Role]**")
		target = st.text_input("Target username").lower().strip()
		role = st.selectbox("role", ['user', 'mod', 'admin'])
		if st.form_submit_button('Promote'):
			if not target:
				st.warning(":orange-background[error] Missing target username.")
			elif role == st.session_state.role:
				st.warning(":orange-background[error] This role is already set")
			else:
				xyz = User.setRole(target, role)
				st.write(role)
				if xyz['status']:
					st.success(":green-background[done] " + xyz['message'])
					time.sleep(1.3)
					st.switch_page('pages/admin.py')
				else:
					st.error(":red-background[error] " + xyz['message'])