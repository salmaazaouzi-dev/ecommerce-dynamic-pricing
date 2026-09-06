import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Config de la page Streamlit
st.set_page_config(
    page_title="E-Commerce Dynamic Pricing Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 E-Commerce Dynamic Pricing & Benchmark Dashboard")
st.markdown("Automated competitor price monitoring and sentiment-driven price optimization.")

# Barre latérale pour la sélection des produits
st.sidebar.header("Product Selection")
selected_category = st.sidebar.selectbox("Category", ["Electronics", "Beauty", "Fashion"])
selected_product = st.sidebar.selectbox(
    "Select Product",
    ["Wireless Noise-Canceling Headphones", "Pro Gaming Mouse", "Mechanical Keyboard"]
)

# Données de démonstration
our_price = 149.99
competitor_data = pd.DataFrame({
    "Competitor": ["TechMart", "ElectroHub", "ZoneData", "GlobalShop"],
    "Price ($)": [139.99, 155.00, 129.90, 160.00],
    "Availability": ["In Stock", "In Stock", "Out of Stock", "In Stock"],
    "Is Anomaly": [False, False, True, False]
})

avg_competitor_price = competitor_data["Price ($)"].mean()
recommended_price = 144.50
sentiment_score = 0.45  # Positif

# Visualisation des métriques principales (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Our Current Price", value=f"${our_price:.2f}")
col2.metric(label="Market Avg Price", value=f"${avg_competitor_price:.2f}", delta=f"{avg_competitor_price - our_price:.2f}")
col3.metric(label="Recommended Price", value=f"${recommended_price:.2f}", delta="Optimal Margin")
col4.metric(label="Brand Sentiment Score", value=f"{sentiment_score:.2f} / 1.0", delta="Positive")

st.divider()

# Graphique comparatif des prix
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Competitor Price Benchmark")
    fig = px.bar(
        competitor_data,
        x="Competitor",
        y="Price ($)",
        color="Is Anomaly",
        color_discrete_map={True: "#EF553B", False: "#636EFA"},
        text_auto=".2f",
        title="Price Comparison across Competitors (Red = Price Anomaly)"
    )
    fig.add_hline(y=our_price, line_dash="dash", line_color="green", annotation_text="Our Price")
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("Market Summary")
    st.dataframe(competitor_data, use_container_width=True)

st.divider()

# Section NLP Sentiment Analysis
st.subheader("Customer Sentiment & Review Analysis")
reviews_df = pd.DataFrame({
    "Competitor": ["TechMart", "ElectroHub", "TechMart"],
    "Rating": [5.0, 2.0, 4.0],
    "Review Text": [
        "Excellent quality for the price! Delivery was ultra fast.",
        "Customer support was unhelpful and shipping took two weeks.",
        "Solid product, works as expected. A bit pricey though."
    ],
    "Sentiment": ["POSITIVE", "NEGATIVE", "POSITIVE"]
})

st.table(reviews_df)
