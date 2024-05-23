import streamlit as st
from sqlalchemy import create_engine, text

""" Raccogli le principali funzioni con divide dalle varie pagine"""


def connect_db(dialect, username, password, gost, dbname):
    try:
        engine=create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn=engine.connect()
        return conn
    except:
        return False

def excute_query(conn, query):
    return conn.execute(text(query))


def check:connection():
    if "connection" not in st.session:state.keys():
        st.session_state["connection"] = False

    if st.sidebar.button("Connettiti al DB") #restituisce True se il bottone è attivato
        myconnection = connect_db(dialect="mysql+pymysql",username="student",password="user_pwd",host="localhost",dbname="classicmodels") #le credenziali non dovrebbero mai essere messe nei codici, ma in file di testo appositi
        
        if myconnection is False:
            st.session_state["connection"] = myconnection
        
        else:
            st.session_state["connection"] = False
            st.sidebar.error("Errore nella connessione al DB")
