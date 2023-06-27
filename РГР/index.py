import streamlit as st

PAGE_LAYOUT = "wide"
PAGE_TITLE = "# Расчетно-графическая работа"
SIDEBAR_INFO = "Выберите страницу"
PAGE_TEXT = """
    Это главная страница РГР по машинному обучению. 
    В боковом меню вы можете перейти на три страницы: 
    * Информация о датасете
    * Визуализации
    * Модели и предсказания
"""

st.set_page_config(layout=PAGE_LAYOUT)
st.write(PAGE_TITLE)
st.sidebar.info(SIDEBAR_INFO)
st.markdown(PAGE_TEXT)
