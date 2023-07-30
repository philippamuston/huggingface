
from transformers import pipeline

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--txt',  type=str, help='the text to be sentiment analysed')
args = parser.parse_args()

if args.txt:
    print(f"Analysing sentiment of text : {args.txt}")
    print(pipeline('sentiment-analysis')(args.txt))
