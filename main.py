import streamlit as st


st.set_page_config(page_title="Ca sĩ yêu thích", page_icon=":smile:")
with st.sidebar:
    st.image("https://static.wikia.nocookie.net/producerviet/images/a/a1/Th%E1%BA%AFng_%28Ng%E1%BB%8Dt%29.webp/revision/latest?cb=20230729011109", caption="Ngọt")
    st.write("Ban nhạc Ngọt")
    st.write("Ngọt là một ban nhạc pop rock Việt Nam gồm bốn thành viên Vũ Đinh Trọng Thắng (hát chính, guitar đệm), Phan Việt Hoàng (guitar bass), Nguyễn Hùng Nam Anh (trống)[1] và Hoàng Chí Trung (keyboard)")
    
st.title("Bài hát yêu thích")
st.write("Ngọt - LẦN CUỐI (đi bên em xót xa người ơi)")
st.audio("lancuoi.mp3", format="audio/mp3")

st.title("MV yêu thích")
st.write("Ngọt - LẦN CUỐI (đi bên em xót xa người ơi)")
st.video("https://www.youtube.com/watch?v=kSjj0LlsqnI", format="video/mp4")