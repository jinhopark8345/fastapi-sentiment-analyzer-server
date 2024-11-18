from transformers import pipeline

model_path = "./models/cardiffnlp_twitter-roberta-base-sentiment-latest"
model = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)


def get_model():
    return model
