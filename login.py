from mongo_db import MongoDB

class Login():
    def __init__(self, st) -> None:
        self.usuario = "usuario"
        self.senha = "senha"
        self.client = MongoDB(st)

    def verificar_credenciais(self):        
        return self.client.get_login(self.usuario, self.senha)
    
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
