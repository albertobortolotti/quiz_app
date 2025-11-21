# --- INIZIO CODICE pages/domanda_1.py ---

import streamlit as st
import data_storage # <--- AGGIUNTO

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


if 'total_score' not in st.session_state.keys() or 'email' not in st.session_state.keys() or 'session_id' not in st.session_state.keys(): # <--- MODIFICATO
    st.switch_page("./pages/pagina_accoglienza.py")

# ... (resto del codice originale)

    if switch_page:
        # Archivia la risposta prima di cambiare pagina # <--- AGGIUNTO
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
        ) # <--- FINE LOGICA AGGIUNTA
        
        # Switch to the selected page
        page_file = "./pages/domanda_2.py"
        st.session_state['button'] = False

        if choices == quest_dict["correct_answer"]:
            st.session_state['total_score'] = st.session_state['total_score'] + quest_dict["score"]

        st.switch_page(page_file)

# ... (resto del codice originale)
# --- FINE CODICE pages/domanda_1.py ---
