import streamlit as st
from PIL import Image
import re

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

# Funzione per validare l'email
def validate_email(email):
    """
    Valida l'email controllando che contenga @ e almeno un punto dopo la @
    """
    if not email:
        return False
    
    # Controlla presenza di @ e punto
    if '@' not in email or '.' not in email:
        return False
    
    # Controlla che ci sia almeno un punto dopo la @
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    if '.' not in parts[1]:
        return False
    
    # Pattern regex più completo per validazione email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Delete all the items in Session state (solo al primo caricamento)
if 'initialized' not in st.session_state:
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state['initialized'] = True
    st.session_state['total_score'] = 0
    st.session_state['user_email'] = ''
    st.session_state['answers'] = {}  # Dizionario per archiviare le risposte

# Open the image from the specified path
st.image("./config/Acus-logo-con-payoff-positivo.png", caption=None)

# Add space between the header and the next item
nl(1)

# Text Prompt
st.write("""Rispondi a questo quiz per avere l'opportunità di vincere un regalo!""")

nl(1)

# Input per l'email
email = st.text_input(
    "Inserisci la tua email:",
    value=st.session_state.get('user_email', ''),
    placeholder="esempio@email.com"
)

# Messaggio di errore/successo
email_valid = False
if email:
    if validate_email(email):
        st.success("✓ Email valida")
        email_valid = True
        st.session_state['user_email'] = email
    else:
        st.error("✗ Email non valida. Assicurati che contenga @ e un punto nel dominio")

nl(1)

# Button to switch page (attivo solo se l'email è valida)
switch_page = st.button("Inizia", disabled=not email_valid)

if switch_page and email_valid:
    # Salva l'email nello session state
    st.session_state['user_email'] = email
    # Switch to the selected page
    page_file = "./pages/domanda_1.py"
    st.switch_page(page_file)
