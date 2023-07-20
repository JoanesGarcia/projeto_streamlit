import streamlit as st

if "logado" not in st.session_state:
    st.session_state["logado"] = False

st.set_page_config(
    page_title="Meu App Personalizado",
    layout="centered",
    initial_sidebar_state="auto"  # Defina como "collapsed" para iniciar com a barra lateral recolhida
)

def verificar_credenciais(usuario, senha):
    return usuario == "usuario" and senha == "senha12333"

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
        st.title("Login")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Login"):
            if verificar_credenciais(usuario, senha):
                st.success("Login bem-sucedido!")
                st.session_state["logado"] = True
                st.experimental_rerun()                
            else:
                st.error("Credenciais inválidas. Tente novamente.")
    else:
        libera_acesso()
   
if __name__ == "__main__":
    main()
