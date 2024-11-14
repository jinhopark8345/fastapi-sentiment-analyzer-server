# Forked from : https://github.com/curiousily/Deploy-BERT-for-Sentiment-Analysis-with-FastAPI

# Project Structure
```bash
app/
├── main.py               # Main entry point for running the FastAPI app
├── db/
│   ├── base.py           # Database engine and Base declaration
│   ├── models.py         # SQLAlchemy models (e.g., User, Feedback)
│   └── session.py        # SessionLocal for database interactions
├── routers/
│   ├── feedback.py       # Endpoints related to feedback
│   └── predict.py        # Endpoint for prediction
├── schemas/
│   ├── feedback.py       # Pydantic models for feedback
│   └── prediction.py     # Pydantic models for prediction
└── classifier/
    ├── model.py          # Model logic and `get_model` dependency
```

# Deploy BERT for Sentiment Analsysi with FastAPI
Deploy a pre-trained BERT model for Sentiment Analysis as a REST API using FastAPI

## Demo
The model is trained to classify sentiment (negative, neutral, and positive) on a custom dataset from app reviews on Google Play. Here's a sample request to the API:

```bash
http POST http://127.0.0.1:8000/predict text="Good basic lists, i would like to create more lists, but the annual fee for unlimited lists is too out there"
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

You can also [read the complete tutorial here](https://www.curiousily.com/posts/deploy-bert-for-sentiment-analysis-as-rest-api-using-pytorch-transformers-by-hugging-face-and-fastapi/)

## Installation

Clone this repo:

```sh
git clone git@github.com:curiousily/Deploy-BERT-for-Sentiment-Analysis-with-FastAPI.git
cd Deploy-BERT-for-Sentiment-Analysis-with-FastAPI
```

Install the dependencies:

```sh
# activate your python virtual environment
# conda activate py310

# pip install gdown fastapi uvicorn pydantic torch transformers
pip install -r requirements.txt
```

Download the pre-trained model:

```python
import gdown

gdown.download(
    "https://drive.google.com/uc?id=1V8itWtowCYnb2Bc9KlK9SxGff9WwmogA",
    "assets/model_state_dict.bin",
)
```

## Test the setup

Start the HTTP server:

```sh
uvicorn sentiment_analyzer.api:app
```

Send a test request:

```sh
# for http command in macOS, brew install httpie
http POST http://localhost:8000/predict text="This app is a total waste of time!"
```

## License

MIT
