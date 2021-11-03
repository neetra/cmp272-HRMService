DELIMITER $$
DROP PROCEDURE IF EXISTS sp_add_other_details $$
CREATE PROCEDURE sp_add_other_details(
IN emailid VARCHAR(255),
IN dep_id int,
IN m_id int,
IN g_id int,
IN des_id int
)
BEGIN 
	-- Declare all variables
	DECLARE userid_local int;
    DECLARE addid INT;	
	DECLARE userid INT;	
    
    -- Get user id from email
    SELECT User_id into userid FROM Colleagues where Email = emailid LIMIT 1; 

	SELECT  User_id into userid_local FROM Colleagues_mappings where User_id = userid;

    if userid_local is NULL or userid_local = "" then
		INSERT into Colleagues_mappings(User_id, Gender_id, Des_id, M_id, Dep_id ) VALUES (userid, g_id, des_id, m_id, dep_id);
	else 
		update  Colleagues_mappings set
			 Gender_id  = g_id ,
             Des_id = des_id,
             Dep_id = dep_id,
             M_id = m_id
		where 
			User_id =userid;			
    end if;
END$$

DELIMITER ;


