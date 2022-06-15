#Importing Libraries
from ntpath import join
from posixpath import split
import pandas as pd
import matplotlib.pyplot as plt 
#%matplotlib inline
from wordcloud import WordCloud
#Importing Dataset
df = pd.read_csv("C:\\Users\\roger\\Google Drive\\2022-1\\InvestigacionEducativaAulaIngenieria\\Taller_2_DatosCualitativos\\percepciones.csv")
#Checking the Data
df.head()
#Checking for NaN values
df.isna().sum()
#Removing NaN Values
# df.dropna(inplace = True)
#df.fillna('', inplace=True)
#Creating the text variable
text = " ".join(answers.split()[1] for answers in df.answers)

# Creating word_cloud with text as argument in .generate() method
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
# Display the generated Word Cloud
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
print('Keep show alive.')

from collections import Counter
counts = Counter(text)
print(counts)