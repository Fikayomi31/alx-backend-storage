-- Script that creates trigger that reset email
-- The attribute valid_email only when the email has change

DELIMITER //
CREATE TRIGGER update_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
//
DELIMITER;
