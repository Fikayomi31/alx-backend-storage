-- Script that create a stored procedure ComputeAverageScoreForUser
-- that compute and store the average score for student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	SET @av = (SELECT AVG(score) AS av FROM corrections WHERE user_id=user_id);
	UPDATE users SET average_score = @av WHERE id = user_id;
END;
//
DELIMITER ;