import streamlit as st
from streamlit import session_state as ss
from datetime import datetime;date = datetime.now()
from models import teleBOT
#import extra_streamlit_components as stx

def verified():
	st.sidebar.page_link("pages/home.py", label='Home')
	st.sidebar.page_link("pages/profile.py", label="Profile")
	if st.session_state.role == 'admin':
		st.sidebar.page_link("pages/admin.py", label="Admin Panel")
	else:
		with st.sidebar.expander("Message developer"):
			form = st.sidebar.form('send message to developer', clear_on_submit=True)
			inp = form.text_area('**Send message to** :red-background[greegmon]').strip()
			if form.form_submit_button('Send', type="primary", use_container_width=True):
				if len(inp) < 10:
					form.warning("Message too short")
				else:
					msg = {
						"sender": ss.data['username'],
						"message": inp,
						"time": date.strftime("%-m/%-d/%Y - %-I:%M %p")
					}
					teleBOT(f"[✉️] - MESSAGE\n\nSender : {msg['sender']}\nMessage : {msg['message']}\n\n(🕠) - {msg['time']}")
					form.success(':green-background[success] Message Sent')

def unverified():
	st.sidebar.page_link("pages/login.py", label="Login")
	st.sidebar.page_link("pages/signup.py", label="Signup")

def menu():
	st.markdown('''
	<style>
	.eczjsme4 button,.eczjsme3 .ef3psqc4{background: #4371e6 !important;color: white !important}
	</style>
	''', unsafe_allow_html=True)
	if 'role' not in st.session_state or st.session_state.role == None:
		unverified()
		return
	verified()

def memu():
	if 'role' not in st.session_state or st.session_state.role == None:
		st.switch_page('main.py')
	menu()