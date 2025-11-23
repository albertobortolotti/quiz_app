import streamlit as st
from PIL import Image

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]

st.session_state['total_score'] = 0


# Open the image from the specified path
#image = Image.open(r"C:\Users\acus\PycharmProjects\Prova_GUI\images\Acus-logo-con-payoff-positivo.png""")


# with st.columns(3)[1]:
# Display the image with a caption in Streamlit
st.image("./config/Acus-logo-con-payoff-positivo.png", caption=None)


# Add space between the geader and the next item
nl(1)

# Text Prompt
st.write("""Rispondi a questo quiz per avere l'opportunità di vincere un regalo!""")



# choices = st.radio("Scegli una risposta:", ['c','d','a','pippo'], index = None)

# Button to switch page
switch_page = st.button("Inizia")
if switch_page:
    # Switch to the selected page
    page_file = "./pages/domanda_1.py"
    st.switch_page(page_file)

# results_placeholder = st.empty()

##Results Feedback
# if choices == 'c':
#     results_placeholder.success("CORRECT")
# else:
#     results_placeholder.error("INCORRECT")

# # Global Elements
# vspace = "\n"
#
# # page layout
# # st.set_page_config(layout='centered', initial_sidebar_state='collapsed')
#
# # # styling the webpage
# # # Set custom CSS using the style.css file
# # def set_custom_style():
# #     with open("style.css") as f:
# #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# # # Call the function to set custom style
# # set_custom_style()
#

#
# # Placeholder will come in handy in the App
# content_placeholder = st.empty()
# body_placeholder = st.empty()
#
# # layout of our landing pages of each section of the App
# def set_landing_page(page_title = True):
#     if page_title is False:
#         content_placeholder.empty()
#         body_placeholder.empty()
#     else:
#         content_placeholder.empty()
#         content_placeholder.header(page)
#         body_placeholder.empty()
#
#
# def test_your_knowledge(val=False):
#     if val == True:
#         global page
#         page = "Test Your Knowledge"
#         set_landing_page()
#         import quiz
#         nl(1)
#         st.markdown(f"""
#         *How conversant are you with OAU Sports ?
#         What do you know about the history of sports on OAU campus ?*
#         *How current and up-to-date are you? Test your knowledge with ten (10) randomly generated questions!*
#         \n*In a later update, the point scheme and at the end of the quiz, you may see how you rank on the leaderboard.*
#
#         Instructions:
#         1. The questions load with all answers default to Option B, kindly
#         select your answers by changing clicking on the radio button or
#         leaving it at the default (if applicable)
#
#         2. The question pool contain 1000+ questions on OAU Sports cutting
#         across Football (majorly), other sports and general questions.
#
#         3. All Questions do not carry equal points:
#         General Questions(5pts)     Women Sports(3pts)
#         Football Questions(2.5pts)  Other Sports(2.5pts)
#
#         4. The quiz is not time-bound.
#
#         """)
#
#         scorecard_placeholder = st.empty()
#         nl(2)
#         # Acrivate Session States
#         ss = st.session_state
#         # Initializing Session States
#         if 'counter' not in ss:
#             ss['counter'] = 0
#         if 'start' not in ss:
#             ss['start'] = False
#         if 'stop' not in ss:
#             ss['stop'] = False
#         if 'refresh' not in ss:
#             ss['refresh'] = False
#         if "button_label" not in ss:
#             ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
#         if 'current_quiz' not in ss:
#             ss['current_quiz'] = {}
#         if 'user_answers' not in ss:
#             ss['user_answers'] = []
#         if 'grade' not in ss:
#             ss['grade'] = 0
#
#         # Function for button click
#         def btn_click():
#             ss.counter += 1
#             if ss.counter > 2:
#                 ss.counter = 0
#                 ss.clear()
#             else:
#                 update_session_state()
#                 with st.spinner("*this may take a while*"):
#                     time.sleep(2)
#
#         # Function to update current session
#         def update_session_state():
#             if ss.counter == 1:
#                 ss['start'] = True
#                 ss.current_quiz = random.sample(quiz.sport_questions, 10)
#             elif ss.counter == 2:
#                 # Set start to False
#                 ss['start'] = True
#                 # Set stop to True
#                 ss['stop'] = True
#             elif ss.counter == 3:
#                 # Deactivate start & stop by setting them to False
#                 ss['start'] = ss['stop'] = False
#                 # Activate refresh to True
#                 ss['refresh'] = True
#                 ss.clear()
#
#         # Function to display a question
#         def quiz_app():
#             # create container
#             with st.container():
#                 if (ss.start):
#                     for i in range(len(ss.current_quiz)):
#                         number_placeholder = st.empty()
#                         question_placeholder = st.empty()
#                         options_placeholder = st.empty()
#                         results_placeholder = st.empty()
#                         expander_area = st.empty()
#                         # Add '1' to current_question tracking variable cause python starts counting from 0
#                         current_question = i + 1
#                         # display question_number
#                         number_placeholder.write(f"*Question {current_question}*")
#                         # display question based on question_number
#                         question_placeholder.write(f"**{ss.current_quiz[i].get('question')}**")
#                         # list of options
#                         options = ss.current_quiz[i].get("options")
#                         # track the user selection
#                         options_placeholder.radio("", options, index=1, key=f"Q{current_question}")
#                         nl(1)
#                         # Grade Answers and Return Corrections
#                         if ss.stop:
#                             # Track length of user_answers
#                             if len(ss.user_answers) < 10:
#                                 # comparing answers to track score
#                                 if ss[f'Q{current_question}'] == ss.current_quiz[i].get("correct_answer"):
#                                     ss.user_answers.append(True)
#                                 else:
#                                     ss.user_answers.append(False)
#                             else:
#                                 pass
#                             # Results Feedback
#                             if ss.user_answers[i] == True:
#                                 results_placeholder.success("CORRECT")
#                             else:
#                                 results_placeholder.error("INCORRECT")
#                             # Explanation of the Answer
#                             expander_area.write(f"*{ss.current_quiz[i].get('explanation')}*")
#
#             # calculate score
#             if ss.stop:
#                 ss['grade'] = ss.user_answers.count(True)
#                 scorecard_placeholder.write(f"### **Your Final Score : {ss['grade']} / {len(ss.current_quiz)}**")
#
#         # Initializing Button Text
#         st.button(label=ss.button_label[ss.counter],
#                   key='button_press', on_click=btn_click)
#         nl(3)
#         # Run Main App
#         quiz_app()

#         nl(1)




