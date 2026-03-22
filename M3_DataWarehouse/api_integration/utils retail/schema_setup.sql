-- Capa de Staging: Datos crudos de Kaggle
CREATE TABLE IF NOT EXISTS staging_orders (
    invoice_no VARCHAR(20),
    stock_code VARCHAR(20),
    description TEXT,
    quantity INTEGER,
    invoice_date TIMESTAMP,
    unit_price DECIMAL(10,2),
    customer_id VARCHAR(20),
    country VARCHAR(50)
);

-- Capa de Warehouse: Datos de las llamadas (Voice AI Logs)
CREATE TABLE IF NOT EXISTS call_logs (
    call_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(20),
    transcription TEXT,
    call_duration_seconds INTEGER,
    call_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ai_sentiment VARCHAR(20),
    ai_summary TEXT,
    is_resolved BOOLEAN DEFAULT FALSE
);

-- Índices para velocidad de respuesta en la llamada (Latencia 2026)
CREATE INDEX idx_customer_id ON staging_orders(customer_id);
CREATE INDEX idx_call_timestamp ON call_logs(call_timestamp);
