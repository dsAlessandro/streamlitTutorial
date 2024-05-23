import streamlit as st
import utils.utils
import pandas as pandas
#ogni tab ha una funzione separata

def create_tab_prodotti(tab_prodotti):
    col1, col2, col3 = tab.prodotti.columns(3)
    col1.write("Prova 1")
    payment_info = execute_query(st.session_state["connection"], "SELECT SUM(amount) AS 'Total Amount', MAX(amount) as 'Max Payment', AVG(amount) as 'Average Payment', FROM payments;")
    payment_info_dict = [dict(zip(payment_info.keys(), result)) for result in payment_info]




if __name__ == "__main__":
    st.title("Analisi")

    #creazione dei tab distinti
    tab_prodotti, tab_staff, tab_clienti = st.tabs(["Prodotti", "Staff", "Clienti"])

    if check_connection():
        create_tab_prodotti(tab_prodotti)

