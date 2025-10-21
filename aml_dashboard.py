import streamlit as st
import pandas as pd

def show():
    st.title('داشبورد AML - دیتاپژوه پارسا')
    st.write('مثال داده‌های مشکوک به پولشویی')
    data = pd.DataFrame({
        'مشتری': ['A', 'B', 'C'],
        'تراکنش(میلیون)': [12.5, 3.2, 8.7],
        'وضعیت': ['بررسی', 'پاک', 'مشکوک']
    })
    st.table(data)
