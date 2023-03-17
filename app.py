import streamlit as st
import numpy as np
import tensorflow as tf
# import cv2
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

CLASS_TO_CHAR = {0 : "1", 
                 1 : "2", 
                 2 : "3", 
                 3 : "4",
                 4 : "5",
                 5 : "6",
                 6 : "7",
                 7 : "8",
                 8 : "9",
                 9 : "A",
                 10 : "B",
                 11 : "C",
                 12 : "D",
                 13 : "E",
                 14 : "F",
                 15 : "G",
                 16 : "H",
                 17 : "I",
                 18 : "J",
                 19 : "K",
                 20 : "L",
                 21 : "M",
                 22 : "N",
                 23 : "O",
                 24 : "P",
                 25 : "Q",
                 26 : "R",
                 27 : "S",
                 28 : "T",
                 29 : "U",
                 30 : "V",
                 31 : "W",
                 32 : "X",
                 33 : "Y",
                 34 : "Z"}

def preprocessing(img):
    img = Image.fromarray(img)
    img = img.resize((224, 224))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    img = img/255
    return img

st.title("Indian Sign Language Recognition")
st.set_option('deprecation.showfileUploaderEncoding', False)
nav = st.sidebar.radio("Navigation", ["Home"])

uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    up_img = Image.open(uploaded_file)
    st.image(up_img, width=100)

if st.button("Predict Now"):
    try:
        img = np.asarray(up_img)
        img = preprocessing(img)
        model :tf.keras.models.Model = tf.keras.models.load_model("./Models/model_1_aug.h5")
        prediction = model.predict(img)
        img_class = CLASS_TO_CHAR[int(np.argmax(prediction, axis=1))]
        st.success("Predicted sign : {}".format(img_class))

    except Exception as e:
        st.error("Connection Error - \n{}".format(e))