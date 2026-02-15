# Topsis-Kavish-102317012

A Python package for implementing **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) for multi-criteria decision analysis.

## What is TOPSIS?

TOPSIS is a multi-criteria decision analysis method that helps in ranking alternatives based on their closeness to the ideal solution. It is widely used in decision-making scenarios where multiple conflicting criteria need to be considered.

## Installation

You can install the package using pip:

```bash
pip install topsis-kavish-102317012
```

## Usage

### Command Line

After installation, you can use the `topsis` command directly from the terminal:

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

**Example:**
```bash
topsis data.csv "1,1,1,1" "+,+,-,+" output.csv
```

### Python Script

You can also use it in your Python code:

```python
from topsis_kavish_102317012 import topsis

topsis('data.csv', '1,1,1,1', '+,+,-,+', 'output.csv')
```

## Input File Format

The input CSV file should have the following structure:

- **First column**: Names of alternatives (e.g., Fund Name, Model Name)
- **Remaining columns**: Numeric criteria values

**Example (data.csv):**
```
Fund Name,P1,P2,P3,P4
M1,0.87,0.40,6.7,47.9
M2,0.66,0.45,6.9,48.5
M3,0.66,0.42,5.4,49.7
```

## Parameters

- **InputDataFile**: Path to the input CSV file
- **Weights**: Comma-separated weights for each criterion (e.g., "1,1,1,1")
- **Impacts**: Comma-separated impacts for each criterion, either '+' (beneficial) or '-' (non-beneficial)
- **OutputResultFileName**: Path for the output CSV file

## Output

The output CSV file will contain:
- All original columns
- **Topsis Score**: Calculated TOPSIS score for each alternative
- **Rank**: Ranking based on TOPSIS score (1 is best)

## Requirements

- Python >= 3.6
- pandas >= 1.0.0
- numpy >= 1.18.0

## Validations

The package performs the following validations:
- Input file must have at least 3 columns
- Columns from 2nd to last must contain only numeric values
- Number of weights must equal number of criteria
- Number of impacts must equal number of criteria
- Impacts must be either '+' or '-'

## Author

**Kavish**  
Roll Number: 102317012

## License

MIT License
