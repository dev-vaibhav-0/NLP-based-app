import os
from huggingface_hub import InferenceClient

class API:
    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key="HF_TOKEN",
        )

    def sentiment_analysis(self, text):
        result = self.client.text_classification(
            text,
            model="tabularisai/multilingual-sentiment-analysis",
        )
        print(result)
        return result
    
    def ner(self, text):
        # Hugging Face NER model
        result = self.client.token_classification(
            text,
            model="dslim/bert-base-NER"
        )
        print(result)
        return result

    def emotion(self, text):
        # Hugging Face Emotion model
        result = self.client.text_classification(
            text,
            model="bhadresh-savani/distilbert-base-uncased-emotion"
        )
        print(result)
        return result
