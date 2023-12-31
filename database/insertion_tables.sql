CREATE TABLE IF NOT EXISTS family (
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS property (
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS usage (
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS cosmetic (
    id UUID // generated by default
    name VARCHAR(100) NOT NULL,
    expiry_date DATE NOT NULL,
    initial_quantity SMALLINT NOT NULL,
    current_quantity SMALLINT,
    family VARCHAR(100),
    price MONEY,
    prefered_usage VARCHAR(100),
    PRIMARY KEY (name, expiry_date),
    FOREIGN KEY (family) REFERENCES family (name),
    FOREIGN KEY (usage) REFERENCES usage (name)
);

CREATE TABLE IF NOT EXISTS cosmetic_usage_per_property (
   id_cosmetic UUID,
   property_name VARCHAR(100),
   PRIMARY KEY (id_cosmetic, property_name),
   FOREIGN KEY (id_cosmetic) REFERENCES cosmetic (id),
   FOREIGN KEY (property_name) REFERENCES property (name)
);