import streamlit as st

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


if 'total_score' not in st.session_state.keys():
    st.switch_page("./pages/pagina_accoglienza.py")

if 'clicked_3' not in st.session_state:
    st.session_state.clicked_3 = True

def click_button():
    st.session_state.clicked_3 = False

if 'disable_choices_3' not in st.session_state:
    st.session_state.disable_choices_3 = False

def disable_choices():
    st.session_state.disable_choices_3 = True

# define question dictionary

quest_dict = {
              "question":"In che anno è nata Acus?",
              "options":['2008','2010','2012','2015'],
              "correct_answer":"2008",
              "explanation":"Acus nasce nel 2008 come startup all'interno dell'Incubatore del Politecnico di Torino. Fin da allora lavora esclusivamente nel mercato energy&utilities",
              "score":10}

css_code = f"""
<style>
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] p {{
        font-size: 16px !important; /* Imposta la dimensione del font desiderata */
    }}
</style>
"""

# 3. Inietta il CSS nella pagina
st.markdown(css_code, unsafe_allow_html=True)


bar_placeholder = st.empty()
question_placeholder = st.empty()
options_placeholder = st.empty()
results_placeholder = st.empty()
expander_area = st.empty()
nl(1)
button_placeholder = st.empty()

bar_placeholder.progress(60, text='3 di 5')


# Text Prompt
# question_placeholder.write(quest_dict["question"])
question = f'<p style="font-size: 32px;">{quest_dict["question"]}</p>'
question_placeholder.write(
    question, unsafe_allow_html=True
                           )


choices = options_placeholder.radio("Scegli una risposta:", quest_dict["options"], index = None, on_change=click_button, disabled= st.session_state.disable_choices_3, label_visibility='collapsed')

check_button = button_placeholder.button("Check", disabled = st.session_state.clicked_3, on_click=disable_choices)


if not st.session_state.get('button'):

    st.session_state['button'] = check_button

if st.session_state['button']:

    if choices == quest_dict["correct_answer"]:
        results_placeholder.success("CORRETTO")
        # st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]
    else:
        results_placeholder.error("SBAGLIATO")
    # Explanation of the Answer
    expander_area.write(f"*{quest_dict["explanation"]}*")

    switch_page = button_placeholder.button("Prossimo")

    if switch_page:
        # Switch to the selected page
        page_file = "./pages/domanda_4.py"
        st.session_state['button'] = False

        if choices == quest_dict["correct_answer"]:
            st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]

        st.switch_page(page_file)












