import json
import sys

def main():
    tweet_file = open(sys.argv[1])
    term_incidence_count = 0
    term_count_map = {}
    for line in tweet_file:
        json_parse = json.loads(line)
        if json_parse.has_key("text"):
            tweet_text = json_parse["text"]
            tweet_terms = tweet_text.split()
            for term in tweet_terms:
                if term_count_map.has_key(term):
                    term_count_map[term] += 1
                else:
                    term_count_map[term] = 1
                term_incidence_count += 1
    for key in term_count_map.keys():
        print key, float(term_count_map[key]) / term_incidence_count

if __name__ == '__main__':
    main()