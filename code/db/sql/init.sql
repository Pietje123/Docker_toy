
CREATE DATABASE IF NOT EXISTS `db_name`;
USE `db_name`;

CREATE TABLE users (
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50),
  birthdate DATE,
  PRIMARY KEY (user_id)
);

CREATE TABLE pofjes (
  pof_id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL, 
  price FLOAT,
  date DATE,
  PRIMARY KEY (pof_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (username, birthdate)
VALUES ("HENK", "1970-01-01");