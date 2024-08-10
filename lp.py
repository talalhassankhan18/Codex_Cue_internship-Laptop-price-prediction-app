import streamlit as st
import joblib
import pandas as pd
import base64

# Load the trained model
model_filename = 'C:/Users/PMLS/Downloads/Laptop price prediction/Model/laptop_price_regression_model.pkl'
loaded_model = joblib.load(model_filename)

# Function to make predictions and return specs
def predict_price(data):
    df = pd.DataFrame(data, index=[0])
    prediction = loaded_model.predict(df)
    # Return prediction and the input data (specs)
    return prediction[0], data

# Function to load the image and convert it to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to the uploaded image
image_path = 'C:/Users/PMLS/Downloads/Laptop price prediction/2.jpg'
base64_image = get_base64_image(image_path)

# Custom CSS for styling
st.markdown(f"""
    <style>
        .header {{
            background: url(data:image/png;base64,{base64_image});
            background-size: cover;
            padding: 20px 0;
            border-radius: 10px;
            text-align: center;
            margin: -10px -10px 10px -10px;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
            color: white; /* Adjust the text color to ensure visibility */
            font-size: 2.5em;
            font-weight: bold;
        }}
        .header:hover {{
            background: url(data:image/png;base64,{base64_image});
            background-size: cover;
            opacity: 0.8;
        }}
        .main {{
            background: linear-gradient(135deg, #008080 0%, #20B2AA 100%);
            padding: 10px;
            border-radius: 10px;
        }}
        body {{
            background-color: #1e1e1e;
            font-family: 'Helvetica Neue', sans-serif;
            color: #f0f0f0;
        }}
        .container {{
            background-color: #008080;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            padding: 20px;
            margin: 20px auto;
            max-width: 1600px;
        }}
        .title {{
            background-color: #FFFFFF;
            color: #008080;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }}
        .subheader {{
            color: #FFFFFF;
            font-size: 24px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .stButton>button {{
            background-color: #008080;
            color: white;
            border-radius: 10px;
            font-size: 20px;
            padding: 10px;
            border: none;
            cursor: pointer;
        }}
        .stButton>button:hover {{
            background-color: #000000;
            color: white;
        }}
        .stTextArea>div>textarea, .stFileUploader>div>div {{
            background-color: #333333;
            color: #f0f0f0;
            border: 2px solid #008080;
            border-radius: 10px;
            font-size: 22px;
            padding: 10px;
            margin-bottom: 20px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }}
        .stFileUploader>label {{
            color: #f0f0f0;
        }}
        .stSelectbox, .stNumberInput {{
            margin-bottom: 15px;
            background-color: #1C1C1C;
            border: 1px solid #555;
            border-radius: 8px;
            color: #ddd;
            padding: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
            width: 100%; /* Increased width for selectboxes and number inputs */
            max-width: 400px; /* Adjust as needed */
        }}
        .form-container {{
            display: flex;
            flex-direction: column;
            padding: 20px;
            width: 50%; /* The other half of the page for select boxes */
        }}
        .form-container .stSelectbox, .form-container .stNumberInput {{
            margin-bottom: 15px;
        }}
        .center-button {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }}
        .footer {{
            color: #2c3e50;
            text-align: center;
            margin-top: 50px;
            font-size: 18px;
        }}
        /* General selector for Streamlit file uploader label */
        .stFileUploader label {{
            color: white !important;
        }}
        .image-container img {{
            width: 100%; /* Ensure the image fits within the container's width */
            height: auto; /* Maintain the aspect ratio of the image */
            max-height: 600px; /* Optional: Set the maximum height for the image */
            border-radius: 15px; /* Set the border-radius for rounded corners */
        }}
    </style>
""", unsafe_allow_html=True)

# App layout
st.markdown('<div class="header">Laptop Price Prediction</div>', unsafe_allow_html=True)

# Create a two-column layout
col1, col2 = st.columns([1, 1])

