import underthesea
import string


def remove_stopwords(input_text, stopwords_file='stopword.txt'):
    # Read the custom stop words from the file
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)

    cleaned_words = [word for word in input_text.split() if word.lower() not in stopwords]
    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text

def word_segment(text):
    return underthesea.word_tokenize(text, format="text")

def remove_numbers(input_string):
    # Use the isalpha() method to filter out numeric characters
    cleaned_string = ''.join(char for char in input_string if not char.isdigit())
    return cleaned_string

def remove_punctuation(input_string):
    # Create a translation table to remove all punctuation characters
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translate method to remove punctuation
    cleaned_string = input_string.translate(translator)
    
    return cleaned_string

def lower_case(text):
    return text.lower()

def data_preprocessing(text):
    return word_segment(remove_numbers(remove_punctuation(lower_case(text))))

def read_data(data):
    for x in ['train', 'validation', 'test']:
        data[x] = data[x].map(lambda example: {'sentence': data_preprocessing(example['sentence'])})

def read_input(input):
    return data_preprocessing(input)