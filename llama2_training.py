import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

# Read comments and actual categories from Excel sheet
comments_df = pd.read_excel("/content/sample_data/traning_labelled_data.xlsx")

# Initialize variables for accuracy calculation
predicted_categories = []
actual_categories = []

# Convert class labels to numeric form
label_encoder = LabelEncoder()
actual_categories_encoded = label_encoder.fit_transform(actual_categories)

for column in comments_df.columns:
  for value in comments_df[column]:
    output = ""
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "system_prompt": "Train with the yahoo comments given and learn which category they fall into.",
            "prompt": column + " : " + value
        },
    ):
        output += str(event)



