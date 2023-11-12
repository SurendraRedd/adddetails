import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

DB_NAME = "userdata.db"

with st.sidebar:
    selected = option_menu("", ["Home", 'Details'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)

# Function to create a database table
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            mobile_no TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to insert user data into the database
def insert_data(name, address, mobile_no):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, address, mobile_no)
        VALUES (?, ?, ?)
    """, (name, address, mobile_no))
    conn.commit()
    conn.close()

# Function to fetch all user data from the database
def fetch_all_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

def is_valid_mobile_number(mobile_number):
    # Add your custom validation logic here
    # For simplicity, let's check if it's a 10-digit number
    return mobile_number.isdigit() and len(mobile_number) == 10

# Main Streamlit app
def main():
    if selected == "Home":
        st.title("🎁Koerber Diwali gift ")

        # Create the database table if it doesn't exist
        create_table()

        # Input fields for user data
        name = st.text_input("🚻Enter Name:")
        address = st.text_area("🏠Enter Address:")
        mobile_no = st.text_input("☎️Enter Mobile Number:")

        # Submit button to store data
        if st.button("Submit"):
            if is_valid_mobile_number(mobile_no):
                st.success("Valid mobile number entered: " + mobile_no)
            else:
                st.warning("Please enter a valid 10-digit mobile number.")

            if name and address and mobile_no:
                # Insert data into the database
                insert_data(name, address, mobile_no)
                st.success("Data submitted successfully!")
            else:
                st.warning("Please fill in all fields.")

    if selected == "Details":
        # Display all user data
        st.header("User Data in the Database:")
        data = fetch_all_data()
        if data:
            for row in data:
                st.write(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}, Mobile Number: {row[3]}")
        else:
            st.info("No user data available.")

if __name__ == "__main__":
    main()
