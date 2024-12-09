import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import streamlit as st

def run_eda():
    # Load data from CSV file
    df = pd.read_csv('hotel_booking.csv')

    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

    # Filter the DataFrame for non-canceled bookings
    df_non_canceled = df[df['is_canceled'] == 0]

    # Group data by 'reservation_status_date' and calculate mean 'adr'
    chart_data = df_non_canceled.groupby('reservation_status_date')['adr'].mean().reset_index()

    # Set the reservation date as the index
    chart_data.set_index('reservation_status_date', inplace=True)

    # Streamlit app layout
    st.title("Visualization of Hotel Booking")
    st.write('By Serina Roihaanah')
    st.header("",divider='rainbow')
    st.subheader("Average Daily Rate Over Time")

    # Add a description
    st.write(
        "This line chart displays the average daily rate (ADR) of hotel bookings that were not canceled over time. "
        "This analysis helps to understand pricing trends in the hotel industry, allowing for more informed decision-making regarding pricing strategies. "
    )

    # Add a sidebar for date range filtering
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Select date range", 
                                        [chart_data.index.min(), chart_data.index.max()])

    # Filter the chart data based on the selected date range
    filtered_data = chart_data.loc[date_range[0]:date_range[1]]

    # Create a single line chart with the filtered data
    st.line_chart(filtered_data)

    st.divider()



    # Filter the DataFrame for canceled bookings
    df_canceled = df[df['is_canceled'] == 1]

    # Group data by 'reservation_status_date' and calculate mean 'adr'
    chart_data = df_canceled.groupby('reservation_status_date')['adr'].mean().reset_index()

    # Set the reservation date as the index
    chart_data.set_index('reservation_status_date', inplace=True)

    st.subheader("Average Daily Rate of Canceled Bookings Over Time")

    # Add a description
    st.write(
        "This line chart displays the average daily rate (ADR) of hotel bookings that were canceled over time. "
        "This analysis helps to understand how pricing trends may influence cancellation behavior, aiding in better management decisions."
    )
    # Filter the chart data based on the selected date range
    filtered_data = chart_data.loc[date_range[0]:date_range[1]]

    # Create a single line chart with the filtered data
    st.line_chart(filtered_data)



    # Ensure the relevant columns are present
    if 'hotel' in df.columns and 'name' in df.columns and 'is_canceled' in df.columns:
        # Count the frequency of hotel names by hotel type and cancellation status
        hotel_frequency = df.groupby(['hotel', 'is_canceled'])['name'].count().unstack(fill_value=0).reset_index()

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        hotel_frequency.set_index('hotel', inplace=True)
        hotel_frequency.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'])
        plt.title('Frequency of Hotel Names by Hotel Type and Cancellation Status')
        plt.xlabel('Hotel Type')
        plt.ylabel('Frequency of Names')
        plt.xticks(rotation=45)
        plt.legend(title='Cancellation Status', labels=['Not Canceled (0)', 'Canceled (1)'])
        
        # Store bar chart figure for later use
        bar_chart_fig = plt.gcf()
        plt.close()  # Prevents display before Streamlit shows it

    else:
        st.write("The required columns ('hotel', 'name', and 'is_canceled') are not present in the data.")

    st.divider()

    # Ensure the 'reservation_status' column is present
    if 'reservation_status' in df.columns:
        # Count the frequency of each reservation status
        status_counts = df['reservation_status'].value_counts()

        # Create a pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'salmon', 'lightgreen'])
        plt.title('Reservation Status Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.

        # Store pie chart figure for later use
        pie_chart_fig = plt.gcf()
        plt.close()  # Prevents display before Streamlit shows it

    else:
        st.write("The required column 'reservation_status' is not present in the data.")

    # Create columns for the bar chart and pie chart
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Hotel Name Frequency")
        st.write("This bar chart displays the frequency of hotel names for each hotel type, separated by cancellation status.")
        st.pyplot(bar_chart_fig)

    with col2:
        st.subheader("Reservation Status")
        st.write("This pie chart displays the distribution of reservation statuses.")
        st.pyplot(pie_chart_fig)



    st.divider()

    # Hitung value count untuk kolom market_segment
    market_segment_counts = df_canceled['market_segment'].value_counts()

    # Membuat bar chart horizontal
    st.subheader('Market Segment of Canceled Hotel Bookings')
    st.write('This bar chart displays the frequency of market segments for canceled hotel bookings, providing insights into which segments are most affected by cancellations.')
    st.bar_chart(market_segment_counts, use_container_width=True, height=400)



    st.divider()



    # Menghitung jumlah untuk kolom meal dan reserved_room_type
    meal_counts = df['meal'].value_counts()
    room_type_counts = df['reserved_room_type'].value_counts()

    # Create a pie chart for meal types
    plt.figure(figsize=(8, 6))
    plt.pie(meal_counts, labels=meal_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'salmon', 'lightgreen', 'gold', 'lavender'])
    plt.title('Distribution of Meal Types')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    meal_pie_chart_fig = plt.gcf()
    plt.close()  # Prevents display before Streamlit shows it

    # Create a bar chart for reserved room types
    plt.figure(figsize=(8, 6))
    plt.bar(room_type_counts.index, room_type_counts, color=['lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightyellow'])
    plt.title('Distribution of Reserved Room Types')
    plt.xlabel('Room Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    room_type_bar_chart_fig = plt.gcf()
    plt.close()  # Prevents display before Streamlit shows it

    # Create columns for the bar chart and pie chart
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribution of Meal Types")
        st.write("This pie chart illustrates the distribution of various meal options chosen by guests, highlighting their preferences during their stay.")
        st.pyplot(meal_pie_chart_fig)

    with col2:
        st.subheader("Distribution of Reserved Room Types")
        st.write("This bar chart presents the counts of different reserved room types, allowing us to assess which categories are most popular among guests.")
        st.pyplot(room_type_bar_chart_fig)



    st.divider()

if __name__ == "__main__":
    run_eda()