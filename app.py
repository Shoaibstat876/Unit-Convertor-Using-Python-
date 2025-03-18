import streamlit as st

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371,
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])


def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif to_unit == "Fahrenheit" and from_unit == "Kelvin":
        return (value - 273.15) * 9/5 + 32


# Streamlit UI
st.title("🌍 Universal Unit Converter")
st.write("Convert Length, Weight, and Temperature easily!")

# Select conversion category
conversion_type = st.selectbox("Select a category:", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
    to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit", ["Grams", "Kilograms", "Pounds", "Ounces"])
    to_unit = st.selectbox("To Unit", ["Grams", "Kilograms", "Pounds", "Ounces"])
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value:", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

# Footer
st.markdown("---")
st.write("💡 Built with Streamlit | 🚀 Keep Learning!")