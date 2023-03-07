CREATE TABLE IF NOT EXISTS products(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title VARCHAR(36) NOT NULL UNIQUE,
         description VARCHAR(140) NOT NULL,
         category_id INTEGER NOT NULL,
         FOREIGN KEY (category_id) REFERENCES category (id)
     );