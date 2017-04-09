#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated)

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        words = text_string


        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)


        stemmer = SnowballStemmer("english")

        to_stem = text_string.replace('\n', ' ').replace('  ', ' ').split()
        to_stem2 = text_string.split()
        if to_stem != to_stem2:
            print "Double Whitespace or line break found!"
            print to_stem
            print to_stem2

        after_stem = []
        for word in to_stem:
            after_stem.append(stemmer.stem(word))

        if len(to_stem) != len(after_stem):
            print "Stemmed not same size as unstemmed!"
            print to_stem
            print after_stem


        # #print "words stemmed: ", words_stem
        words = " ".join(after_stem)
        words = words.replace('\n', ' ').replace('  ', ' ')



    return words



def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

