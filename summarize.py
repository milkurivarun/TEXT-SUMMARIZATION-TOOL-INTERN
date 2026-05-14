from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Input text
text = """
Artificial Intelligence (AI) is rapidly changing the world.
It helps automate tasks, improve efficiency, and support decision-making.
AI is used in healthcare, education, banking, and transportation.
Machine learning and deep learning are important branches of AI.
As technology grows, AI will continue to impact everyday life.
"""

# Parse the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Create summarizer
summarizer = LsaSummarizer()

# Generate summary
summary = summarizer(parser.document, 2)

print("\nOriginal Text:\n")
print(text)

print("\nSummary:\n")

for sentence in summary:
    print(sentence)
