import streamlit as st
from streamlit_chat import message
from utils import query_from_API

st.set_page_config(
    page_title="ndhieunguyen chatbot",
    page_icon="🤖",
)

query = st.sidebar.text_area("You:", "", placeholder="Say something...", height=256)
with st.spinner("Generating..."):
    if query != "":
        if "message" not in st.session_state:
            st.session_state["message"] = []

        st.session_state["message"].append((query, True))
        response = query_from_API(query=query, token=st.secrets['poe_api_token'])
        st.session_state["message"].append((response, False))

        for mess, is_user in st.session_state["message"]:
            message(message=mess, is_user=is_user)
