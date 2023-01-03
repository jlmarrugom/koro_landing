import streamlit as st
st.set_page_config(
    page_title="KoroAI",
    page_icon="attachments/koro_icon.png"
)

c1,c2 = st.columns([1,3])
c1.image("attachments/koro_icon_dark.png")
c2.title("This is the KoroAI Project Page")
st.write(
    """
    KoroAI is a project that emerges from the market necessity
    of Simple Artificial Intelligence apps, created with a high 
    quality standard.

    ## Project Goals
    We support the following services:
    """
    )
c1, c2, c3 = st.columns(3)

c1.write(
    """
    ### General Machine Learning
     - Data Classification.
     - Data Regression.
     - Data Clustering.
     - Data Generation.
    """)

c2.write(
    """
    ### Computer Vision
     - Image Classification.
     - Image Generation.
     - Visual Search.
     - Image Clustering.
    """)

c3.write(
    """
    ### AudioAI 
     - Audio Classification.
     - Audio Enhancement.
     - Voice Conversion.
     - Text to Speech.
     - Speech to text.
    """)

st.write(
    """
    ## Contact
    José Marrugo, Software Engineer \n
    jlmarrugom@hotmail.com
    """)
