import time
import random
from datetime import datetime
import pandas as pd
from config import STREAM_DELAY

PRODUCTS = [
    ("Laptop", "Electronics", 900, 1500),
    ("Headphones", "Electronics", 50, 200),
    ("T-Shirt", "Apparel", 10, 30),
    ("Shoes", "Apparel", 40, 120),
    ("Coffee", "Grocery", 3, 8)
]

def generate_sale():
    product, category, p_min, p_max = random.choice(PRODUCTS)
    price = round(random.uniform(p_min, p_max), 2)
    quantity = random.randint(1, 5)

    return {
        "timestamp": datetime.now().isoformat(),
        "product": product,
        "category": category,
        "quantity": quantity,
        "price": price,
        "total": round(price * quantity, 2)
    }

def generate_stream():
    while True:
        record = generate_sale()
        df = pd.DataFrame([record])
        df.to_csv("data/stream.csv", mode="a", header=False, index=False)
        print("Generated:", record)
        time.sleep(int(STREAM_DELAY))

if __name__ == "__main__":
    generate_stream()
