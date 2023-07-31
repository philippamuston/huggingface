## Initiate and test

```bash
python -m venv .env  
source .env/bin/activate
pip install torch torchvision
# ^ installs pytorch which is too big for git to handle!
python hello.py
#Hello, Phil
python torch_test.py
#Creates a list of vectors
python sentiment-analysis.py --txt 'i love it!'
#Rates sentiment of text
```


## Useful links:
https://huggingface.co/docs/transformers/installation
