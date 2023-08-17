import streamlit as st
import base64
from _4_1_UI_predict import feedback
from _4_2_UI_login import log_in
from _4_3_UI_text import instruction, about

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
  
def main():
    global menu, choice
    set_background('background.png')
    menu = ["Introduction","Home","Feedback","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'Feedback':
        feedback()
    
    elif choice == 'Introduction':
        instruction()
    elif choice == 'About':
        st.title("This is a mini Project for DAP391m")
        about()
    elif choice == 'Home':
        log_in()

if __name__ == "__main__":
    with open('feedback.txt','a+',encoding='utf-8') as file_feedback:
        pass
    main()
