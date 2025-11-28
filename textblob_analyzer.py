import pandas as pd
from textblob import TextBlob

# --- Configuration ---
# 1. Define the name of your input and output files
INPUT_FILE = 'CRM_v2.xlsx'
OUTPUT_FILE = 'Sentiment_analyzed.xlsx'

# 2. **CRITICAL:** Define the exact name of the column containing the text
TEXT_COLUMN = 'Requirement' 

print(f"Starting TextBlob analysis on {INPUT_FILE}...")

# --- Analysis Function ---

def get_textblob_sentiment(text):
    """
    Calculates Polarity and Subjectivity using TextBlob 
    and determines a simple sentiment label.
    """
    # 1. Handle missing/non-text data
    if pd.isna(text) or not isinstance(text, str):
        return 0.0, 0.0, 'NEUTRAL 😐'

    # 2. Create the TextBlob object
    analysis = TextBlob(text)
    
    # 3. Extract the two core scores
    polarity = analysis.sentiment.polarity     # Range: -1.0 (Negative) to 1.0 (Positive)
    subjectivity = analysis.sentiment.subjectivity # Range: 0.0 (Objective) to 1.0 (Subjective)
    
    # 4. Determine the overall sentiment label based on polarity
    if polarity > 0.05:
        sentiment = "POSITIVE 😊"
    elif polarity < -0.05:
        sentiment = "NEGATIVE 😠"
    else:
        sentiment = "NEUTRAL 😐"
        
    return polarity, subjectivity, sentiment

# --- Main Workflow ---

try:
    # 1. Read the Excel file into a pandas DataFrame (table)
    df = pd.read_excel(INPUT_FILE)

    # 2. Apply the analysis function to every value in the specified TEXT_COLUMN.
    # The lambda function unpacks the three values returned by get_textblob_sentiment().
    df[['Polarity_Score', 'Subjectivity_Score', 'Sentiment_Label']] = df[TEXT_COLUMN].apply(
        lambda x: pd.Series(get_textblob_sentiment(x))
    )

    # 3. Save the resulting DataFrame (with the new columns) to a new Excel file
    df.to_excel(OUTPUT_FILE, index=False) 

    print(f"\n✅ Analysis complete!")
    print(f"Results saved to {OUTPUT_FILE}")

except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find the file named '{INPUT_FILE}'.")
    print("Please make sure the Excel file is in the same folder as the Python script.")