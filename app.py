import streamlit as st

from pickle import load

def main():
    # with open('Best_RF_model.pkl', 'rb') as f:
    #     Best_RF_model = load(f)

    #     st.write("Best_RF_Model:", Best_RF_model)
    load(open('Best_RF_model.pkl', 'rb'))

    property_type = st.selectbox("Property Type", options=["Apartment", "House", "Condo", "Townhouse"])
    num_people = st.slider("Number of People Accommodated", min_value=1, max_value=10)
    num_reviews = st.number_input("Number of Reviews", min_value=0, step=1)
    beds = st.number_input("Number of Beds", min_value=0, step=1)
    security_deposit = st.number_input("Security Deposit ($)", min_value=0)

if __name__=="__main__":
    main()