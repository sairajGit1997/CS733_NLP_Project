import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder

comments_df = pd.read_excel("/content/sample_data/test_labelled_data.xlsx")

predicted_categories = []
actual_categories = []

for column in comments_df.columns:
  for value in comments_df[column]:
    output = ""
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "system_prompt": "Predict which category does the given comment falls into Humor or Consolidating or Abusive or Spam or Neutral or Ideological, Just output the category",
            "prompt": value
        },
    ):
        output += str(event)

    # Add predicted category to the list
    predicted_categories.append(output.strip())
    actual_categories.append(column.capitalize())


# Calculating accuracy, precision, recall, F1-score values
accuracy = accuracy_score(actual_categories, predicted_categories)
precision = precision_score(actual_categories, predicted_categories, average='weighted')
recall = recall_score(actual_categories, predicted_categories, average='weighted')
f1 = f1_score(actual_categories, predicted_categories, average='weighted')

# Printing accuracy, precision, recall, and F1-score values
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
