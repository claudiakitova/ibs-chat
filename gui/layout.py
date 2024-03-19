import streamlit as st

class Layout:

    def show_header(self):
        """
        Displays the header of the app
        """
        st.markdown(
            """
            <h1 style='text-align: center;'>БКС Ассистент 💬</h1>
            """,
            unsafe_allow_html=True,
        )

    def show_api_key_missing(self):
        """
        Displays a message if the user has not entered an API key
        """
        st.markdown(
            """
            <div style='text-align: center;'>
                <h4>Ваш ассистент в мире финансов</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        """
        Displays the prompt form
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="Задайте вопрос",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Спросить")

            is_ready = submit_button and user_input
        return is_ready, user_input