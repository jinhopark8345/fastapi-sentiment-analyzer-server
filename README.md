# Forked from : https://github.com/curiousily/Deploy-BERT-for-Sentiment-Analysis-with-FastAPI

# What this project is about?
- Deploy a pre-trained BERT model for Sentiment Analysis as a REST API using FastAPI
- The model is trained to classify sentiment (negative, neutral, and positive) on a custom dataset from app reviews on Google Play. Here's a sample request to the API:

when the server is running (check out installation & setup from below sections), you can query like this.
```bash
http POST http://127.0.0.1:8081/predict text="Good basic lists, I would like to create more lists, but the annual fee for unlimited lists is too out there"
```

The response you'll get looks something like this:

```js
{
    "confidence": 0.9999083280563354,
    "probabilities": {
        "negative": 3.563107020454481e-05,
        "neutral": 0.9999083280563354,
        "positive": 5.596495248028077e-05
    },
    "sentiment": "neutral"
}
```

# Project Detail

Project structure
```bash
app/
├── main.py               # Main entry point for running the FastAPI app
├── db/
│   ├── base.py           # Database engine and Base declaration
│   ├── models.py         # SQLAlchemy models (e.g., User, Feedback)
│   └── session.py        # SessionLocal for database interactions
├── routers/
│   ├── feedback.py       # Endpoints for feedback
│   └── predict.py        # Endpoints for prediction
├── schemas/
│   ├── feedback.py       # Pydantic models for feedback
│   └── prediction.py     # Pydantic models for prediction
└── classifier/
    ├── model.py          # Model logic and `get_model` dependency
```

## Download model locally
```python
from transformers import pipeline
model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
model_save_path = "./model/cardiffnlp_twitter-roberta-base-sentiment-latest"

pipeline = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

sentence = "I am happy"

result = pipeline(sentence)
print(f"{result = }")

pipeline.save_pretrained(model_save_path)
```




## Local Installation

```sh
# Clone this repo:
git clone git@github.com:jinhopark8345/fastapi-sentiment-analyzer-server.git
cd  fastapi-sentiment-analyzer-server

# Activate your python virtual environment
# conda activate py310

# Install the dependencies
pip install -r requirements.txt
```

## Development Setup
```sh
# Precommit
pip install pre-commit
pre-commit install

# (optional)
pre-commit run --all-files
```

## Docker Installation
```sh
# Clone this repo:
git clone git@github.com:jinhopark8345/fastapi-sentiment-analyzer-server.git
cd  fastapi-sentiment-analyzer-server

# build docker image
docker build -t fastapi-sentiment-analyzer-server:1.0.0 .
```


## Test the setup

```sh
# Start the HTTP server:
uvicorn app.main:app --host 0.0.0.0 --port 8081

# Send a test request:
# (To install http command in Ubuntu: do "apt-get install http")
http POST http://localhost:8081/predict text="This app is a total waste of time!"
```

## License
MIT
