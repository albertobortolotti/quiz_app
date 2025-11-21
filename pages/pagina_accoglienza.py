import streamlit as st
from PIL import Image

# Importazione del nuovo modulo per l'archiviazione
import data_storage

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

# --- GESTIONE STATO DI SESSIONE INIZIALE ---
# Delete all the items in Session state, but keep 'email' and 'session_id' if they exist
if 'email' not in st.session_state or 'session_id' not in st.session_state:
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# Inizializzazione dello score
st.session_state['total_score'] = 0

# --- INTERFACCIA UTENTE (UI) ---

# Display the image
st.image("./config/Acus-logo-con-payoff-positivo.png", caption=None)

# Add space between the header and the next item
nl(1)

# Text Prompt
st.write("""Rispondi a questo quiz per avere l'opportunità di vincere un regalo!""")
nl(1)

# --- LOGICA DI VALIDAZIONE E NAVIGAZIONE ---

def navigate_to_domanda_1():
    # Poiché il bottone è abilitato solo se 'email_valid' è True,
    # qui possiamo eseguire direttamente la navigazione.
    st.switch_page("./pages/domanda_1.py")

def validate_email():
    email = st.session_state.email_input
    # Inizializza o resetta lo stato di validazione
    st.session_state['email_valid'] = False 

    # Esegui la validazione
    if email and '@' in email and '.' in email:
        st.session_state['email_valid'] = True
        st.session_state['email'] = email
        
        # Inizializza la sessione solo se non è già stata inizializzata
        if 'session_id' not in st.session_state:
            st.session_state['session_id'] = data_storage.initialize_session(email)
    
    # IMPORTANTE: NON CHIAMARE st.switch_page O st.rerun QUI!

# Campo di input email: on_change chiama la validazione
email_input = st.text_input(
    "Inserisci la tua email per iniziare:", 
    key="email_input", 
    on_change=validate_email
)

# Bottone per cambiare pagina
st.button(
    "Inizia",
    # Il bottone è DISABILITATO finché la validazione non ha successo
    disabled=not st.session_state.get('email_valid', False),
    on_click=navigate_to_domanda_1 # Usa il callback per la navigazione
)

# Messaggio di feedback
if st.session_state.get('email_valid'):
    st.success(f"Email registrata: {st.session_state['email']}")
elif st.session_state.get('email_input'):
    # Mostra l'errore solo se l'utente ha digitato qualcosa
    st.error("Inserisci un'email valida.")
