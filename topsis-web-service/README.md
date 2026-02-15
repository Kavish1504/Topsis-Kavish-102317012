# TOPSIS Web Service

A web-based interface for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis with email notification support.

## Features

- 📤 Upload CSV files
- ⚙️ Configure weights and impacts
- 📊 View results instantly
- 📧 Receive results via email
- 💾 Download results

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Usage

1. **Upload CSV File**: Click "Browse File" and upload your data file
2. **Configure Weights**: Enter comma-separated weights (e.g., 1,1,1,1)
3. **Configure Impacts**: Enter comma-separated impacts (e.g., +,+,-,+)
4. **Enter Email**: Provide your email address
5. **Calculate**: Click the "Calculate TOPSIS" button
6. **View Results**: Results will be displayed and sent to your email

## Email Configuration

To enable email functionality:

1. Open `app.py`
2. Update the following variables:
   - `from_email`: Your Gmail address
   - `password`: Your Gmail App Password

### How to Generate Gmail App Password:

1. Go to your Google Account settings
2. Enable 2-Factor Authentication
3. Go to Security → 2-Step Verification → App passwords
4. Generate a new app password for "Mail"
5. Use this password in the code

## Input File Format

The CSV file should have:
- First column: Names/IDs of alternatives
- Remaining columns: Numeric criteria values

Example:
```csv
Model,Price,Storage,Camera,Battery
M1,250,64,12,4000
M2,200,128,8,4500
M3,300,256,16,5000
```

## Author

Kavish (102317012)
