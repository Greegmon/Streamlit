import streamlit as st
import requests
from menu import memu;memu()
st.header("Facebook React");st.divider()

cookie = st.text_area("Cookie")
post = st.text_input("Link")
x = ["👍 LIKE","❤️ LOVE","🤗 CARE","😆 HAHA","😲 WOW","😢 SAD","😡 ANGRY"]
react = st.selectbox("Reaction", x)

def sendReact(cookie, post, react):
	link = "https://flikers.net/android/android_get_react.php"
	pay = {"post_id": post, "react_type": react, "version": 'v1.7'}
	head = {
		'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 12; V2134 Build/SP1A.210812.003)",
		'Connection': "Keep-Alive",
		'Accept-Encoding': "gzip",
		'Content-Type': "application/json",
		'Cookie': cookie
	}
	res = requests.post(link, json=pay, headers=head)
	return

btn = st.button("Submit", type='primary')
if btn:
	if not cookie or not post or not react:
		st.error("Error, Missing input value")
	else:
		if "c_user=" in cookie:
			st.success("Sending reacts...")
			sendReact(cookie, post, react.split(' ')[1])
		else:
			st.error("Invalid Cookie")