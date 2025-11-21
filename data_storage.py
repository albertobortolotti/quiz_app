# --- INIZIO CODICE data_storage.py ---

import json
import os
from datetime import datetime

DATA_FILE = "quiz_data_archive.json"

def load_data():
    """Carica i dati esistenti dal file JSON."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Restituisce una struttura vuota se il file è corrotto
                return {}
    return {}

def save_data(data):
    """Salva i dati nel file JSON."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def initialize_session(email):
    """Inizializza una nuova sessione nel file di archivio."""
    data = load_data()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Usa l'email come chiave principale per l'archiviazione
    if email not in data:
        data[email] = []
    
    # Crea un ID di sessione univoco (timestamp)
    session_id = timestamp
    
    new_session = {
        "session_id": session_id,
        "start_time": timestamp,
        "email": email,
        "answers": {},
        "score": 0
    }
    
    data[email].append(new_session)
    save_data(data)
    
    # Restituisce l'ID della sessione per tracciare le risposte
    return session_id

def update_session_answer(email, session_id, question_id, answer, is_correct, score_awarded):
    """Aggiorna una risposta specifica nella sessione."""
    data = load_data()
    
    if email in data:
        for session in data[email]:
            if session.get("session_id") == session_id:
                session["answers"][question_id] = {
                    "answer": answer,
                    "is_correct": is_correct,
                    "score_awarded": score_awarded
                }
                save_data(data)
                return True
    return False

def update_session_score(email, session_id, final_score):
    """Aggiorna il punteggio finale della sessione."""
    data = load_data()
    
    if email in data:
        for session in data[email]:
            if session.get("session_id") == session_id:
                session["score"] = final_score
                session["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_data(data)
                return True
    return False

# Funzione di utilità per visualizzare l'archivio (non usata nel quiz, ma utile per il debug)
def view_archive():
    """Stampa il contenuto dell'archivio."""
    data = load_data()
    print(json.dumps(data, indent=4))

# --- FINE CODICE data_storage.py ---
