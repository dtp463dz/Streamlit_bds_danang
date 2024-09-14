import streamlit as st
import joblib
import pandas as pd

loaded_pipeline = joblib.load('\\batdongsan\models\\bds_danang.joblib')

st.title("Đoán Giá Bất Động Sản Đà Nẵng")

st.sidebar.title("Nhập Thông Tin")
title = st.sidebar.text_input("Tiêu đề", value="Bán nhà An Mỹ 4, An Hải Tây, Sơn Trà, Đà Nẵng")
area = st.sidebar.number_input("Diện tích (m²)", value=150, min_value=1, max_value=50000)
bedroom = st.sidebar.number_input("Số phòng ngủ", value=3, min_value=1, max_value=10)
toilet = st.sidebar.number_input("Số phòng tắm", value=2, min_value=0, max_value=10)
location = st.sidebar.text_input("Vị trí", value="Sơn Trà, Đà Nẵng")
price_per_m2 = st.sidebar.number_input("Giá mỗi mét vuông (triệu đồng)", value=70, min_value=0, max_value=500)

input_data = {
    'Title': title,
    'Area(m2)': area,
    'Bedroom': bedroom,
    'Toilet': toilet,
    'Location': location,
    'Price_per_m2(trieu)': price_per_m2
}

input_df = pd.DataFrame([input_data])

predictions = loaded_pipeline.predict(input_df)
formatted_prediction = "${:,.2f}".format(predictions[0])

# Display the prediction
st.write(f"Dự đoán giá nhà:", f"<span style='color:green; font-size:24px'>{formatted_prediction}</span>", unsafe_allow_html=True)

latitude, longitude = get_coordinates_for_location(location)  

map_data = pd.DataFrame({
    'latitude': [latitude],
    'longitude': [longitude]
})

st.map(map_data)

def get_coordinates_for_location(location):
    coordinates = {
        'Sơn Trà, Đà Nẵng': (16.075, 108.228),
    }
    return coordinates.get(location, (0, 0))
