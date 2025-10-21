import streamlit as st
import numpy as np
import pandas as pd

def show():
    st.title('داشبورد مدیریت ریسک - دیتاپژوه پارسا')
    st.write('نمایش سطح ریسک مشتریان')
    df = pd.DataFrame({
        'مشتری': ['A', 'B', 'C', 'D'],
        'ریسک': np.random.rand(4)
    })
    st.bar_chart(df.set_index('مشتری'))
