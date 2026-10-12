import sys 
import emoji

if len(sys.argv < [2]):
    sys.exit("Too few arguments!")
text = sys.argv[1]
print(emoji.emojize(text, language= "alias"))


