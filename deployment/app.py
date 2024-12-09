import streamlit as st

# Import functions from eda.py and predict.py
from eda import run_eda
from prediction import make_prediction

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Select", ["Home", "EDA", "Prediction"])

    if selection == "Home":
        st.title("Welcome to the Hotel Reservation Prediction Application")
        st.subheader("",divider = 'blue')
        st.write(
            "This application is designed to provide insights and predictions related to hotel bookings. "
            "It features two main functionalities:"
        )

        st.subheader("1. Exploratory Data Analysis (EDA)")
        st.write(
            "In the EDA section, you can explore various visualizations and statistical summaries of hotel booking data. "
            "This includes analyzing trends, understanding cancellation patterns, and evaluating factors that influence booking decisions. "
            "The visualizations will help you gain a deeper understanding of the data and make informed decisions based on historical booking behavior."
        )
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px !important;
                color: #4CAF50;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<p class="big-font">Explore the insights and improve your booking strategies!</p>', unsafe_allow_html=True)

        st.subheader("2. Prediction Model")
        st.write(
            "The Prediction section allows you to input specific features related to a hotel reservation and predict whether a booking is likely to be canceled. "
            "By entering details such as the hotel type, lead time, number of guests, and other relevant parameters, you can receive a prediction indicating whether the reservation is likely to be canceled or not. "
            "This feature is beneficial for hotel managers and staff in planning and managing bookings more effectively."
        )
        st.markdown(
            """
            <style>
            .highlight {
                color: #FF5733;
                font-weight: bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<p class="highlight">Make informed decisions to enhance your hotel management!</p>', unsafe_allow_html=True)

    elif selection == "EDA":
        run_eda()  # Call EDA function
    elif selection == "Prediction":
        make_prediction()  # Call prediction function

if __name__ == "__main__":
    main()
