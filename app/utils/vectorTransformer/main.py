from sentence_transformers import SentenceTransformer



class VectorTransformer:

    def __init__(self):
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')

    def transform(self, sentences):
        return self.model.encode(sentences)