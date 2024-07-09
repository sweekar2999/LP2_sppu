import streamlit as st
bot_name="College_Buddy"

knowledge_base = {

    "what is your name?" : [
        f"My name is {bot_name}! \n Happy to help you out with your College enquiries!"
    ],

    "hello": [
        f"Hello my name is {bot_name}! \n Happy to help you out with your College enquiries!"
    ],

    "what are the best colleges from pune?": [
        "COEP",
        "PICT",
        "VIT",
        "CUMMINS",
        "PCCOE"
    ],

    "which are  the best engineering branches?": [
        "Computer Engineering",
        "IT Engineering",
        "ENTC Engineering"
    ],

    "what are the top branch cut-offs for coep?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2 percentile",
    ],   

    "what are the top branch cut-offs for pict?" : [
        "Computer Engineering : 99.4 percentile",
        "IT Engineering : 98.6 percentile",
        "ENTC Engineering: 97.2 percentile",
    ],  

    "what are the top branch cut-offs for vit?" : [
        "Computer Engineering : 99.8 percentile",
        "IT Engineering: 97.1 percentile",
        "ENTC Engineering: 96.2 percentile",
    ],    

    "what are the top branch cut-offs for cummins?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2",
    ],  

    "what are the top branch cut-offs for pccoe?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2",
    ], 

    "When do college admissions start?": [
        "Admissions generally start around August",
    ],
   
}
st.header("College Buddy HERE!")
def respond(input:str):
 if (input in knowledge_base):
  print(input)
  values=knowledge_base[input]
  for value in values:
   st.write(value)
 else:
  print(input)
  st.write("sorry")
  key=input
  answer=st.text_input("Answer")
  add=st.button("add")
  if (add):
   knowledge_base[key] = [answer]
if __name__=="__main__":
 input=st.text_input("query here")
 col1,col2= st.columns([1,0.1])
 with col1:
  ask=st.button("ask")
 with col2:
  quit=st.button("quit")
 if(ask):
  respond(inout)
 if(quit):
  st.write("yhak u")













