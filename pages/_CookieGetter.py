import requests
import re
import streamlit as st
from menu import memu;memu()

def Cookie(user, passw):
	session=requests.Session()
	headers = {
		'authority': 'free.facebook.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment closer]*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'dpr': '3',
		'origin': 'https://free.facebook.com',
		'referer': 'https://free.facebook.com/login/?email=%s'%(user),
		'sec-ch-prefers-color-scheme': 'dark',
		'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		'viewport-width': '980',
	}
	getlog = session.get(f'https://free.facebook.com/login.php')
	idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(getlog.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(getlog.text)).group(1),"try_number":"0","unrecognize_tries":"0","email":user,"pass":passw,"login":"Log In","bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(getlog.text)).group(1),}
	comp=session.post("https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated",headers=headers,data=idpass,allow_redirects=False)
	jopl=session.cookies.get_dict().keys()
	cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
	if "c_user" in jopl:
		return st.write(f"**:green-background[Cookie]**\n{cookie}")
	elif "checkpoint" in jopl:
		return st.error(":red-background[error] Account checkpoint")
	else:
		return st.error(":red-background[error] Invalid username or password")

st.header('Cookie Getter')
st.divider()

with st.form('cookie get'):
	x = st.text_input("email/id/number").strip()
	y = st.text_input("password", type='password').strip()
	if st.form_submit_button('Get cookie', type='primary', use_container_width=True):
		if not x or not y:
			st.warning('Missing input value', icon="🚨")
		else:
			Cookie(x,y)