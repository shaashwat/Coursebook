import json
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import tensorflow as tf
import numpy as np
import pandas as pd
import os
from untitled1 import ratemyprof

vocab_size = 10000
embedding_dim = 16
max_length = 32
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"
training_size = 11000

workpath = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(workpath, "commentdata.csv"), lineterminator='\n')

sentences = data.Comments
labels = data.Ratings

for i in range(0, len(sentences)):
    sentences[i] = str(sentences[i])

training_sentences = sentences[0:training_size]
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)
newmodel = tf.keras.models.load_model(os.path.join(workpath, 'mymodel.h5'))


def getCommentSentiment(comment):


    # start comment out


    '''
    testing_sentences = sentences[training_size:]
    training_labels = labels[0:training_size]
    testing_labels = labels[training_size:]
    
    training_labels_final = np.array(training_labels)
    testing_labels_final = np.array(testing_labels)
    
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_sentences)
    
    word_index = tokenizer.word_index
    
    training_sequences = tokenizer.texts_to_sequences(training_sentences)
    training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    
    testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
    testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    num_epochs = 30
    history = model.fit(training_padded, training_labels_final, epochs=num_epochs, validation_data=(testing_padded, testing_labels_final), verbose=2)
    
    model.save(os.path.join(workpath, "mymodel.h5"))
    print("saved weights")
    '''

    # end comment out


    print("Loaded model from disk")
    test_data = np.array([comment]) #put gatech comments here
    test_seq = tokenizer.texts_to_sequences(test_data)
    test_padded = pad_sequences(test_seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    return newmodel.predict(test_padded)

def getAverageSentiment(prof):
    comments = ratemyprof.getProfComments(prof)
    if (len(comments) == 0):
        return -1.0
    else:
        sum = 0
        counter = 0
        if len(comments) < 15:
            for comment in comments:
                sum += (getCommentSentiment(comment)[0][0])
                print(counter)
                counter += 1
        else:
            for i in range(15):
                sum += (getCommentSentiment(comments[i])[0][0])
                print(counter)
                counter += 1

    return sum/counter

def getSentimentList(profnames):
    sentlist = []
    for prof in profnames:
        sentlist.append(getAverageSentiment(prof))
    return sentlist

