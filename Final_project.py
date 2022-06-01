from email.utils import collapse_rfc2231_value
from sre_constants import SUCCESS
import streamlit as st
import streamlit_book as stb
#Add some Text 

st.write("This is Killer Mike")
st.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")
st.button("Click Here if you like Mike")
st.balloons()
st.checkbox("I agree")
col1,col2,col3,col4,col5,col6 = st.columns(6)
col1.write("This is Column 1")
col1.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")
col1.button("Do you like this picture")
col2.write("This is Column 2")
col2.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")
col3.write("This is Column 3")
col3.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")
col4.write("This is Column 4")
col4.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")

col5.write("This is Column 5")
col5.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")
col6.write("This is Column 6")
col6.image("Killer_Mike_photo_by_Dan_Medhurst.jpg")
stb.true_or_false("Is Mike a rapper", True,
                  success ="You got it right",
                  error = "Try Again",
                  button= "Please Select")
stb.single_choice("What is kind of car does Mike drive", ["Ford", "Chevy", "Mazda","Saab"],
                                                         2, 
                                                         success= 'Correct. Mike would not drive anything else', 
                                                         error= "Mike would never drive that",
                                                         button= "Pick one")
stb.multiple_choice("What type of business does Mike  Own",
                    {"Barbershop":True,
                    "Arcade": False,
                    "Bank":True,
                    "Resturant":True,
                    "Rental Car Agency" :False,
                    },
                    success="Damn Right",
                    error= "Come On, Really!, Try again",
                    button= "Choose all that apply")
                    