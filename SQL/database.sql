CREATE DATABASE IF NOT EXISTS voting_system;
USE voting_system;

CREATE TABLE IF NOT EXISTS candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    votes INT DEFAULT 0
);

INSERT INTO candidates (name) VALUES ('Neal Dunn (REP)'), ('Al Lawson (DEM)');
