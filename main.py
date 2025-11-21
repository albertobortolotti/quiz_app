# --- INIZIO CODICE main.py ---

import streamlit as st

pages = [
        st.Page("./pages/pagina_accoglienza.py", default=True),
        st.Page("./pages/domanda_1.py"),
        st.Page("./pages/domanda_2.py"),
        st.Page("./pages/punteggio_finale.py")
    ]

pg = st.navigation(pages,position="hidden")

pg.run()

# --- FINE CODICE main.py ---
