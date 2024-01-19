-- Script that create a stored procedure ComputeAverageScoreForUser
-- that compute and store the average score for student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avgscore FLOAT;
	SELECT AVG(score) AS avgscore FROM corrections AS c WHERE c.user_id=user_id;
	UPDATE users SET average_score = avgscore WHERE id = user_id;
END;
//
DELIMITER ;
