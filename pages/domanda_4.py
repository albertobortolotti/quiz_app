import streamlit as st

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


if 'total_score' not in st.session_state.keys():
    st.switch_page("./pages/pagina_accoglienza.py")

if 'clicked_4' not in st.session_state:
    st.session_state.clicked_4 = True

def click_button():
    st.session_state.clicked_4 = False

if 'disable_choices_4' not in st.session_state:
    st.session_state.disable_choices_4 = False

def disable_choices():
    st.session_state.disable_choices_4 = True

# define question dictionary

quest_dict = {
              "question":"Quale di queste attività NON è gestita dai software Acus?",
              "options":['Riconciliare ciclo attivo e ciclo passivo','Gestire il Sistema Indennitario (CMOR)','Gestire lo scambio pratiche UDD–Reseller','Fare forecasting predittivo dei consumi'],
              "correct_answer":"Fare forecasting predittivo dei consumi",
              "explanation":'''*I software di Acus gestiscono le seguenti problematiche:*
- *Acuphi: riconciliare ciclo attivo e ciclo passivo (importi, misure e volumi)*
- *Acusim: gestire il sistema indennitario*
- *Aculink: portale reseller*
- *Acuflow: automazione flussi filiera energy&utilities*''',
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

bar_placeholder.progress(80, text='4 di 5')


# Text Prompt
# question_placeholder.write(quest_dict["question"])
question = f'<p style="font-size: 32px;">{quest_dict["question"]}</p>'
question_placeholder.write(
    question, unsafe_allow_html=True
                           )


choices = options_placeholder.radio("Scegli una risposta:", quest_dict["options"], index = None, on_change=click_button, disabled= st.session_state.disable_choices_4, label_visibility='collapsed')

check_button = button_placeholder.button("Check", disabled = st.session_state.clicked_4, on_click=disable_choices)


if not st.session_state.get('button'):

    st.session_state['button'] = check_button

if st.session_state['button']:

    if choices == quest_dict["correct_answer"]:
        results_placeholder.success("CORRETTO")
        # st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]
    else:
        results_placeholder.error("SBAGLIATO")
    # Explanation of the Answer
    expander_area.write(f"{quest_dict["explanation"]}")

    switch_page = button_placeholder.button("Prossimo")

    if switch_page:
        # Switch to the selected page
        page_file = "./pages/domanda_5.py"
        st.session_state['button'] = False

        if choices == quest_dict["correct_answer"]:
            st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]

        st.switch_page(page_file)












