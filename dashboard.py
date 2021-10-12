import streamlit as st
import streamlit.components.v1 as components
import pickle
import re
from PIL import Image

score = []
score2d = []

#streamlit section

st.set_page_config(
    page_title="Artificial Assessor",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr {
            background-color:  #00aaff  !important;
            color: white !important;
        }
        div[role="radiogroup"] > div {
            color:white !important;
            background-color: red !important;
        }
        .st-dd, .st-cb,  {
            color: white !important;
        }
        div[data-baseweb="select"] > div {
            background-color:  white  !important;
        }
        div[data-baseweb="select"] > div {
            background-color:  white  !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

image = Image.open('images/robot.png')
police = Image.open('images/police.png')
solution = Image.open('images/solution.png')
profile = Image.open('images/profile.png')

st.sidebar.image(image, caption='', width=250)

st.sidebar.write('<span style="font-size:20px; color:#000000"><b>Artificial Assessor</b></span>',
                 unsafe_allow_html=True)


page = st.sidebar.radio('Sprint Navigation', ['Introduction','Solution','Demo','Contributor'])

if page == 'Introduction':
    st.title("Introduction")
    
    st.header("Problem Statement")
    
    st.markdown('Many of our police men after training or graduating from the academy, struggle to find their place within the PNP workforce. Assessment is extensive and slow but even then it is prone to error. Moreover, the assessment is not standardize for the whole police force. sometimes these assessments do not intersect with the interest of the recruits.',unsafe_allow_html=False)
    
    st.components.v1.iframe("https://www.youtube.com/embed/C5yeITanRuo", height = 600)
    
elif page == 'Solution':
    st.title("Solution")
    
    st.markdown('To modernize the PNP\'s assessment of its police personnel, An AI can greatly help fast track assessment and evaluation of pnp personel. what would take weeks or days for evaluator to decide on placement, will take minutes for the AI to recommend the applicant\'s placement. It will help evaluators scan through applicants and gain trust though competency.',unsafe_allow_html=False)
    
    st.header("How it works")
    
    st.markdown('applicants will go through an assessment test for data collection. these data in addition to the applicant\'s college degree will help the AI give accurate assessment and evaluation of the applicant. Certain parts of the test give weights to a particular assessment. for example if the applicant has a bigger scores in english in the assessment test + a Bachelor\'s degree in communication, the AI will evaluate that the applicant is suitable for Public Relations related work. likewise an applicant with high score in mathemathics particularly accounting + an engineering degree, the AI will have to distinguish between a financing job or engineering job for the applicant.',unsafe_allow_html=False)
    
    st.header("")
    
    st.image(solution)
    
elif page == 'Demo':
    st.title("Demo")
    
    st.image(police, width=200)
    
    st.header("Assessment Inputs")
    
    math_input = st.text_input("math score")
    english_input = st.text_input("english score")
    science_input = st.text_input("science score")
    logical_thinking_input = st.text_input("logical thinking score")
    degree_input = st.text_input("college degree")
    
    score.append(math_input)
    score.append(english_input)
    score.append(science_input)
    score.append(logical_thinking_input)
    
    score2d.append(score)
    
    #load model
    Pkl_Filename = "Saved_Model.pkl"
    with open(Pkl_Filename, 'rb') as file:  
        Pickled_Model = pickle.load(file)
    
    st.header("Result")
    
    prediction = str(Pickled_Model.predict(score2d))
    
    re.sub(r'[^\w]', '', prediction)
    
    if prediction:
        st.write(prediction)
    else:
        st.write('no data')
    
elif page == 'Contributor':
    st.title("Contributor")
    
    st.image(profile)