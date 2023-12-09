import re

def format_sentence(sentence):
    return ' '.join(sentence.strip().capitalize().split())

def split_into_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [format_sentence(sentence) for sentence in sentences if sentence.strip()]
    return sentences

def main():
    paragraphs = []
    try:
        while True:
            line = input()
            paragraphs.append(line)
    except EOFError:
        pass
    text = ' '.join(paragraphs)
    sentences = split_into_sentences(text)
    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()
