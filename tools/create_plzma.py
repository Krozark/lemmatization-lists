import lzma
import pickle


path = "lemmatization-fr.txt"
input_data = {}
with open(path, "r") as f:
    data = f.read().split("\n")
    for line in data:
        if not line:
          continue

        lemma, txt= line.split("\t")
        if txt in input_data:
            input_data[txt].add(lemma)
        else:
            input_data[txt] = {lemma}

i = 0
for k,v in input_data.items():
    if len(v) > 1:
        print(k,v)
        i += 1
print(i)
    
# data is a dict as the key is the word, and the value the lemma
#data : dict[str, str] = {}
#
#path = "simplemma/strategies/dictionaries/data/your_language.plzma"
#
#final_data = {k.encode():v.encode() for k,v in data.items()}
#with lzma.open(path, "wb") as filehandle:
#    pickle.dump(final_data, filehandle)
