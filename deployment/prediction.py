import streamlit as st
import pandas as pd
import joblib


def  make_prediction():
    st.title('Hotel Reservation Prediction Model')
    st.header('',divider='rainbow')

    st.markdown(
        """
        <p style='color: blue;'>Use the sidebar to select input features.</p>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.header('User Input Features',divider='rainbow')


    def user_input():
        hotel = st.sidebar.selectbox('Hotel', ['City Hotel', 'Resort Hotel'])
        lead_time = st.sidebar.number_input('Lead Time', min_value=0, value=115)
        arrival_year = st.sidebar.number_input('Arrival Year', min_value=2015, value=2017)
        arrival_month = st.sidebar.selectbox('Arrival Month', ['January', 'February', 'March', 'April', 'May', 
                                                                'June', 'July', 'August', 'September', 'October', 
                                                                'November', 'December'])
        stays_in_weekend_nights = st.sidebar.number_input('Stays in Weekend Nights', min_value=0, value=1)
        stays_in_week_nights = st.sidebar.number_input('Stays in Week Nights', min_value=0, value=2)
        adults = st.sidebar.number_input('Number of Adults', min_value=1, value=2)
        children = st.sidebar.number_input('Number of Children', min_value=0, value=0)
        babies = st.sidebar.number_input('Number of Babies', min_value=0, value=0)
        meal = st.sidebar.selectbox('Meal Type', ['BB', 'HB', 'FB', 'SC'])
        country = st.sidebar.selectbox('Country', ['FRA', 'PRT', 'USA', 'GBR'])
        market_segment = st.sidebar.selectbox('Market Segment', ['Online TA', 'Offline TA/TO', 'Corporate'])
        distribution_channel = st.sidebar.selectbox('Distribution Channel', ['TA/TO', 'Direct'])
        is_repeated_guest = st.sidebar.selectbox('Is Repeated Guest?', [0, 1])
        previous_cancellations = st.sidebar.number_input('Previous Cancellations', min_value=0, value=0)
        previous_bookings_not_canceled = st.sidebar.number_input('Previous Bookings Not Canceled', min_value=0, value=0)
        reserved_room_type = st.sidebar.selectbox('Reserved Room Type', ['A', 'B', 'C', 'D'])
        assigned_room_type = st.sidebar.selectbox('Assigned Room Type', ['A', 'B', 'C', 'D'])
        booking_changes = st.sidebar.number_input('Booking Changes', min_value=0, value=0)
        deposit_type = st.sidebar.selectbox('Deposit Type', ['No Deposit', 'Refundable', 'Non Refundable'])
        days_in_waiting_list = st.sidebar.number_input('Days in Waiting List', min_value=0, value=0)
        customer_type = st.sidebar.selectbox('Customer Type', ['Transient', 'Contract', 'Group'])
        adr = st.sidebar.number_input('Average Daily Rate (ADR)', min_value=0.0, value=135.0)
        required_car_parking_spaces = st.sidebar.number_input('Required Car Parking Spaces', min_value=0, value=0)
        total_of_special_requests = st.sidebar.number_input('Total of Special Requests', min_value=0, value=0)
        reservation_status = st.sidebar.selectbox('Reservation Status', ['Check-Out', 'Canceled', 'No-Show'])

        data = {
            'hotel': hotel,
            'lead_time': lead_time,
            'arrival_date_year': arrival_year,
            'arrival_date_month': arrival_month,
            'stays_in_weekend_nights': stays_in_weekend_nights,
            'stays_in_week_nights': stays_in_week_nights,
            'adults': adults,
            'children': children,
            'babies': babies,
            'meal': meal,
            'country': country,
            'market_segment': market_segment,
            'distribution_channel': distribution_channel,
            'is_repeated_guest': is_repeated_guest,
            'previous_cancellations': previous_cancellations,
            'previous_bookings_not_canceled': previous_bookings_not_canceled,
            'reserved_room_type': reserved_room_type,
            'assigned_room_type': assigned_room_type,
            'booking_changes': booking_changes,
            'deposit_type': deposit_type,
            'days_in_waiting_list': days_in_waiting_list,
            'customer_type': customer_type,
            'adr': adr,
            'required_car_parking_spaces': required_car_parking_spaces,
            'total_of_special_requests': total_of_special_requests,
            'reservation_status': reservation_status,
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_data = user_input()

    st.subheader('User Input')
    st.write("""This is a view of the data you have entered.
    """)
    st.write(input_data)

    load_model = joblib.load("model.pkl")

    prediction = load_model.predict(input_data)

    if prediction  == 0:
        prediction_label = 'Will Not Cancel'
        color = 'blue'  # Set color to blue for 'Will Not Cancel'
    else:
        prediction_label = 'Will Cancel'
        color = 'red'  # Set color to red for 'Will Cancel'

    # Display the prediction message
    st.write('Based on user input, the prediction model predicted: ')

    # Use HTML to color the prediction label
    st.markdown(f"<p style='color: {color};'>{prediction_label}</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    make_prediction()