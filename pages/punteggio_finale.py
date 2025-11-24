import streamlit as st

message1_placeholder = st.empty()
message2_placeholder = st.empty()

    # Invia l'email con i risultati
    success = send_results_email(
        user_email=st.session_state['user_email'],
        answers=st.session_state['answers'],
        score=st.session_state['total_score']
    )

if st.session_state['total_score'] == 50:
    st.balloons()

    message1 = '''WOW! Sei un vero esperto di Acus! 🔥<br>
Hai superato il quiz alla grande: meriti il tuo super premio!<br>
Vieni al nostro stand a ritirare l’ombrello (speriamo non piova… ma nel dubbio meglio averlo 😎).'''

    message2 = '''Restiamo in contatto:<br>
🔗 LinkedIn: <a href="https://www.linkedin.com/company/acus-s-p-a">www.linkedin.com/company/acus-s-p-a<a>'''


    message1_placeholder.write(f'<p style="font-size: 20px;">{message1}</p>', unsafe_allow_html=True)
    message2_placeholder.write(f'<p style="font-size: 20px;">{message2}</p>', unsafe_allow_html=True)

else:
    message1 = '''Oooh… per un soffio! 😅<br>
Hai sbagliato almeno una risposta, ma niente drammi: abbiamo per te un dolce premio di consolazione!<br>
Passa al nostro stand per ritirarlo.'''

    message2 = '''Seguici per rifarti la prossima volta:<br>
🔗 LinkedIn: <a href="https://www.linkedin.com/company/acus-s-p-a">www.linkedin.com/company/acus-s-p-a<a>'''



    message1_placeholder.write(f'<p style="font-size: 20px;">{message1}</p>', unsafe_allow_html=True)
    message2_placeholder.write(f'<p style="font-size: 20px;">{message2}</p>', unsafe_allow_html=True)

