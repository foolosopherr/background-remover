import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout='wide')

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

def change_img(img):
    image = Image.open(img)
    col1, col2 = st.columns(2)
    col1.write('Original image')
    col1.image(image)

    transformed_image = remove(image)
    col2.write('Transformed Image')
    col2.image(transformed_image)

    st.download_button('Download transformed image', convert_image(transformed_image), 'transformed.png')

st.header('Background remover')

st.write('Upload your image')
option = st.selectbox('Upload image or take a webcam photo', ['Computer', 'Webcam'])
if option == 'Computer':
    img = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg'])
else:
    img = st.camera_input('Take a photo')

if img:
    change_img(img)
else:
    st.write('I am waiting...')