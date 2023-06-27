import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title('専門コース演習II 2023年6月21日の課題')
st.subheader('課題1: GradioExample.ipynbを応用し、二つの数字を受け取り足し算した結果を返すWebアプリを構築すること')

number_1 = st.number_input('最初の数字を入力してください', step=1, key='number_1')
number_2 = st.number_input('次の数字を入力してください',step=1, key='number_2')
st.write('２つの数字の和は ', number_1 + number_2, 'です')
st.subheader('課題2: GradioExample.ipynbを応用し、任意の文字列をブラウザから入力しstaff.txtに合致すれば「います」、合致しなければ「みつかりません」を出力するWebアプリを作成すること。')
uploaded_file = st.file_uploader("Add text file !")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data.split('\n'))
    text = st.text_input('任意の文字列をを入力してください')
    if st.button('Check for name'):
        if text in string_data.split('\n'):
            st.write('います')
        else:
            st.write('みつかりません')

