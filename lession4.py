import streamlit as st
import time

st.title("Chương trình nhập thông tin học sinh")

name = st.text_input("Nhập tên")
age = st.text_input("Nhập tuổi")
school = st.text_input("Nhập trường")

if st.button("Submit"):
    if not name or not age or not school:
        st.warning("Vui lòng nhập đầy đủ thông tin")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
            status_text.text(f"Đang xử lý {i + 1}%")
        
        st.success("Đăng ký thành công")
        st.write("Tên: ", name)
        st.write("Tuổi: ", age)
        st.write("Trường: ", school)

        st.balloons()
