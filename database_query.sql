CREATE EXTENSION IF NOT EXISTS "pgcrypto";  -- This is necessary to use gen_random_uuid()

SELECT * FROM pg_extension;

CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
    unique_nickname VARCHAR(80) NOT NULL,
    email VARCHAR(250) NOT NULL,
    number_phone VARCHAR(16) NOT NULL,
	displayed_nickname VARCHAR(140),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	last_enter TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
);

ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);
ALTER TABLE users ADD CONSTRAINT unique_nickname UNIQUE (unique_nickname);
ALTER TABLE users ADD CONSTRAINT unique_phone UNIQUE (number_phone);

