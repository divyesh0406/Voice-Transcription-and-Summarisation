#pip install SpeechRecognition
#pip install nltk
#in IDLE shell write following commands
# nltk.download('stopwords')
# nltk.download('punkt')

import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

r = sr.Recognizer()

text1 = """There are many techniques available to generate extractive summarization
to keep it simple, I will be using an unsupervised learning approach to
find the sentences similarity and rank them. Summarization can be
defined as a task of producing a concise and fluent summary while
preserving key information and overall meaning. One benefit of this will
be, you don’t need to train and build a model prior start using it for
your project. It’s good to understand Cosine similarity to make the best
use of the code you are going to see. Cosine similarity is a measure of
similarity between two non-zero vectors of an inner product space that
measures the cosine of the angle between them. Its measures cosine of
the angle between vectors. The angle will be 0 if sentences are similar.""" 

text = """"""

def sumarizer():
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    
       
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()
       
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
       
       
       
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
       
    average = int(sumValues / len(sentenceValue))

    summary = ""
    
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += sentence
    print("\nSummary: " + summary)

MyText = ""
print("Listening")
        
        

while(MyText != "Stop stop. "):    
    try:
            with sr.Microphone() as source2:
                    
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                    
                MyText = MyText.capitalize() + ". "
                if(MyText != "Stop stop. "):
                    print(MyText)
                    text = text + MyText
            
    except:
        pass
sumarizer()
