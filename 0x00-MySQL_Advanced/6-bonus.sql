-- Script that create a stored procedure AddBonus that add
-- A new correction for a student

DELIMITER //
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	DECLARE exist_id INT;

	SELECT id INTO exist_id FROM projects WHERE name=project_name;
	IF exist_id IS NULL THEN
		INSERT INTO projects (name) VALUES (projecr_name);
		SET curr 
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, (SELECT id FROM projects WHERE name=project_name), score);
END;
//
DELIMITER ;