with col1:
    # Input fields in sidebar
    st.sidebar.header('Input Laptop Features')
    brand = st.sidebar.selectbox('Brand', ['HP', 'Dell', 'Acer', 'Asus', 'Apple'])
    ram_gb = st.sidebar.number_input('RAM (in GB)', min_value=2, max_value=64, value=8)
    hdd = st.sidebar.number_input('HDD (in GB)', min_value=128, max_value=2048, value=500)
    ssd = st.sidebar.number_input('SSD (in GB)', min_value=0, max_value=2048, value=256)
    weight = st.sidebar.number_input('Weight (in kg)', min_value=1.0, max_value=5.0, value=2.0)
    cpu = st.sidebar.selectbox('CPU', ['Intel i3', 'Intel i5', 'Intel i7', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7'])
    gpu = st.sidebar.selectbox('GPU', ['None', 'NVIDIA', 'AMD', 'Intel Integrated'])
    touchscreen = st.sidebar.selectbox('Touchscreen', ['Yes', 'No'])
    warranty = st.sidebar.number_input('Warranty (in years)', min_value=1, max_value=5, value=1)
    processor_gnrtn = st.sidebar.selectbox('Processor Generation', ['4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th'])
    
    screen_size = st.sidebar.number_input('Screen Size (in inches)', min_value=10.0, max_value=20.0, value=15.6)
    os_bit = st.sidebar.selectbox('OS Bit', ['32', '64'])
    ram_type = st.sidebar.selectbox('RAM Type', ['DDR4', 'DDR3', 'DDR2'])
    processor_brand = st.sidebar.selectbox('Processor Brand', ['Intel', 'AMD'])
    processor_name = st.sidebar.selectbox('Processor Name', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7'])
    graphic_card_gb = st.sidebar.number_input('Graphic Card (in GB)', min_value=0, max_value=8, value=2)
    msoffice = st.sidebar.selectbox('MS Office', ['Yes', 'No'])
    num_ratings = st.sidebar.number_input('Number of Ratings', min_value=0, value=1000)
    num_reviews = st.sidebar.number_input('Number of Reviews', min_value=0, value=500)
    rating = st.sidebar.number_input('Rating', min_value=0.0, max_value=5.0, value=4.5)
    os = st.sidebar.selectbox('Operating System', ['Windows', 'macOS', 'Linux', 'Chrome OS'])

    # Center the "Predict Price" button
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("Predict Price"):
        user_data = {
            'brand': brand,
            'ram_gb': ram_gb,
            'hdd': hdd,
            'ssd': ssd,
            'weight': weight,
            'cpu': cpu,
            'gpu': gpu,
            'Touchscreen': 1 if touchscreen == 'Yes' else 0,
            'warranty': warranty,
            'processor_gnrtn': processor_gnrtn,
            'screen_size': screen_size,
            'os_bit': os_bit,
            'ram_type': ram_type,
            'processor_brand': processor_brand,
            'processor_name': processor_name,
            'graphic_card_gb': graphic_card_gb,
            'msoffice': 1 if msoffice == 'Yes' else 0,
            'Number of Ratings': num_ratings,
            'Number of Reviews': num_reviews,
            'rating': rating,
            'os': os
        }
        price, specs = predict_price(user_data)
        
        # Display the predicted price
        st.markdown(f"""
        <div style='text-align: center;'>
            <span style='font-size: 24px; color: #FFFFFF; font-weight: bold;'>
                Predicted Laptop Price: ${price:.2f}
            </span>
        </div>
        """, unsafe_allow_html=True)
        st.write("Laptop Specs")

        # Convert specs to a DataFrame
        specs_df = pd.DataFrame([specs])
        
        # Split the DataFrame into chunks of 6 columns
        def split_dataframe(df, chunk_size):
            return [df.iloc[:, i:i + chunk_size] for i in range(0, df.shape[1], chunk_size)]

        specs_chunks = split_dataframe(specs_df, 6)
        
        # Display each chunk
        for chunk in specs_chunks:
            st.table(chunk)

with col2:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image('C:/Users/PMLS/Downloads/Laptop price prediction/2.jpg', use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
# How to Use Section
st.markdown("""
    ## How to Use the Laptop Price Prediction App

    Welcome to the Laptop Price Prediction app! Here’s how you can use it:

    1. **Select Laptop Features**: On the left sidebar, you’ll find various input fields. Enter the details of the laptop you want to evaluate:
        - **Brand**: Choose the brand of the laptop.
        - **RAM (in GB)**: Specify the amount of RAM in gigabytes.
        - **HDD (in GB)**: Enter the hard disk drive capacity in gigabytes.
        - **SSD (in GB)**: Enter the solid-state drive capacity in gigabytes.
        - **Weight (in kg)**: Provide the weight of the laptop in kilograms.
        - **CPU**: Select the type of CPU used in the laptop.
        - **GPU**: Select the GPU (graphics processing unit) if any.
        - **Touchscreen**: Specify if the laptop has a touchscreen.
        - **Warranty (in years)**: Enter the warranty period in years.
        - **Processor Generation**: Choose the generation of the processor.
        - **Screen Size (in inches)**: Provide the size of the screen in inches.
        - **OS Bit**: Select the operating system bit version.
        - **RAM Type**: Choose the type of RAM.
        - **Processor Brand**: Specify the brand of the processor.
        - **Processor Name**: Choose the name of the processor.
        - **Graphic Card (in GB)**: Enter the graphics card capacity in gigabytes.
        - **MS Office**: Specify if MS Office is included.
        - **Number of Ratings**: Enter the number of ratings for the laptop.
        - **Number of Reviews**: Enter the number of reviews for the laptop.
        - **Rating**: Provide the average rating of the laptop.
        - **Operating System**: Select the operating system of the laptop.

    2. **Click 'Predict Price'**: After entering the details, click the **"Predict Price"** button.

    3. **View Results**: The predicted price of the laptop will be displayed below the button, along with a table showing the specifications you entered.

    4. **Image Display**: On the right side, you will see an image related to the laptop prediction.
""")