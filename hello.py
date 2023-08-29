import streamlit as st

st.write('Hello, Welome')
from PIL import Image
from pathlib import Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
image_1 = str(current_dir / "Logo-removebg.png")
pil_image = Image.open(image_1)
image_array = np.array(pil_image)
st.image(image_array)
