import streamlit as st

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


if 'total_score' not in st.session_state.keys():
    st.switch_page("./pages/pagina_accoglienza.py")

if 'clicked_2' not in st.session_state:
    st.session_state.clicked_2 = True

def click_button():
    st.session_state.clicked_2 = False

if 'disable_choices_2' not in st.session_state:
    st.session_state.disable_choices_2 = False

def disable_choices():
    st.session_state.disable_choices_2 = True

# define question dictionary

quest_dict = {"header":"Domanda 2/5",
              "question":"Qual è la prima lettera dell'alfabeto?",
              "options":['a','b','c','d'],
              "correct_answer":"a",
              "explanation":"La a è la prima lettera dell'alfabeto",
              "score":10}

header_placeholder = st.empty()
question_placeholder = st.empty()
options_placeholder = st.empty()
results_placeholder = st.empty()
expander_area = st.empty()
nl(1)
button_placeholder = st.empty()

header_placeholder.header(quest_dict["header"])


# Text Prompt
question_placeholder.write(quest_dict["question"])

choices = options_placeholder.radio("Scegli una risposta:", quest_dict["options"], index = None, on_change=click_button, disabled= st.session_state.disable_choices_2)

check_button = button_placeholder.button("Check", disabled = st.session_state.clicked_2, on_click=disable_choices)


if not st.session_state.get('button'):

    st.session_state['button'] = check_button

if st.session_state['button']:

    if choices == quest_dict["correct_answer"]:
        results_placeholder.success("CORRETTO")
    else:
        results_placeholder.error("SBAGLIATO")
    # Explanation of the Answer
    expander_area.write(f"*{quest_dict["explanation"]}*")

    switch_page = button_placeholder.button("Prossimo")

    if switch_page:
        # Switch to the selected page
        page_file = "./pages/punteggio_finale.py"
        st.session_state['button'] = False

        if choices == quest_dict["correct_answer"]:
            st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]

        st.switch_page(page_file)



