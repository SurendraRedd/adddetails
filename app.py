import streamlit as st
import sqlite3

# Function to create a database table
def create_table():
    conn = sqlite3.connect("userdata.db")
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
    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, address, mobile_no)
        VALUES (?, ?, ?)
    """, (name, address, mobile_no))
    conn.commit()
    conn.close()

# Function to fetch all user data from the database
def fetch_all_data():
    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

# Main Streamlit app
def main():
    st.title("User Data API")

    # Create the database table if it doesn't exist
    create_table()

    # Input fields for user data
    name = st.text_input("Enter Name:")
    address = st.text_area("Enter Address:")
    mobile_no = st.text_input("Enter Mobile Number:")

    # Submit button to store data
    if st.button("Submit"):
        if name and address and mobile_no:
            # Insert data into the database
            insert_data(name, address, mobile_no)
            st.success("Data submitted successfully!")
        else:
            st.warning("Please fill in all fields.")

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
