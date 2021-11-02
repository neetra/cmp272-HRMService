DELIMITER $$
DROP PROCEDURE IF EXISTS sp_add_other_details $$
CREATE PROCEDURE sp_add_other_details(
IN userid int,
IN dep_id int,
IN m_id int,
IN g_id int,
IN des_id int
)
BEGIN  
	DECLARE userid_local int;
	SELECT  User_id into userid_local FROM Colleagues_mappings where User_id = userid;
    Select userid_local;
    if userid_local != null then
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


