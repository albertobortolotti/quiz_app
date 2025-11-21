# --- INIZIO CODICE pages/pagina_accoglienza.py ---

import streamlit as st
from PIL import Image

# Importazione del nuovo modulo per l'archiviazione
import data_storage # <--- AGGIUNTO

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

# Delete all the items in Session state, but keep 'email' and 'session_id' if they exist
# Questo assicura che l'email e l'ID di sessione vengano mantenuti tra le pagine,
# ma vengano resettati solo se l'utente torna alla pagina di accoglienza per ricominciare.
if 'email' not in st.session_state or 'session_id' not in st.session_state: # <--- MODIFICATO
    for key in list(st.session_state.keys()):
        del st.session_state[key]

st.session_state['total_score'] = 0


# Open the image from the specified path
#image = Image.open(r"C:\Users\acus\PycharmProjects\Prova_GUI\images\Acus-logo-con-payoff-positivo.png""")


# with st.columns(3)[1]:
# Display the image with a caption in Streamlit
st.image("./config/Acus-logo-con-payoff-positivo.png", caption=None)


# Add space between the geader and the next item
nl(1)

# Text Prompt
st.write("""Rispondi a questo quiz per avere l'opportunità di vincere un regalo!""")
nl(1) # <--- AGGIUNTO

# --- NUOVA LOGICA DI VALIDAZIONE EMAIL ---
def validate_email(): # <--- AGGIUNTO
    email = st.session_state.email_input
    if email and '@' in email and '.' in email:
        st.session_state['email_valid'] = True
        st.session_state['email'] = email
        # Inizializza la sessione solo se non è già stata inizializzata
        if 'session_id' not in st.session_state:
            st.session_state['session_id'] = data_storage.initialize_session(email)
    else:
        st.session_state['email_valid'] = False

email_input = st.text_input("Inserisci la tua email per iniziare:", key="email_input", on_change=validate_email) # <--- AGGIUNTO on_change

# choices = st.radio("Scegli una risposta:", ['c','d','a','pippo'], index = None)

# Button to switch page
switch_page = st.button("Inizia", disabled=not st.session_state.get('email_valid', False)) # <--- MODIFICATO

# Messaggio di feedback
if st.session_state.get('email_valid'): # <--- AGGIUNTO
    st.success(f"Email registrata: {st.session_state['email']}")
elif st.session_state.get('email_input'):
    st.error("Inserisci un'email valida.")

if switch_page and st.session_state.get('email_valid'): # <--- MODIFICATO
    # Switch to the selected page
    page_file = "./pages/domanda_1.py"
    st.switch_page(page_file)

# ... (resto del codice originale)
# --- FINE CODICE pages/pagina_accoglienza.py ---
