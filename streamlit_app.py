import streamlit as st

st.title("Student Grade Predictor")


st.write("Enter your marks to estimate the grade")

math = st.slider("Math Marks", 0, 100)
science = st.slider("Science Marks", 0, 100)
english = st.slider("English Marks", 0, 100)

average = (math + science + english) / 3

if st.button("Calculate Grade"):

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    st.success(f"Average Marks: {average:.2f}")
    st.info(f"Predicted Grade: {grade}")
