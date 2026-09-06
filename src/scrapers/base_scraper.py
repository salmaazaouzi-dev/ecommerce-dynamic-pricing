import os
import random
from datetime import datetime
from typing import Dict, List, Any
from bs4 import BeautifulSoup


class BaseECommerceScraper:
    """
    Scraper module designed to fetch product prices and client reviews
    from target e-commerce competitor platforms.
    """

    def __init__(self, competitor_name: str):
        self.competitor_name = competitor_name

    def parse_html_content(self, html_raw: str) -> Dict[str, Any]:
        """
        Extracts structural product details from raw HTML content.
        """
        soup = BeautifulSoup(html_raw, "html.parser")
        
        title_element = soup.select_one(".product-title") or soup.select_one("h1")
        price_element = soup.select_one(".product-price") or soup.select_one(".price")

        title = title_element.get_text(strip=True) if title_element else "Unknown Product"
        price_text = price_element.get_text(strip=True) if price_element else "0.0"

        return {
            "title": title,
            "raw_price": price_text,
            "scraped_at": datetime.utcnow().isoformat()
        }

    def fetch_mock_price_update(self, product_id: int, base_price: float) -> Dict[str, Any]:
        """
        Simulates live competitor pricing variations around a base price.
        """
        variation_percentage = random.uniform(-0.12, 0.08)
        scraped_price = round(base_price * (1 + variation_percentage), 2)
        is_available = random.choice([True, True, True, False])

        return {
            "product_id": product_id,
            "competitor_name": self.competitor_name,
            "scraped_price": scraped_price,
            "is_available": is_available,
            "scraped_at": datetime.utcnow().isoformat()
        }

    def fetch_mock_reviews(self, product_id: int) -> List[Dict[str, Any]]:
        """
        Generates simulated user reviews for NLP sentiment analysis pipeline.
        """
        sample_reviews = [
            {"rating": 5.0, "text": "Excellent quality for the price! Delivery was ultra fast."},
            {"rating": 4.0, "text": "Solid product, works as expected. A bit pricey though."},
            {"rating": 2.0, "text": "Customer support was unhelpful and shipping took two weeks."},
            {"rating": 1.0, "text": "Defective on arrival. Would not recommend to anyone."},
            {"rating": 5.0, "text": "Best purchase I made this year, highly recommended!"}
        ]

        reviews = []
        selected_samples = random.sample(sample_reviews, k=3)
        
        for item in selected_samples:
            reviews.append({
                "product_id": product_id,
                "competitor_name": self.competitor_name,
                "rating": item["rating"],
                "review_text": item["text"]
            })

        return reviews


if __name__ == "__main__":
    scraper = BaseECommerceScraper(competitor_name="TechMart")
    sample_data = scraper.fetch_mock_price_update(product_id=101, base_price=299.99)
    print("Sample Scraped Price Data:", sample_data)
