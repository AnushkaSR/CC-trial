DELIMITER $$
CREATE FUNCTION number_of_Comments(P_ID INT) 
RETURNS INT
DETERMINISTIC
BEGIN
    declare c INT;
    set c = (SELECT count(*) from post_comments WHERE post_comments.Post_ID = P_ID);
    RETURN c;
END
$$ 
DELIMITER;