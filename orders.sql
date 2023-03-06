CREATE TABLE IF NOT EXISTS orders(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         INTEGER FOREIGN KEY (user_id) REFERENCES users (id)
         INTEGER FOREIGN KEY (status_id) REFERENCES statuses (id)
     );

