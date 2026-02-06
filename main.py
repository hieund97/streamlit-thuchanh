import streamlit as st


st.set_page_config(page_title="Trang chủ", page_icon=":smile:", layout = "centered")
st.title("Con vật bạn yêu thích")

col1, col2, col3, col4, col5 = st.columns(5)
name = ""
info = ""

with col1:
    cat = st.button("Con mèo")
    if cat:
        name = "Con mèo"
        info = "Đây là thông tin của con mèo"
with col2:
    dog = st.button("Con chó")
    if dog:
        name = "Con chó"
        info = "Đây là thông tin của con chó"
with col3:
    lion = st.button("Con sư tử")
    if lion:
        name = "Con sư tử"
        info = "Đây là thông tin của con sư tử"
with col4:
    horse = st.button("Con ngựa")
    if horse:
        name = "Con ngựa"
        info = "Đây là thông tin của con ngựa"
with col5:
    eagle = st.button("Con thiên nga")
    if eagle:
        name = "Con thiên nga"
        info = "Đây là thông tin của con thiên nga"

with st.sidebar:
    st.header("Trắc nghiệm tính cách")
    st.write(f"Con vật bạn chọn là con {name}") 
    
with st.expander(name):
    st.write(info)