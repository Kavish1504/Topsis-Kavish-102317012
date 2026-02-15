import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import sys
from io import StringIO
from dotenv import load_dotenv
load_dotenv()

# Import topsis function
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from topsis_logic import topsis_calculate


def send_email(to_email, result_file):
    from_email = os.getenv('SENDER_EMAIL') 
    password = os.getenv('EMAIL_PASSWORD')  
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'TOPSIS Analysis Results'
        
        # Email body
        body = """
        Hello,
        
        Your TOPSIS analysis has been completed successfully!
        
        Please find the results attached.
        
        Best regards,
        TOPSIS Web Service
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach result file
        with open(result_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(result_file)}')
            msg.attach(part)
        
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        
        return True, "Email sent successfully!"
        
    except Exception as e:
        return False, f"Failed to send email: {str(e)}"


# Streamlit App
st.set_page_config(page_title="TOPSIS Web Service", page_icon="📊", layout="wide")

st.title("📊 TOPSIS Analysis Web Service")
st.markdown("---")

st.markdown("""
### Welcome to TOPSIS Calculator!
Upload your data, configure parameters, and receive results via email.

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method.
""")

st.markdown("---")

# File upload
st.subheader("1️⃣ Upload Input File")
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    # Display uploaded data
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    with st.expander("📋 View Uploaded Data"):
        st.dataframe(df)
    
    # Get number of criteria
    num_criteria = len(df.columns) - 1
    
    st.markdown("---")
    st.subheader("2️⃣ Configure Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Weights input
        st.markdown("**Weights** (comma-separated)")
        st.info(f"Enter {num_criteria} weights")
        weights_input = st.text_input(
            "Weights",
            value=",".join(["1"] * num_criteria),
            placeholder="e.g., 1,1,1,1",
            label_visibility="collapsed"
        )
    
    with col2:
        # Impacts input
        st.markdown("**Impacts** (comma-separated: + or -)")
        st.info(f"Enter {num_criteria} impacts")
        impacts_input = st.text_input(
            "Impacts",
            value=",".join(["+"] * num_criteria),
            placeholder="e.g., +,+,-,+",
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    st.subheader("3️⃣ Email Configuration")
    
    email_input = st.text_input(
        "Enter your email address",
        placeholder="your-email@example.com"
    )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🚀 Calculate TOPSIS", type="primary", use_container_width=True):
        
        # Validation
        if not weights_input or not impacts_input:
            st.error("Please provide both weights and impacts!")
        elif not email_input:
            st.error("Please provide your email address!")
        else:
            try:
                # Parse weights and impacts
                weights = [float(w.strip()) for w in weights_input.split(',')]
                impacts = [i.strip() for i in impacts_input.split(',')]
                
                # Validate
                if len(weights) != num_criteria:
                    st.error(f"Number of weights ({len(weights)}) must equal number of criteria ({num_criteria})")
                elif len(impacts) != num_criteria:
                    st.error(f"Number of impacts ({len(impacts)}) must equal number of criteria ({num_criteria})")
                elif not all(i in ['+', '-'] for i in impacts):
                    st.error("Impacts must be either '+' or '-'")
                else:
                    # Show progress
                    with st.spinner('🔄 Calculating TOPSIS...'):
                        # Save uploaded file temporarily
                        temp_input = 'temp_input.csv'
                        df.to_csv(temp_input, index=False)
                        
                        # Calculate TOPSIS
                        result_df = topsis_calculate(df, weights, impacts)
                        
                        # Save result
                        result_file = 'topsis_result.csv'
                        result_df.to_csv(result_file, index=False)
                        
                        st.success("✅ TOPSIS calculation completed!")
                        
                        # Display results
                        st.subheader("📊 Results")
                        st.dataframe(result_df, use_container_width=True)
                        
                        # Download button
                        csv = result_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results",
                            data=csv,
                            file_name="topsis_results.csv",
                            mime="text/csv"
                        )
                    
                    # Send email
                    st.markdown("---")
                    with st.spinner('📧 Sending email...'):
                        success, message = send_email(email_input, result_file)
                        if success:
                            st.success(f"{message}")
                        else:
                            st.error(f"{message}")
                        
                        # Clean up
                        if os.path.exists(temp_input):
                            os.remove(temp_input)
                
            except ValueError as e:
                st.error(f"Error: {str(e)}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

else:
    st.info("👆 Please upload a CSV file to get started")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Created by Kavish (102317012) | TOPSIS Web Service</p>
</div>
""", unsafe_allow_html=True)
