import streamlit as st
import json
import mechanize
from menu import memu

st.header("Token Getter")
st.divider()
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [("User-Agent", "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")]
# Get the account access token EAAAAU and EAADYP
def token(x,y):
	def EAAAAU(user,passw):
		res = br.open(f"https://b-api.facebook.com/method/auth.login?email={user}&password={passw}&format=json&generate_session_cookies=1&generate_machine_id=1&generate_analytics_claim=1&locale=en_US&client_country_code=US&credentials_type=device_based_login_password&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&fb_api_req_friendly_name=authenticate&api_key=882a8490361da98702bf97a021ddc14d&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32")
		data = json.load(res)
		if 'access_token' in data:
			return data['access_token']
		else:
			st.error(f":red-background[error] {data['error_msg']}")
			return
	def EAADYP(user, passw):
		res = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + user + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
		data = json.load(res)
		if 'access_token' in data:
			return data['access_token']
		else:
			st.error(f":red-background[error] {data['error_msg']}")
			return
	try:
		user,passw = (x,y)
		reg = EAAAAU(user,passw)
		if reg:
			st.write(f"**:blue-background[EAAAAU]** : {reg}")
			st.write(f"**:blue-background[EAADYP]** : {EAADYP(user,passw)}")
	except:
		st.error(":red-background[error] While getting your access token")

with st.form('Token Getter', clear_on_submit=True):
	u = st.text_input('email/id/number').strip()
	p = st.text_input('password', type='password')
	if st.form_submit_button('Get Token', type="primary"):
		if not u or not p:
			st.warning("Missing inputs value", icon='🚨')
		else:
			token(u,p)

memu()