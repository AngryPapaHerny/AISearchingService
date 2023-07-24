import streamlit as st
import bardapi 
# from bardapi import Bard

# token = st.secrets["bard_api"]

theme = st.sidebar.radio('테마',['default','dark'])
option = st.sidebar.selectbox(
    'Menu',
     ('검색', '멀티미디어', '기타'))
token = st.sidebar.text_input(
    label='BardToken', 
    placeholder='Token 값을 입력하세요.'
)


if option == '검색':
    st.title("인공지능 검색 서비스")
    
    response=''
    
    # tab1, tab2, tab3 = st.tabs(['answer1', 'answer2','answer3'])
    
    with st.form("form"):
        user_input = st.text_input("Prompt")
        submit = st.form_submit_button("Submit")

    if submit and user_input:
        with st.spinner("waiting..."):
            bard = bardapi.Bard(token)
            response = bard.get_answer(user_input)
      
    # with st.spinner("waiting..."):
    #     if submit and user_input:
    #         response = bardapi.Bard(token).get_answer(user_input)
           
    # st.write(response)

        answers=[]

    # try:
        # for i,choice in enumerate(response['choices']):
        for choice in response['choices']:
            answers.append(choice['content'][0])

        tab1, tab2, tab3 = st.tabs(['answer1', 'answer2','answer3'])

        with tab1:
            st.write(answers[0])
        with tab2:
            st.write(answers[1])
        with tab3:
            st.write(answers[2])
    # except:
    #     st.write("무엇을 도와드릴까요?")

elif option == '멀티미디어':
    st.title("페이지 2")

else : 
    st.title('페이지 3')
