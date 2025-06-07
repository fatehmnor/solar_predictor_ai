import streamlit as st
from PIL import Image
import numpy as np

def simulate_pv_output(brightness):
    return max(0, min(400, (brightness - 50) * 4))

st.title("📸 Sky Photo to PV Output Estimator")

uploaded_file = st.file_uploader("Upload a photo of the sky", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('L')
    st.image(image, caption="Uploaded Sky Image", use_column_width=True)

    img_array = np.array(image)
    avg_brightness = np.mean(img_array)

    estimated_output = simulate_pv_output(avg_brightness)

    st.subheader("Prediction Result")
    st.write(f"🧠 Average Brightness: {avg_brightness:.2f}")
    st.write(f"🔋 Estimated PV Output: {estimated_output:.2f} W")

    st.bar_chart({"PV Output (W)": [estimated_output]})
