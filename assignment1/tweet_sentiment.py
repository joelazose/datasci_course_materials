import json
import sys

def hw(sent_file, tweet_file):
    scores = parse_sentiment_file(sent_file)
    for line in tweet_file:
        score = 0
        json_parse = json.loads(line)
        if json_parse.has_key("text"):
            tweet_text = json_parse["text"]
            tweet_terms = tweet_text.split()
            for term in tweet_terms:
                if scores.has_key(term):
                    score += scores[term]
        print score

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

def parse_sentiment_file(afinnfile):
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

if __name__ == '__main__':
    main()
