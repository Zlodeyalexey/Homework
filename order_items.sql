CREATE TABLE IF NOT EXISTS order_items(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         INTEGER FOREIGN KEY (order_id) REFERENCES orders (id)
         INTEGER FOREIGN KEY (product_id) REFERENCES products (id)
     );