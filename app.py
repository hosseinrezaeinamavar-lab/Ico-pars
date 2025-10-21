import streamlit as st
import datetime
from license_manager import check_license
from dashboards import aml_dashboard, risk_dashboard, inspection_dashboard

st.set_page_config(page_title='دیتاپژوه پارسا SaaS', layout='wide')

st.sidebar.title('ورود شرکت')
company = st.sidebar.text_input('نام شرکت')
submit = st.sidebar.button('تأیید')

licenses = {
    'ParsaRisk': datetime.date(2025, 12, 31),
    'DemoCo': datetime.date(2025, 11, 30)
}

if submit:
    if check_license(company, licenses):
        st.success(f'مجوز شرکت {company} معتبر است.')
        option = st.sidebar.selectbox('انتخاب داشبورد', ['AML', 'مدیریت ریسک', 'بازرسی'])
        if option == 'AML':
            aml_dashboard.show()
        elif option == 'مدیریت ریسک':
            risk_dashboard.show()
        elif option == 'بازرسی':
            inspection_dashboard.show()
    else:
        st.error('مجوز شرکت نامعتبر یا منقضی است.')
