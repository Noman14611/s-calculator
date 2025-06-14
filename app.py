import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.title("🧮 Scientific Calculator")

operation = st.selectbox("Select operation", [
    "Addition", "Subtraction", "Multiplication", "Division",
    "Power (x^y)", "Square Root (√x)",
    "Logarithm (log10)", "Trigonometry (sin, cos, tan)"
])

if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power (x^y)"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    if st.button("Calculate"):
        if operation == "Addition":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtraction":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiplication":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Division":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Error: Division by zero.")
        elif operation == "Power (x^y)":
            st.success(f"Result: {math.pow(num1, num2)}")

elif operation == "Square Root (√x)":
    num = st.number_input("Enter a number", value=0.0)
    if st.button("Calculate"):
        if num >= 0:
            st.success(f"Result: {math.sqrt(num)}")
        else:
            st.error("Error: Negative number.")

elif operation == "Logarithm (log10)":
    num = st.number_input("Enter a number", value=1.0)
    if st.button("Calculate"):
        if num > 0:
            st.success(f"Result: {math.log10(num)}")
        else:
            st.error("Error: Log undefined for zero or negative numbers.")

elif operation == "Trigonometry (sin, cos, tan)":
    angle = st.number_input("Enter angle in degrees", value=0.0)
    rad = math.radians(angle)
    if st.button("Calculate"):
        st.success(f"sin({angle}) = {math.sin(rad)}")
        st.success(f"cos({angle}) = {math.cos(rad)}")
        st.success(f"tan({angle}) = {math.tan(rad)}")
