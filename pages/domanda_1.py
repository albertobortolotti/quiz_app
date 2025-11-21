import streamlit as st
import data_storage

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


if 'total_score' not in st.session_state.keys() or 'email' not in st.session_state.keys() or 'session_id' not in st.session_state.keys():
    st.switch_page("./pages/pagina_accoglienza.py")

if 'clicked_1' not in st.session_state:
    st.session_state.clicked_1 = True

def click_button():
    st.session_state.clicked_1 = False

if 'disable_choices_1' not in st.session_state:
    st.session_state.disable_choices_1 = False

def disable_choices():
    st.session_state.disable_choices_1 = True

# define question dictionary

quest_dict = {
              "question":"Quali sono i principali servizi offerti da Acus?",
              "options":['Solo software','Software + BPO + Consulenza','Software + Consulenza','Solo consulenza'],
              "correct_answer":"Software + BPO + Consulenza",
              "explanation":"Ideiamo e sviluppiamo software proprietari, affianchiamo i nostri clienti con consulenza organizzativa e di processo e offriamo servizi di BPO pensati per semplificare il lavoro quotidiano. Uniamo competenza tecnica e ascolto per costruire soluzioni realmente utili, su misura delle esigenze di chi lavora con noi.",
              "score":10}

bar_placeholder = st.empty()
question_placeholder = st.empty()
options_placeholder = st.empty()
results_placeholder = st.empty()
expander_area = st.empty()
nl(1)
button_placeholder = st.empty()

bar_placeholder.progress(20, text='1 di 5')


# Text Prompt
# question_placeholder.write(quest_dict["question"])
question = f'<p style="font-size: 32px;">{quest_dict["question"]}</p>'
question_placeholder.write(
    question, unsafe_allow_html=True
                           )


choices = options_placeholder.radio("Scegli una risposta:", quest_dict["options"], index = None, on_change=click_button, disabled= st.session_state.disable_choices_1, label_visibility='collapsed')

check_button = button_placeholder.button("Check", disabled = st.session_state.clicked_1, on_click=disable_choices)


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
        # Archivia la risposta prima di cambiare pagina
        question_id = "domanda_1"
        answer = choices
        is_correct = (choices == quest_dict["correct_answer"])
        score_awarded = quest_dict["score"] if is_correct else 0
        
        data_storage.update_session_answer(
            st.session_state['email'],
            st.session_state['session_id'],
            question_id,
            answer,
            is_correct,
            score_awarded
        )
        # Switch to the selected page
        page_file = "./pages/domanda_2.py"
        st.session_state['button'] = False

        if choices == quest_dict["correct_answer"]:
            st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]

        st.switch_page(page_file)











