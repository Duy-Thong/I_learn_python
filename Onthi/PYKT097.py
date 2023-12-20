import re

def main():
    list = []
    
    while True:
        try:
            line = input()
            line = line.strip().lower()
            exp = ".?!"
            if line[-1] in exp:
                line = line[:-1] + " "+line[-1]
            if  line[-1] not in exp :
                line += ' .'
    
            tmp = re.split(r'\s+',line)
        
            index = 0
            result = []
            for i in range(len(tmp)):
                if tmp[i] in exp:
                    sentence = tmp[index:i+1]
                    index = i + 2
                    s=" ".join(sentence)
                    s[0].capitalize()
                    result.append((" ".join(sentence[:-1]) + sentence[-1]).capitalize())
            list.extend(result)

        except EOFError:
            break
    for i in list:
        print(i)



if __name__ == "__main__":
    main()
