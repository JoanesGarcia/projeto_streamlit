import streamlit as st

from login import Login

if "logado" not in st.session_state:
    st.session_state["logado"] = False

st.set_page_config(
    page_title="Meu App Personalizado",
    layout="centered",
    initial_sidebar_state="auto"  # Defina como "collapsed" para iniciar com a barra lateral recolhida
)

def libera_acesso():
    st.sidebar.title("Menu")
    pagina_selecionada = st.sidebar.selectbox("Selecione uma página:", ["Página 1", "Página 2", "Página 3"])

    if pagina_selecionada == "Página 1":
        st.title("Conteúdo da Página 1")
    elif pagina_selecionada == "Página 2":
        st.title("Conteúdo da Página 2")

def main():
    print(st.session_state["logado"])
    if not st.session_state["logado"]:
        login = Login(st)
        login.logar(st)
    else:
        libera_acesso()
   
if __name__ == "__main__":
    main()
