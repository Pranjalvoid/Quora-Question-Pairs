import streamlit as st
import helper
import pickle
import urllib.request

st.header('Duplicate Question Pairs')

# ---------- Load Model from HuggingFace ----------
MODEL_URL = "https://huggingface.co/pranjalvoid/duplicate-question-detector-model/resolve/main/model.pkl"
model = pickle.load(urllib.request.urlopen(MODEL_URL))
# -------------------------------------------------

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
