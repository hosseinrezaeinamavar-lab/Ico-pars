import streamlit as st
import pandas as pd

def show():
    st.title('داشبورد بازرسی - دیتاپژوه پارسا')
    st.write('ثبت نتایج بازدید و ممیزی')
    df = pd.DataFrame({
        'تاریخ': ['1404/07/01', '1404/07/15', '1404/08/01'],
        'واحد': ['فروش', 'مالی', 'عملیات'],
        'امتیاز': [8.5, 7.2, 9.1]
    })
    st.dataframe(df)
