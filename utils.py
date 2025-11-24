import streamlit as st
from PIL import Image
import re
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

# Funzione per inviare email con i risultati
def send_results_email(user_email, answers=None, score=None):
    """
    Invia i risultati del quiz via email
    """
    try:
        # Credenziali email dal secrets
        smtp_server = st.secrets["email"]["smtp_server"]
        smtp_port = st.secrets["email"]["smtp_port"]
        sender_email = st.secrets["email"]["sender_email"]
        sender_password = st.secrets["email"]["sender_password"]
        recipient_email = st.secrets["email"]["recipient_email"]
        
        # Crea il messaggio
        message = MIMEMultipart("alternative")
        message["Subject"] = f"Nuova risposta al Quiz - {user_email}"
        message["From"] = sender_email
        message["To"] = recipient_email
        
        # Prepara il contenuto
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Corpo del messaggio in formato testo
        text_content = f"""
Nuova risposta al quiz ricevuta!

Data e ora: {timestamp}
Email partecipante: {user_email}

Risposte:
- Domanda 1: {answers.get('domanda_1', 'Non risposta') if answers else 'Non risposta'}
- Domanda 2: {answers.get('domanda_2', 'Non risposta') if answers else 'Non risposta'}
- Domanda 3: {answers.get('domanda_3', 'Non risposta') if answers else 'Non risposta'}
- Domanda 4: {answers.get('domanda_4', 'Non risposta') if answers else 'Non risposta'}
- Domanda 5: {answers.get('domanda_5', 'Non risposta') if answers else 'Non risposta'}

Punteggio totale: {score if score is not None else 0}/5

---
Email inviata automaticamente dal sistema Quiz Aziendale
        """
        
        # Corpo del messaggio in formato HTML
        html_content = f"""
        <html>
          <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
              <h2 style="color: #0066cc; border-bottom: 2px solid #0066cc; padding-bottom: 10px;">
                Nuova risposta al quiz ricevuta!
              </h2>
              
              <div style="background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <p><strong>Data e ora:</strong> {timestamp}</p>
                <p><strong>Email partecipante:</strong> {user_email}</p>
              </div>
              
              <h3 style="color: #0066cc;">Risposte:</h3>
              <ul style="list-style-type: none; padding: 0;">
                <li style="padding: 8px; background-color: #f9f9f9; margin: 5px 0; border-left: 3px solid #0066cc;">
                  <strong>Domanda 1:</strong> {answers.get('domanda_1', 'Non risposta') if answers else 'Non risposta'}
                </li>
                <li style="padding: 8px; background-color: #f9f9f9; margin: 5px 0; border-left: 3px solid #0066cc;">
                  <strong>Domanda 2:</strong> {answers.get('domanda_2', 'Non risposta') if answers else 'Non risposta'}
                </li>
                <li style="padding: 8px; background-color: #f9f9f9; margin: 5px 0; border-left: 3px solid #0066cc;">
                  <strong>Domanda 3:</strong> {answers.get('domanda_3', 'Non risposta') if answers else 'Non risposta'}
                </li>
                <li style="padding: 8px; background-color: #f9f9f9; margin: 5px 0; border-left: 3px solid #0066cc;">
                  <strong>Domanda 4:</strong> {answers.get('domanda_4', 'Non risposta') if answers else 'Non risposta'}
                </li>
                <li style="padding: 8px; background-color: #f9f9f9; margin: 5px 0; border-left: 3px solid #0066cc;">
                  <strong>Domanda 5:</strong> {answers.get('domanda_5', 'Non risposta') if answers else 'Non risposta'}
                </li>
              </ul>
              
              <div style="background-color: #e8f4f8; padding: 15px; border-radius: 5px; margin: 20px 0; text-align: center;">
                <h3 style="color: #0066cc; margin: 0;">Punteggio totale: {score if score is not None else 0}/5</h3>
              </div>
              
              <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
              <p style="font-size: 12px; color: #999; text-align: center;">
                Email inviata automaticamente dal sistema Quiz Aziendale
              </p>
            </div>
          </body>
        </html>
        """
        
        # Aggiungi entrambe le versioni del messaggio
        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")
        message.attach(part1)
        message.attach(part2)
        
        # Invia l'email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Sicurezza TLS
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        return True
        
    except Exception as e:
        st.error(f"Errore nell'invio dell'email: {e}")
        return False

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
