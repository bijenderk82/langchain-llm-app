import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Hamster", "Rat", "Snake", "Lizard", "Cow"))

print(animal_type)

if animal_type == "Dog":
    pet_color = st.sidebar.text_area(
    label="What color is your dog?",
    max_chars=15
)
    
    if animal_type == "Cat":
      pet_color = st.sidebar.text_area(
    label="What color is your cat?",
    max_chars=15
    )

if animal_type == "Hamster":
  pet_color = st.sidebar.text_area(
    label="What color is your hamster?",
    max_chars = 15
    )

if animal_type == "Rat":
  pet_color = st.sidebar.text_area(label="What color is your rat?", max_chars = 25)

if animal_type == "Snake":
  pet_color = st.sidebar.text_area(label="What color is your snake?", max_chars = 25)

if animal_type == "Lizard":
  pet_color = st.sidebar.text_area(
    label="What color is your lizard?",
    max_chars = 25
    )

if animal_type == "Cow":
  pet_color = st.sidebar.text_area(label="What color is your cow?", max_chars = 25)
 
  
if pet_color:
    response = lch.generate_pet_names(animal_type, pet_color)
    st.text(response['pet_name'])
