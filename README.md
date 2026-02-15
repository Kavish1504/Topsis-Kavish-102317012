# TOPSIS Web Service & Python Package
**Multi-Criteria Decision Making using TOPSIS**

This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) algorithm and provides:
1. A Python CLI tool published on PyPI
2. A Web Service with an intuitive user interface and email delivery

---



## 1. Methodology

The TOPSIS workflow followed in this project is shown below:
```
Data Collection
      ↓
Data Validation & Preprocessing
      ↓
Weight & Impact Assignment
      ↓
TOPSIS Computation
      ↓
Result Generation & Ranking
      ↓
Result Delivery (CSV / Email)
```

### Algorithm Steps:
1. **Normalize** the decision matrix
2. Calculate **weighted normalized** decision matrix
3. Determine **ideal best** and **ideal worst** solutions
4. Calculate **Euclidean distances** from ideal solutions
5. Calculate **TOPSIS score** (closeness coefficient)
6. **Rank** alternatives based on scores

---

## 2. Description

**TOPSIS** is a Multi-Criteria Decision Making (MCDM) technique that ranks alternatives based on their geometric distance from:
- **Ideal Best Solution** (closest to all best criteria values)
- **Ideal Worst Solution** (farthest from all worst criteria values)

The alternative closest to the ideal best solution and farthest from the ideal worst receives **Rank 1**.

### Key Highlights
✅ Fully implemented in **Python**  
✅ Available as a **CLI tool** via PyPI  
✅ **Web Service** with interactive UI  
✅ Comprehensive **input validation** (weights, impacts, data types)  
✅ **Email delivery** of results  
✅ Results in **CSV format** with scores and rankings  

---

## 3. Input / Output

### Input Format

The input CSV file should contain:
- **First column:** Alternative names (e.g., Model, Product, Supplier)
- **Remaining columns:** Numeric criteria values

#### Parameters:
- **Weights:** Comma-separated numeric values representing importance of each criterion
- **Impacts:** Comma-separated `+` (beneficial) or `-` (non-beneficial) for each criterion

### Example Input

**Input CSV (`data.csv`):**
```csv
Model,Storage,Camera,Price,Rating
M1,16,12,250,5
M2,16,8,200,3
M3,32,16,300,4
M4,32,8,275,4
M5,16,16,225,2
```

**Weights:**
```
0.25,0.25,0.25,0.25
```

**Impacts:**
```
+,+,-,+
```
*Explanation:*
- Storage: Higher is better (+)
- Camera: Higher is better (+)
- Price: Lower is better (-)
- Rating: Higher is better (+)

### Output Format

The output CSV includes two additional columns:
- **Topsis Score:** Closeness coefficient (0 to 1)
- **Rank:** Final ranking (1 is best)

**Example Output:**

| Model | Storage | Camera | Price | Rating | Topsis Score | Rank |
|-------|---------|--------|-------|--------|--------------|------|
| M3    | 32      | 16     | 300   | 4      | 0.6391       | 1    |
| M5    | 16      | 16     | 225   | 2      | 0.5123       | 2    |
| M4    | 32      | 8      | 275   | 4      | 0.4829       | 3    |
| M1    | 16      | 12     | 250   | 5      | 0.4234       | 4    |
| M2    | 16      | 8      | 200   | 3      | 0.3567       | 5    |

---

## 4. Python Package (PyPI CLI Tool)

### 📦 Installation
```bash
pip install topsis-kavish-102317012
```

### 🚀 Usage

**Command Syntax:**
```bash
python -m topsis_kavish_102317012.topsis <input_csv> <weights> <impacts> <output_csv>
```

**Example:**
```bash
python -m topsis_kavish_102317012.topsis data.csv "1,1,1,1" "+,+,-,+" result.csv
```

**Python Script Usage:**
```python
from topsis_kavish_102317012 import topsis

topsis('data.csv', '1,1,1,1', '+,+,-,+', 'output.csv')
```

### 🔗 PyPI Link
[https://pypi.org/project/topsis-kavish-102317012/](https://pypi.org/project/topsis-kavish-102317012/)

### ✅ Features
- ✓ Input validation (file format, numeric values, parameter counts)
- ✓ Error handling with descriptive messages
- ✓ Fast computation using NumPy and Pandas
- ✓ Command-line interface for easy integration

---

## 5. Web Service

The TOPSIS algorithm is also deployed as an **interactive web application** built with **Streamlit**.

### 🌐 Features
✅ **File Upload:** Upload CSV files directly  
✅ **Dynamic Configuration:** Enter weights and impacts with real-time validation  
✅ **Email Delivery:** Receive results via email automatically  
✅ **Data Preview:** View uploaded data before processing  
✅ **Results Display:** Interactive table with scores and rankings  
✅ **Download Option:** Download results as CSV  
✅ **Responsive UI:** Clean and intuitive interface  


### 🛠️ Local Setup
```bash
# Navigate to web service directory
cd topsis-web-service

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

## 6. Screenshots

### Web Interface

---

## 7. Project Structure
```
TOPSIS-KAVISH-102317012/
│
├── Topsis-Kavish-102317012/              # Python Package
│   ├── topsis_kavish_102317012/
│   │   ├── __init__.py
│   │   └── topsis.py
│   ├── dist/                             # Distribution files
│   ├── Topsis_Kavish_102317012.egg-info/
│   ├── setup.py                          # Package configuration
│   ├── README.md                         # Package documentation
│   └── LICENSE                           # MIT License
│
├── topsis-web-service/                   # Web Application
│   ├── app.py                            # Streamlit interface
│   ├── topsis_logic.py                   # TOPSIS calculations
│   ├── requirements.txt                  # Dependencies
│   ├── .env.example                      # Environment template
│   └── README.md                         # Web service docs
│
├── .gitignore                            # Git ignore rules
├── README.md                             # Project documentation
└── LICENSE                               # MIT License
```

---



---

## 8. Academic Information

- **Course:** UCS654 – Predictive Data Analytics
- **Student Name:** Kavish
- **Roll Number:** 102317012
- **Institute:** Thapar Institute of Engineering & Technology


## 9. License

This project is licensed under the **MIT License**.
