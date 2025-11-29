**Textblob Sentimental Analysis of FCA CRM 609**

# 📊 TextBlob Sentiment Analysis from Excel

## 🌟 Project

This repository contains a simple, yet effective, Python script that performs **Sentiment Analysis** on large datasets stored in an Excel file (`.xlsx`). It utilizes the lightweight and powerful **TextBlob** Python library.

The script reads text data from a specified column, analyzes the emotional tone (Polarity and Subjectivity), assigns a sentiment label, and outputs the results back into a new Excel file. Finally, it generates a visual **Pie Chart** summarizing the sentiment distribution.

---
P**hase 1: Setup and Installation**

### 1. Prerequisites

You must have **Python 3** installed on your system.

### 2. Install Required Libraries

Open your Terminal or Command Prompt and install all necessary tools using `pip`:

| Library        | Purpose                               | Installation Command |

| **pandas** | Reading and writing structured Excel data. | `pip install pandas` |

| **textblob** | Performing the sentiment analysis. | `pip install textblob` |

| **matplotlib** | Generating the visual Pie Chart. | `pip install matplotlib` |

| **openpyxl** | Engine for pandas to handle `.xlsx` files. | `pip install openpyxl` |

After installing `textblob`, you must download its linguistic data:

python3 -m textblob.download_corpora

3. **Input File Preparation** Your input Excel file must be placed in the root directory of this project and contain a dedicated column for the text reviews.
 
**Phase 2: Running the Analysis**

The core logic is contained within the textblob_analyzer.py file.

**1. Configure the Script**
Open textblob_analyzer.py in your code editor. Ensure the variable TEXT_COLUMN matches the header of the column containing the text you want to analyze.

**2. Execution**
Run the script from your Terminal. Make sure you are in the project folder (cd path/to/project).

python3 textblob_analyzer.py

3. Output Analysis - The script generates the file customer_reviews_analyzed.xlsx with three new columns:
   
Column Name	-----     Description  ---      	Values 

Polarity_Score	The primary sentiment score.	-1.0 (Negative) to +1.0 (Positive).

Subjectivity_Score	Measures how much the text is based on opinion vs. fact.	0.0 (Objective) to 1.0 (Subjective).

Sentiment_Label	The final categorical label.	POSITIVE 😊, NEGATIVE 😠, or NEUTRAL 😐.

📈 **Phase 3: Generating the Visualization (Pie Chart)** 
After the analysis script has run, the visualization script uses the generated output file to create a graphical summary.
1. The Script
The logic for generating the chart is usually placed in a file like textblob_pie_chart.py. This script automatically counts the labels in the **Sentiment_Label** column.

2. Execution
Run the chart generator from your Terminal.

3. Result
The script saves a visual summary of your data as an image file: textblob_sentiment_pie_chart.png. This chart shows the percentage distribution across all sentiment categories.
   
