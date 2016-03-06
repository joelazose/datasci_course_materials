import json
import sys

def main():
    tweet_file = open(sys.argv[1])
    hashtag_count_map = {}
    for line in tweet_file:
        json_parse = json.loads(line)
        if json_parse.has_key("entities"):
            tweet_entities = json_parse["entities"]
            if tweet_entities.has_key("hashtags"):
                tweet_hashtags = tweet_entities["hashtags"]
                for hashtag in tweet_hashtags:
                    if hashtag.has_key("text"):
                        hashtag_text = hashtag["text"]
                        if hashtag_count_map.has_key(hashtag_text):
                            hashtag_count_map[hashtag_text] += 1
                        else:
                            hashtag_count_map[hashtag_text] = 1

    for h in sorted(hashtag_count_map, key = hashtag_count_map.get, reverse=True)[:10]:
        print h, hashtag_count_map[h]

if __name__ == '__main__':
    main()