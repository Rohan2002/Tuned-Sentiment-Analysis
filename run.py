import warnings
warnings.filterwarnings("ignore")
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import tensorflow
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = keras.models.load_model('./models/tuned_imdb.h5')

word_mapping = keras.datasets.imdb.get_word_index()
word_mapping = {k: v + 3 for k, v in word_mapping.items()}

# Add variables
word_mapping["<PAD>"] = 0
word_mapping["<START>"] = 1
word_mapping["<UNK>"] = 2
word_mapping["<UNUSED>"] = 3
max_length = 256
trun_type = "post"

def encode(s):
    encoded = [1]
    sentence = s.split()
    for word in sentence:
        if word.lower() in word_mapping:
            encoded.append(word_mapping[word.lower()])
        else:
            encoded.append(2)
    return encoded

sentence_test = input ("Enter your review:") 
real_encode = encode(sentence_test)
real_padded = pad_sequences(
    [real_encode], maxlen=max_length, truncating=trun_type, value=word_mapping["<PAD>"]
)
print("Your Review: ", sentence_test)
predict = model.predict([real_padded])
if (predict[0][0] < 0.5):
    print("Prediction: Negative Sentiment with accuracy", str(predict[0][0] * 100), "%")
else:
    print("Prediction: Positive Sentiment with accuracy", str(predict[0][0] * 100), "%")