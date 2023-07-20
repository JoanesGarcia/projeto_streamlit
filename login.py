
class Login():
    def __init__(self, usuario, senha) -> None:
        self.usuario = "usuario"
        self.senha = "senha"

    def verificar_credenciais(self):
        return self.usuario == "usuario" and self.senha == "senha12333"
    
    def logar(self, st):
        st.title("Login")
        self.usuario = st.text_input("Usuário")
        self.senha = st.text_input("Senha", type="password")

        if st.button("Login"):            
            if self.verificar_credenciais():
                st.success("Login bem-sucedido!")
                st.session_state["logado"] = True
                st.experimental_rerun()                
            else:
                st.error("Credenciais inválidas. Tente novamente.")
