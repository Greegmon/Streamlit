import streamlit as st
from menu import menu
if 'role' not in st.session_state or st.session_state.role == None:
	st.switch_page('pages/login.py')
menu()

'''
Developer : Lorem (Greegmon)
Facebook : https://www.facebook.com/61555393773104

- Kunin mo na ang source code wag lang ang ka pogian ko 😎
- Sa china nalang ang WPS (West Philippine Sea)
basta satin ang SCS (South China Sea)

-------- NOTE ! --------
kung gagamitin mo tong src nato okay lang
pero punta ka muna sa ./streamlit/secrets.toml
palitan mo yung DB_URL & DB_KEY ng database mo.

TABLE NAME : accounts
_____________________________________________
| id | username | password | role | created |
-----|----------|----------|------|---------|
'''