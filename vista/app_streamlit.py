import streamlit as st
from lexico.lexer import prueba

def main():
    st.title("Analizador Léxico con Streamlit")

    data = st.text_area("Ingrese el código:")
    
    if st.button("Analizar"):
        resultados_validos, errores = prueba(data)
        
        # Mostrar resultados válidos
        st.write("Resultados Válidos:")
        for res in resultados_validos:
            st.markdown(
                f'<div style="background-color:white; padding:10px; margin:10px; border-radius:10px;">{res}</div>',
                unsafe_allow_html=True,
            )

        # Mostrar errores
        st.write("Errores:")
        for error in errores:
            if isinstance(error, str):  # Asegurarse de que es una cadena antes de usar split()
                parts = error.split()
                st.markdown(
                    f'<div style="background-color:red; color:white; padding:10px; margin:10px; border-radius:10px;">{parts}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.write(f"Error de formato inesperado: {error}")

if __name__ == "__main__":
    main()
