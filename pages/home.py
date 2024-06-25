import streamlit as st
from menu import memu;memu()

st.header("Home")
st.divider()


st.markdown('''
<style>
.e1f1d6gn5 .stPageLink a/*.e11k5jya1*/{
  background: #4371e6 !important;
	padding: 3px 13px !important;
	border-radius: 8px;
	color: white !important
}
</style>
''', unsafe_allow_html=True)
A1,B1,C1 = st.columns(3)
with A1.container(border=True):
	st.image('cache/token_getter.jpg', caption="Facebook token getter (EAAAAU, EAADYP)")
	st.page_link("pages/_TokenGetter.py", label='Redirect')

with B1.container(border=True):
	st.image('cache/cookie_getter.jpg', caption='Get facebook cookie')
	st.page_link('pages/_CookieGetter.py', label='Redirect')

with C1.container(border=True):
	st.image('cache/FbReact.jpg', caption='Get facebook cookie')
	st.page_link('pages/_FbReact.py', label='Redirect')