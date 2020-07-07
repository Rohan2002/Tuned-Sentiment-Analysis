# Tuned-Sentiment-Analysis
A hyper-paramter tuned sentiment analysis neural network with 86.15% Test accuracy on the IMDB Dataset from Keras Dataset. 

## Tuned Hyperparameters
1. Dropout Regularization Rate
2. Learning Rate Alpha
3. Used Random Space to search for hyperparamters

## Improvements
This model is definetly overfitting with a training set accuracy set at 98%, validation set accuracy set at 87%, and test set accuracy set at 86.15%. 
We could tune the parameters more to improve the test accuracy and use a bigger neural network too.

## How to run this program
1. If you are running Anaconda run ```conda env create -f tensorflow-sentiment.yml``` to create virtual env to avoid disturbing other files in your system (Recommended!).
Otherwise, If you are just lazy :) then just run ```pip3 install -r requirements.txt```
2. Finally just run ```python3 run.py``` or ```python run.py``` to get the sentiment review from a machine! (Note: It will take some 15-20 seconds to load at the beginning, but it will start quicker after running several times)

Cheers,
Author: Rohan Deshpande




