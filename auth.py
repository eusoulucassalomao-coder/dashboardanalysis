
import streamlit as st

def login():
    """
    Función de autenticación simple.
    """
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("<h1 style='text-align: center;'>Acceso al Dashboard Profesional</h1>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            with st.form("login_form"):
                email = st.text_input("Correo electrónico")
                password = st.text_input("Contraseña", type="password")
                submit_button = st.form_submit_button("Entrar")

                if submit_button:
                    if email == "mvpteste" and password == "mvpteste33":
                        st.session_state.authenticated = True
                        st.success("¡Bienvenido!")
                        st.rerun()
                    else:
                        st.error("Correo o contraseña incorrectos")
        return False
    return True

def logout():
    st.session_state.authenticated = False
    st.rerun()
