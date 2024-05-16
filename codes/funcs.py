import base64
import streamlit as st
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center bottom;
        background-repeat: no-repeat;
        position: relative;
        width: 100%; /* Definir a largura para 100% */
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


def add_img_app(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center bottom;
        background-repeat: no-repeat;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


def add_bg_from_body(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    # String HTML com media query
    st.markdown(f"""
    <style>
      @media (min-width: 769px) {{
            .stApp {{
                background-image: url(data:image/png;base64,{encoded_string.decode()});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
              
              
            }}
        }}
    </style>
    """,unsafe_allow_html=True)

    # Renderiza o HTML no Streamlit

