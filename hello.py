import streamlit as st

st.write('Hello, Welome')
from PIL import Image
image_1 = str(current_dir / "image_file" / "Logo-removebg.png")
pil_image = Image.open(image_1)
image_array = np.array(pil_image)
st.image(image_array)
