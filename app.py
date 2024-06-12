import json
from deep_translator import GoogleTranslator

# Load the JSON data with utf-8 encoding
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialize the translator
translator = GoogleTranslator(source='en', target='es')

# Translate each word to Spanish and update the 'mean' field
for item in data:
    try:
        print("ok")
        translated_word = translator.translate(item['word'])
        item['mean'] = translated_word
    except Exception as e:
        print(f"Error translating word {item['word']}: {e}")
        item['mean'] = None

# Save the updated data back to a JSON file
output_file_path = 'data_translated.json'
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Translated data saved to {output_file_path}")
