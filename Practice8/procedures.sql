
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_phone ~ '^[0-9]+$' THEN
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone)
        ON CONFLICT (name)
        DO UPDATE SET phone = EXCLUDED.phone;
    ELSE
        RAISE NOTICE 'Invalid phone: %', p_phone;
    END IF;
END;
$$;



CREATE OR REPLACE PROCEDURE upsert_many_contacts(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1)
    LOOP
        CALL upsert_contact(p_names[i], p_phones[i]);
    END LOOP;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_contact(
    p_key TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_key OR phone = p_key;
END;
$$;