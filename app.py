import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.title("🔢 Scientific Calculator")

# Session state to store input
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to evaluate the expression safely
def safe_eval(expr):
    try:
        expr = expr.replace('^', '**')
        expr = expr.replace('√', 'math.sqrt')
        expr = expr.replace('log', 'math.log10')
        expr = expr.replace('sin', 'math.sin(math.radians')
        expr = expr.replace('cos', 'math.cos(math.radians')
        expr = expr.replace('tan', 'math.tan(math.radians')
        return eval(expr + (')' if 'radians' in expr else ''))
    except Exception:
        return "Error"

# Calculator layout using columns
buttons = [
    ['7', '8', '9', '/', 'sin'],
    ['4', '5', '6', '*', 'cos'],
    ['1', '2', '3', '-', 'tan'],
    ['0', '.', '^', '+', 'log'],
    ['(', ')', '√', 'C', '=']
]

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            if btn == "C":
                st.session_state.expression = ""
            elif btn == "=":
                result = safe_eval(st.session_state.expression)
                st.session_state.expression = str(result)
            else:
                st.session_state.expression += btn

# Show current expression
st.text_input("Expression", value=st.session_state.expression, key="display")
