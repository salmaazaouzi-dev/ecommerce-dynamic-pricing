from typing import Dict, Any


class SentimentAnalyzer:
    """
    NLP Engine to analyze customer review sentiment.
    Determines polarity scores and categorical labels for e-commerce products.
    """

    def __init__(self):
        # Lexicon keywords for lightweight sentiment inference
        self.positive_keywords = [
            "excellent", "great", "fast", "solid", "recommend",
            "best", "love", "high quality", "good", "perfect"
        ]
        self.negative_keywords = [
            "pricey", "unhelpful", "defective", "slow", "bad",
            "poor", "broken", "terrible", "worst", "disappointed"
        ]

    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Analyzes raw review text and computes a sentiment score and label.
        
        Score mapping:
        - Range: [-1.0, 1.0]
        - Label: POSITIVE (score > 0.2), NEGATIVE (score < -0.2), NEUTRAL otherwise.
        """
        if not text:
            return {"sentiment_score": 0.0, "sentiment_label": "NEUTRAL"}

        lowered_text = text.lower()
        pos_count = sum(1 for word in self.positive_keywords if word in lowered_text)
        neg_count = sum(1 for word in self.negative_keywords if word in lowered_text)

        total_matches = pos_count + neg_count

        if total_matches == 0:
            score = 0.0
            label = "NEUTRAL"
        else:
            score = round((pos_count - neg_count) / total_matches, 2)
            if score > 0.2:
                label = "POSITIVE"
            elif score < -0.2:
                label = "NEGATIVE"
            else:
                label = "NEUTRAL"

        return {
            "sentiment_score": score,
            "sentiment_label": label
        }


if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    sample_review = "Excellent quality for the price! Delivery was ultra fast."
    result = analyzer.analyze_text(sample_review)
    print(f"Review: '{sample_review}'")
    print(f"Analysis Result: {result}")
