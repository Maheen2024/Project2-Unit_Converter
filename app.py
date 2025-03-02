import streamlit as st

# Custom CSS for a soft pastel gradient background
page_bg_gradient = """
<style>
    .stApp {
        background: linear-gradient(135deg, #f3e7e9, #e3eeff); /* Soft pink to light blue */
        background-attachment: fixed;
        background-size: cover;
    }
</style>
"""

st.markdown(page_bg_gradient, unsafe_allow_html=True)
#button style
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #f3e7e9;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.subheader("Frequently Asked Questions (FAQ)")
faq = {
    "How does this converter work?": "It uses predefined conversion factors to accurately convert values between units.",
    "Can I convert between different measurement types?": "No, conversions are only valid within the same category (e.g., length to length, weight to weight).",
    "How is temperature conversion handled?": "Since temperature follows different formulas, it is calculated separately from other units.",
    "Is this tool accurate?": "Yes! The conversion factors are based on standard mathematical values used in measurement systems."
}

for question, answer in faq.items():
    with st.sidebar.expander(question):
        st.write(answer)


        #main body
st.title("🔁 Unit Converter")
st.write("Easily convert between different units of measurement with accuracy and speed⚡")
#conversion types
conversion_type = ["Length", "Temperature", "Weight", "Speed", "Volume", "Time"]

# user choice of conversion
conversion_choice = st.selectbox("✅ Select the type of conversion", conversion_type)

result = None

#conversion of length
if conversion_choice == "Length":
    length = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
    from_length = st.selectbox("From", length)
    to_length = st.selectbox("To", length)
    input_length = st.number_input("Enter the length",value=0.00, format="%.2f")
    #conversion dictionary
    conversion_dict = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 1.09361,
        "feet": 0.3048,
        "inches": 0.0254
    }
    result = input_length * conversion_dict[from_length] / conversion_dict[to_length]


#conversion of temperature
if conversion_choice == "Temperature":
    temperature = ["Celsius", "Fahrenheit", "Kelvin"]
    from_temperature = st.selectbox("From", temperature)
    to_temperature = st.selectbox("To", temperature)
    input_temperature = st.number_input("Enter the temperature",value=1.00, format="%.2f")
    if from_temperature == "Celsius" and to_temperature == "Fahrenheit":
        result = (input_temperature * 9/5) + 32
    elif from_temperature == "Celsius" and to_temperature == "Kelvin":
        result = input_temperature + 273.15
    elif from_temperature == "Fahrenheit" and to_temperature == "Celsius":
        result = (input_temperature - 32) * 5/9
    elif from_temperature == "Fahrenheit" and to_temperature == "Kelvin":
        result = (input_temperature - 32) * 5/9 + 273.15
    elif from_temperature == "Kelvin" and to_temperature == "Celsius":
        result = input_temperature - 273.15
    elif from_temperature == "Kelvin" and to_temperature == "Fahrenheit":
        result = (input_temperature - 273.15) * 9/5 + 32


#conversion of weight
if conversion_choice == "Weight":
    weight = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
    from_weight = st.selectbox("From", weight)
    to_weight = st.selectbox("To", weight)
    input_weight = st.number_input("Enter the weight")
    #conversion dictionary
    conversion_dict = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    }
    result = input_weight * conversion_dict[from_weight] / conversion_dict[to_weight]
   

#conversion of speed
if conversion_choice == "Speed":
    speed = ["m/s", "km/h", "miles/h", "knots"]
    from_speed = st.selectbox("From", speed)
    to_speed = st.selectbox("To", speed)
    input_speed = st.number_input("Enter the speed",value=1.00, format="%.2f")
    #conversion dictionary
    conversion_dict = {
        "m/s": 1,
        "km/h": 3.6,
        "miles/h": 2.23694,
        "knots": 1.94384
    }
    result = input_speed * conversion_dict[from_speed] / conversion_dict[to_speed]
   

#conversion of volume
if conversion_choice == "Volume":
    volume = ["liters", "milliliters", "gallons", "quarts", "pints", "cups", "ounces"]
    from_volume = st.selectbox("From", volume)
    to_volume = st.selectbox("To", volume)
    input_volume = st.number_input("Enter the volume",value=1.00, format="%.2f")
    #conversion dictionary
    conversion_dict = {
        "liters": 1,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.236588,
        "ounces": 0.0295735
    }
    result = input_volume * conversion_dict[from_volume] / conversion_dict[to_volume]
   
#conversion of time
if conversion_choice == "Time":
    time = ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]
    from_time = st.selectbox("From", time)
    to_time = st.selectbox("To", time)
    input_time = st.number_input("Enter the time",value=1.00, format="%.2f")
    #conversion dictionary
    conversion_dict = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
        "weeks": 604800,
        "months": 2628000,
        "years": 31536000
    }
    result = input_time * conversion_dict[from_time] / conversion_dict[to_time]
    
if st.button("Convert"):
        st.write(f"✔ Converted value: {result}")

# st.header("Feedback")
# feedback = st.text_area("We'd love to hear your thoughts about the Unit Converter.")
# if st.button("Submit Feedback"):
#     st.success("Thank you for your feedback!")

    # import streamlit as st

# Sidebar feedback form
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("Share your feedback")

if st.sidebar.button("Submit"):
    if feedback:
        st.sidebar.success("Thank you for your feedback!")
        # You can also save the feedback to a file or database here
    else:
        st.sidebar.warning("Please enter some feedback before submitting.")




       