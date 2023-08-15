import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')
st.write('Display Image')
st.write('プログレスバーの表示')
'Start!'
""" latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(1)
'Done!!!'
if st.checkbox('Show Image'):
    img=Image.open('dubai.png')
    st.image(img, caption='Shigehiro Yoshikawa', use_column_width=True) """
""" left_column,right_column = st.beta_columns(2)
#left_column,right_column=st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム') """

expander=st.beta_expander('問い合わせ')
expnader.write('問い合わせを書く')

""" text=st.sidebar.text_input('あなたの趣味を教えて下さい。')
cond=st.sidebar.slider('あなたの調子は？',0,100,50) """
'あなたの趣味：', text
'コンディション：', cond
""" #df=pd.DataFrame({
   # '1列目':[1, 2, 3 ,4],
   # '2列目':[10, 20, 30 ,40],
#})
#st.table(df.style.highlight_max(axis=1)) """

