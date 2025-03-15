import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

data = {
    'Month': ['Jan-21', 'Feb-21', 'Mar-21', 'Apr-21', 'May-21'],
    'Meat': ['$8,000', '$7,000', '$9,000', '$10,000', '$11,000'],
    'Fruit': ['$12,000', '$10,000', '$13,000', '$15,000', '$14,000'],
    'Paper': ['$7,000', '$6,000', '$8,000', '$9,000', '$10,000'],
    'Total Sales': ['$27,000', '$23,000', '$30,000', '$34,000', '$35,000']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert string values to numeric
for column in ['Meat', 'Fruit', 'Paper', 'Total Sales']:
    df[column] = df[column].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Set the Month column as datetime
df['Month'] = pd.to_datetime(df['Month'], format='%b-%y')

# Streamlit app
st.title('Commodity Sales Trends')

# Checkboxes for commodity selection
commodities = ['Meat', 'Fruit', 'Paper', 'Total Sales']
selected_commodities = st.multiselect('Select commodities to display:', commodities, default=commodities)

# Plotting
st.subheader('Sales Trends Over Time')
fig, ax = plt.subplots()
for commodity in selected_commodities:
    ax.plot(df['Month'], df[commodity], marker='o', label=commodity)

ax.set_title('Sales Trends')
ax.set_xlabel('Month')
ax.set_ylabel('Sales ($)')
ax.legend()
ax.grid()

# Display the plot
st.pyplot(fig)

# Show the DataFrame
st.subheader('Data Table')
st.dataframe(df)