import pandas as pd
import matplotlib.pyplot as plt

# --- Configuration ---
INPUT_FILE = 'Sentiment_analyzed.xlsx'
CHART_FILENAME = 'textblob_sentiment_pie_chart.png'
SENTIMENT_COLUMN = 'Sentiment_Label'

print(f"Starting pie chart generation using data from {INPUT_FILE}...")

# --- Main Workflow ---

try:
    # 1. Read the Excel file into a pandas DataFrame
    df = pd.read_excel(INPUT_FILE)

    # 2. Count the occurrences of each sentiment label
    # This Series contains the labels and their counts.
    sentiment_counts = df[SENTIMENT_COLUMN].value_counts()
    
    # 3. Prepare data for plotting
    labels = sentiment_counts.index
    sizes = sentiment_counts.values

    # 4. Define colors for consistency (Good for clear visualization)
    label_to_color = {
        'POSITIVE 😊': 'tab:green',
        'NEGATIVE 😠': 'tab:red',
        'NEUTRAL 😐': 'tab:gray'
    }
    # Ensure colors match the labels in the correct order
    colors = [label_to_color[label] for label in labels]

    # --- 5. Create and Format the Pie Chart ---
    plt.figure(figsize=(8, 8))
    
    # The plt.pie() function creates the chart
    plt.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', # Display percentages on the slices (e.g., 33.3%)
        startangle=90,     # Start the first slice at the top (makes it look cleaner)
        wedgeprops={'edgecolor': 'black'}, # Adds a border to the slices
        textprops={'fontsize': 12}
    )

    # Set the title and ensure the pie looks like a circle
    plt.title('TextBlob Sentiment Distribution', fontsize=16)
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle. 
    
    # 6. Save the chart to a file
    plt.savefig(CHART_FILENAME)
    plt.close()

    print(f"\n✅ Pie chart saved successfully as: {CHART_FILENAME}")

except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find the file named '{INPUT_FILE}'.")
    print("Please ensure the analyzed Excel file is in the same folder.")
except KeyError:
    print(f"\n❌ ERROR: The column '{SENTIMENT_COLUMN}' was not found in the Excel file.")
    print("Ensure the column name is correct ('Sentiment_Label').")
CHART_FILENAME = 'textblob_sentiment_pie_chart.png'
SENTIMENT_COLUMN = 'Sentiment_Label'

print(f"Starting pie chart generation using data from {INPUT_FILE}...")

# --- Main Workflow ---

try:
    # 1. Read the Excel file into a pandas DataFrame
    df = pd.read_excel(INPUT_FILE)

    # 2. Count the occurrences of each sentiment label
    # This Series contains the labels and their counts.
    sentiment_counts = df[SENTIMENT_COLUMN].value_counts()
    
    # 3. Prepare data for plotting
    labels = sentiment_counts.index
    sizes = sentiment_counts.values

    # 4. Define colors for consistency (Good for clear visualization)
    label_to_color = {
        'POSITIVE 😊': 'tab:green',
        'NEGATIVE 😠': 'tab:red',
        'NEUTRAL 😐': 'tab:gray'
    }
    # Ensure colors match the labels in the correct order
    colors = [label_to_color[label] for label in labels]

    # --- 5. Create and Format the Pie Chart ---
    plt.figure(figsize=(8, 8))
    
    # The plt.pie() function creates the chart
    plt.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', # Display percentages on the slices (e.g., 33.3%)
        startangle=90,     # Start the first slice at the top (makes it look cleaner)
        wedgeprops={'edgecolor': 'black'}, # Adds a border to the slices
        textprops={'fontsize': 12}
    )

    # Set the title and ensure the pie looks like a circle
    plt.title('TextBlob Sentiment Distribution', fontsize=16)
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle. 
    
    # 6. Save the chart to a file
    plt.savefig(CHART_FILENAME)
    plt.close()

    print(f"\n✅ Pie chart saved successfully as: {CHART_FILENAME}")

except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find the file named '{INPUT_FILE}'.")
    print("Please ensure the analyzed Excel file is in the same folder.")
except KeyError:
    print(f"\n❌ ERROR: The column '{SENTIMENT_COLUMN}' was not found in the Excel file.")
    print("Ensure the column name is correct ('Sentiment_Label').")
