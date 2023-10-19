import json
import base64
import streamlit as st
from api import get_response

with open('data/texts.json', 'r') as json_file:
    text = json.load(json_file)


def reset_language(x):
    with open('data/language.txt', 'w') as file:
        file.write(x)


def main():
    st.set_page_config(
    page_title='My Live CV',
        layout='wide',
        page_icon='📈',
        initial_sidebar_state='expanded'
    )

    cols = st.sidebar.columns(5)
    if cols[0].button(':uk:'):
        reset_language('english')
    if cols[1].button(':it:'):
        reset_language('italian')
    if cols[2].button(':es:'):
        reset_language('spanish')

    with open('data/language.txt', 'r') as file:
        language = file.read()

    st.sidebar.image('data/Mugshot.png', width=300, clamp=False)
    st.sidebar.write(text['Sidebar Title'][language])
    st.sidebar.write(text['Sidebar Text'][language])

    col1, col2 = st.columns([0.7, 0.3])

    col1.title(text['Title'][language])
    col1.write(text['Small Text'][language])

    file_ = open("data/giphy.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    with col2.expander(text['Reaction'][language]):
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="mindblown gif">',
            unsafe_allow_html=True,
        )

    user_input = st.text_input(text['Write Here'][language])

    if user_input:
        with st.spinner(text['Loading'][language]):
            transformed_text = get_response(user_input, language)
        st.write(text['Response'][language])
        st.write(transformed_text)


if __name__ == "__main__":
    main()
