import streamlit as st

pages = [
        st.Page("./pages/pagina_accoglienza.py", default=True),
        st.Page("./pages/domanda_1.py"),
        st.Page("./pages/domanda_2.py"),
        st.Page("./pages/domanda_3.py"),
        st.Page("./pages/domanda_4.py"),
        st.Page("./pages/domanda_5.py"),
        st.Page("./pages/punteggio_finale.py")
    ]

pg = st.navigation(pages,position="hidden")

pg.run()

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

