import streamlit as st
from bardapi.core import Bard

token = st.secrets["bard_api"]

theme = st.sidebar.radio('테마', ['default', 'dark'])
option = st.sidebar.selectbox('Menu', ('검색', '멀티미디어', '기타'))

if option == '검색':
    st.title("인공지능 검색 서비스")

    with st.form("form"):
        user_input = st.text_input("Prompt")
        submit = st.form_submit_button("Submit")

    if submit and user_input:
        with st.spinner("waiting..."):
            response = Bard(token).get_answer(user_input)

        try:
            answers = [choice['content'][0] for choice in response['choices']]
            num_tabs = min(len(answers), 3)
            tab1, tab2, tab3 = st.tabs([f'answer{i}' for i in range(1, num_tabs + 1)])

            for i in range(num_tabs):
                with globals()[f'tab{i+1}']:
                    st.write(answers[i])
        except (KeyError, IndexError):
            st.write("무엇을 도와드릴까요?")

elif option == '멀티미디어':
    st.title("페이지 2")

else:
    st.title('페이지 3')
