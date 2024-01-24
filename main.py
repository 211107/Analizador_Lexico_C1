import streamlit as st
from lexico.lexer import prueba

def main():
    st.title("Analizador Léxico")

    data = st.text_area("Ingrese el código:")
    
    if st.button("Analizar"):
        resultado = prueba(data)
      
        st.table(resultado)
        
       

if __name__ == "__main__":
    main()