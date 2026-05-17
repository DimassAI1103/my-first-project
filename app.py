import streamlit as st
import math

st.title("🧮 Калькулятор DimassAI")
op = st.selectbox("Операция:", ["+", "-", "*", "/", "^", "√"])
n1 = st.number_input("Первое число:", step=1.0)
if op != "√":
    n2 = st.number_input("Второе число:", step=1.0)
else:
    n2 = None

if st.button("Посчитать"):
    if op == "+": res = n1 + n2
    elif op == "-": res = n1 - n2
    elif op == "*": res = n1 * n2
    elif op == "/": res = n1 / n2 if n2 != 0 else "Деление на 0!"
    elif op == "^": res = n1 ** n2
    elif op == "√": res = math.sqrt(n1) if n1 >= 0 else "Ошибка"
    st.success(f"Результат: **{res}**")