CHART_FILENAME = 'textblob_sentiment_pie_chart.png'
SENTIMENT_COLUMN = 'Sentiment_Label'

print(f"Starting pie chart generation using data from {INPUT_FILE}...")

# --- Main Workflow ---

try:
    # 1. Read the Excel file into a pandas DataFrame
    df = pd.read_excel(INPUT_FILE)

    # 2. Count the occurrences of each sentiment label
    # This Series contains the labels and their counts.
    sentiment_counts = df[SENTIMENT_COLUMN].value_counts()
    
    # 3. Prepare data for plotting
    labels = sentiment_counts.index
    sizes = sentiment_counts.values

    # 4. Define colors for consistency (Good for clear visualization)
    label_to_color = {
        'POSITIVE 😊': 'tab:green',
        'NEGATIVE 😠': 'tab:red',
        'NEUTRAL 😐': 'tab:gray'
    }
    # Ensure colors match the labels in the correct order
    colors = [label_to_color[label] for label in labels]

    # --- 5. Create and Format the Pie Chart ---
    plt.figure(figsize=(8, 8))
    
    # The plt.pie() function creates the chart
    plt.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', # Display percentages on the slices (e.g., 33.3%)
        startangle=90,     # Start the first slice at the top (makes it look cleaner)
        wedgeprops={'edgecolor': 'black'}, # Adds a border to the slices
        textprops={'fontsize': 12}
    )

    # Set the title and ensure the pie looks like a circle
    plt.title('TextBlob Sentiment Distribution', fontsize=16)
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle. 
    
    # 6. Save the chart to a file
    plt.savefig(CHART_FILENAME)
    plt.close()

    print(f"\n✅ Pie chart saved successfully as: {CHART_FILENAME}")

except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find the file named '{INPUT_FILE}'.")
    print("Please ensure the analyzed Excel file is in the same folder.")
except KeyError:
    print(f"\n❌ ERROR: The column '{SENTIMENT_COLUMN}' was not found in the Excel file.")
    print("Ensure the column name is correct ('Sentiment_Label').")
CHART_FILENAME = 'textblob_sentiment_pie_chart.png'
SENTIMENT_COLUMN = 'Sentiment_Label'

print(f"Starting pie chart generation using data from {INPUT_FILE}...")

# --- Main Workflow ---

try:
    # 1. Read the Excel file into a pandas DataFrame
    df = pd.read_excel(INPUT_FILE)

    # 2. Count the occurrences of each sentiment label
    # This Series contains the labels and their counts.
    sentiment_counts = df[SENTIMENT_COLUMN].value_counts()
    
    # 3. Prepare data for plotting
    labels = sentiment_counts.index
    sizes = sentiment_counts.values

    # 4. Define colors for consistency (Good for clear visualization)
    label_to_color = {
        'POSITIVE 😊': 'tab:green',
        'NEGATIVE 😠': 'tab:red',
        'NEUTRAL 😐': 'tab:gray'
    }
    # Ensure colors match the labels in the correct order
    colors = [label_to_color[label] for label in labels]

    # --- 5. Create and Format the Pie Chart ---
    plt.figure(figsize=(8, 8))
    
    # The plt.pie() function creates the chart
    plt.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', # Display percentages on the slices (e.g., 33.3%)
        startangle=90,     # Start the first slice at the top (makes it look cleaner)
        wedgeprops={'edgecolor': 'black'}, # Adds a border to the slices
        textprops={'fontsize': 12}
    )

    # Set the title and ensure the pie looks like a circle
    plt.title('TextBlob Sentiment Distribution', fontsize=16)
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle. 
    
    # 6. Save the chart to a file
    plt.savefig(CHART_FILENAME)
    plt.close()

    print(f"\n✅ Pie chart saved successfully as: {CHART_FILENAME}")

except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find the file named '{INPUT_FILE}'.")
    print("Please ensure the analyzed Excel file is in the same folder.")
except KeyError:
    print(f"\n❌ ERROR: The column '{SENTIMENT_COLUMN}' was not found in the Excel file.")
    print("Ensure the column name is correct ('Sentiment_Label').")