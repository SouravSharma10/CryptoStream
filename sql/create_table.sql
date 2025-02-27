CREATE TABLE bitcoin_price (
    id SERIAL PRIMARY KEY,
    time_updated TIMESTAMP,
    usd_rate REAL,
    code VARCHAR(10)
);
