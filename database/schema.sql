-- Table mapping core product catalog
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT UNIQUE NOT NULL,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    our_price REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table tracking daily competitor price points
CREATE TABLE IF NOT EXISTS competitor_prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER REFERENCES products(product_id),
    competitor_name TEXT NOT NULL,
    scraped_price REAL NOT NULL,
    is_available BOOLEAN DEFAULT 1,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table storing customer reviews for NLP sentiment analysis
CREATE TABLE IF NOT EXISTS product_reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER REFERENCES products(product_id),
    competitor_name TEXT,
    rating REAL,
    review_text TEXT,
    sentiment_score REAL,
    sentiment_label TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
