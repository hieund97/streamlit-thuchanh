import streamlit as st


st.set_page_config(page_title="Trang chủ", page_icon=":smile:", layout = "centered")
st.title("Con vật bạn yêu thích")

col1, col2, col3, col4, col5 = st.columns(5)
name = ""
info = ""
image = ""
audio = ""
video = ""

with col1:
    cat = st.button("Con mèo")
    if cat:
        name = "Con mèo"
        info = "Đây là thông tin của con mèo"
        image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkZzfOTBoJDKxZHPcHNSshhX-FAXxR75vwnA&s"
        audio = "meme1.mp3"
        video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
with col2:
    dog = st.button("Con chó")
    if dog:
        name = "Con chó"
        info = "Đây là thông tin của con chó"
        image = "https://cafefcdn.com/203337114487263232/2023/2/2/photo-11-16753199532651870361869.jpg"
        audio = "meme1.mp3"
        video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
with col3:
    lion = st.button("Con sư tử")
    if lion:
        name = "Con sư tử"
        info = "Đây là thông tin của con sư tử"
        image = "https://i.pinimg.com/736x/63/d3/7b/63d37bb57907e0cecdf1709f63b86f94.jpg"
        audio = "meme1.mp3"
        video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
with col4:
    horse = st.button("Con ngựa")
    if horse:
        name = "Con ngựa"
        info = "Đây là thông tin của con ngựa"
        image = "https://theselfishmeme.co.uk/wp-content/uploads/2025/12/meme-con-ngua-cuoi-5.webp"
        audio = "meme1.mp3"
        video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
with col5:
    eagle = st.button("Con thiên nga")
    if eagle:
        name = "Con thiên nga"
        info = "Đây là thông tin của con thiên nga"
        image = "thiennga.png"
        video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"

with st.sidebar:
    st.header("Trắc nghiệm tính cách")
    st.write(f"Con vật bạn chọn là con {name}") 
    
with st.expander(name):
    st.write(info)
    if image:
        st.image(image, caption="Con vật bạn chọn")
    if audio:
        st.audio(audio, format="audio/mp3")
    if video:
        st.video(video, format="video/mp4")