

#poetry run python .\lab001.py  C:\\Users\\pawel\\Downloads\\Frankenstein.txt --hist_size 5



from tqdm import tqdm
from collections import Counter
from ascii_graph import Pyasciigraph
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("--hist_size", help="how many words should be displayed on histogram",type=int)
parser.add_argument("--min_len", help = "minimum length of a word to be considered",type = int)
args = parser.parse_args()
file_name = args.filename

hist_size = 10
if args.hist_size:
    hist_size = args.hist_size
min_len = 0
if args.min_len:
    min_len = args.min_len


with open(file_name,encoding="utf-8") as f:
    text = f.read()

text = text.translate({ord(c):None for c in "?.!;,'"})#usuwam interpunkcje itd
text = text.casefold()#lowercase plus jakies dodatkowe rzeczy dla znaków które mozna różnie zapisac
words=text.split()
words = filter(lambda x: len(x)>=min_len,words)
counts =Counter(words)
counts = [(k,v) for k,v in counts.items()]

counts = sorted(counts, key = lambda item : -item[1])



graph = Pyasciigraph()
hist  = graph.graph('Histogram', counts)
for i in range(hist_size+2): #+2 bo pierwsze dwie linie to tutul itp
    if len(hist)>i:
        print(hist[i])
    else:
        print("no other suitable words were found!")
        break








