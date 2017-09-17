CREATE DATABASE example_app;

CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'db_password';

GRANT ALL PRIVILEGES ON *.* to 'db_user'@'localhost';

USE example_app;

CREATE TABLE users (
     username VARCHAR(50) PRIMARY KEY
    ,first_name VARCHAR(50)
    ,last_name VARCHAR(50)
    ,email VARCHAR(50)
    ,phone_number VARCHAR(50)
);

INSERT INTO users (username,first_name,last_name,email,phone_number) VALUES
     ('kgoedel','Kurt','Goedel',NULL,NULL)
    ,('mescher','MC','Escher','mc@eternalgoldenbraid.com',NULL)
    ,('jbach','Johann','Bach','jo@eternalgoldenbrain.com',NULL)
;

CREATE TABLE messages (
     message_id INT PRIMARY KEY AUTO_INCREMENT
    ,message varchar(100) NOT NULL
);

INSERT INTO messages (message) VALUES
     ('Introduction: A Musico-Logical Offering')
    ,('The MU-puzzle')
    ,('Meaning and Form in Mathematics')
    ,('Figure and Ground')
    ,('Consistency, Completeness, and Geometry')
    ,('Recursive Structures and Processes')
    ,('The Location of Meaning')
    ,('The Propositional Calculus')
    ,('Typographical Number Theory')
    ,('Mumon and Goedel')
;
