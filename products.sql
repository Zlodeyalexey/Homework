CREATE TABLE IF NOT EXISTS products(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title VARCHAR(36) NOT NULL UNIQUE,
         description VARCHAR(140) NOT NULL,
         INTEGER FOREIGN KEY (categories_id) REFERENCES categories (id)
     );