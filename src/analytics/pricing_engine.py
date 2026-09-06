from typing import List, Dict, Any
import numpy as np


class PricingEngine:
    """
    Analytics engine for dynamic pricing benchmark, anomaly detection,
    and target price optimization.
    """

    def calculate_market_stats(self, competitor_prices: List[float]) -> Dict[str, float]:
        """
        Computes summary statistics for a set of competitor price points.
        """
        if not competitor_prices:
            return {"mean_price": 0.0, "min_price": 0.0, "max_price": 0.0, "std_price": 0.0}

        prices_arr = np.array(competitor_prices)
        return {
            "mean_price": float(round(np.mean(prices_arr), 2)),
            "min_price": float(round(np.min(prices_arr), 2)),
            "max_price": float(round(np.max(prices_arr), 2)),
            "std_price": float(round(np.std(prices_arr), 2))
        }

    def detect_price_anomalies(
        self, competitor_prices: List[Dict[str, Any]], threshold_z: float = 1.2
    ) -> List[Dict[str, Any]]:
        """
        Identifies pricing anomalies using Z-score calculation.
        Flags price points that significantly deviate from competitor mean.
        """
        prices = [item["scraped_price"] for item in competitor_prices]
        if len(prices) < 2:
            for item in competitor_prices:
                item["is_anomaly"] = False
            return competitor_prices

        mean_price = np.mean(prices)
        std_price = np.std(prices)

        for item in competitor_prices:
            if std_price == 0:
                z_score = 0.0
            else:
                z_score = (item["scraped_price"] - mean_price) / std_price

            item["z_score"] = float(round(z_score, 2))
            item["is_anomaly"] = bool(abs(z_score) > threshold_z)

        return competitor_prices

    def recommend_optimal_price(
        self,
        our_current_price: float,
        avg_competitor_price: float,
        avg_sentiment_score: float
    ) -> float:
        """
        Generates an optimized price recommendation based on competitor benchmark
        and product sentiment score.
        """
        if avg_competitor_price <= 0:
            return our_current_price

        # Pricing strategy logic
        price_gap = avg_competitor_price - our_current_price

        # Sentiment factor: Premium brand perception allows higher price margin
        if avg_sentiment_score > 0.3:
            sentiment_modifier = 1.04
        elif avg_sentiment_score < -0.3:
            sentiment_modifier = 0.96
        else:
            sentiment_modifier = 1.00

        recommended_price = (our_current_price + (price_gap * 0.4)) * sentiment_modifier
        return float(round(recommended_price, 2))


if __name__ == "__main__":
    engine = PricingEngine()
    sample_prices = [
        {"competitor": "CompA", "scraped_price": 100.0},
        {"competitor": "CompB", "scraped_price": 105.0},
        {"competitor": "CompC", "scraped_price": 65.0}  # Anomaly candidate
    ]
    analyzed = engine.detect_price_anomalies(sample_prices)
    rec_price = engine.recommend_optimal_price(
        our_current_price=98.0,
        avg_competitor_price=90.0,
        avg_sentiment_score=0.5
    )
    print("Anomalies analysis:", analyzed)
    print("Recommended Price:", rec_price)
