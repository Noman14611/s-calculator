import streamlit as st
import math

# Title
st.title("Casio Scientific Calculator")

# Display box
if "current_input" not in st.session_state:
    st.session_state.current_input = ""

# Button handlers
def add_input(key):
    st.session_state.current_input += key

def clear():
    st.session_state.current_input = ""

def calculate():
    try:
        st.session_state.result = eval(st.session_state.current_input, {"math": math, "__builtins__": {}} )
        st.session_state.current_input = str(st.session_state.result)
    except Exception as e:
        st.error(f"Error: {e}")

# Display
st.text_input("Expression", st.session_state.current_input, disabled=False, key='input_field')

# Buttons in grid
cols = st.columns(5)

with cols[0]:
    st.button("7", on_click=add_input, args=('7',))
    st.button("4", on_click=add_input, args=('4',))
    st.button("1", on_click=add_input, args=('1',))
    st.button("0", on_click=add_input, args=('0',))


with cols[1]:
    st.button("8", on_click=add_input, args=('8',))
    st.button("5", on_click=add_input, args=('5',))
    st.button("2", on_click=add_input, args=('2',))
    st.button(".", on_click=add_input, args=('.',))


with cols[2]:
    st.button("9", on_click=add_input, args=('9',))
    st.button("6", on_click=add_input, args=('6',))
    st.button("3", on_click=add_input, args=('3',))
    st.button(")", on_click=add_input, args=(')',))


with cols[3]:
    st.button("/", on_click=add_input, args=('/',))
    st.button("*", on_click=add_input, args=('*',))
    st.button("-", on_click=add_input, args=('-',))
    st.button("+", on_click=add_input, args=('+',))


with cols[4]:
    st.button("C", on_click=clear)
    st.button("sin(", on_click=add_input, args=('math.sin(',))
    st.button("cos(", on_click=add_input, args=('math.cos(',))
    st.button("=", on_click=calculate)


# Display result if exists
if "result" in st.session_state:
    st.success(f"Result: {st.session_state.result}")

# Footer
st.write("Casio Scientific Calculator - Streamlit")
