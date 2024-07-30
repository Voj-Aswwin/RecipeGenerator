import streamlit as st
import langchain_helper


st.title("Recipe Generator")
vegetable = st.sidebar.selectbox("Pick a Vegetable", ("Tomato", "Brinjal", "Carrot", "Beatroot", "Raddish"))
food_style = st.sidebar.selectbox("Pick a Style", ("Gravy for Rotis", "Shallow Fry for Rice", "Main Dish"))


if food_style:
    response = langchain_helper.generate_recipe(vegetable,food_style)
    st.header(response['dish_name'].strip())
    st.write(response['recipe'].strip())
    

