DELIMITER $$
DROP PROCEDURE IF EXISTS sp_get_user_details $$
CREATE PROCEDURE sp_get_user_details(
IN emailid VARCHAR(255)

)
BEGIN 
	-- Declare all variables

	DECLARE userid INT;	
    
    -- Get user id from email
    SELECT User_id into userid FROM Colleagues where Email = emailid LIMIT 1; 

	SELECT 
    c.User_id,  c.First_Name, c.Last_name, c.Email, c.Dob, c.DOJ, c.Contact_no, c.Photo_url, des.Des_Name , dep.Dep_name, g.Gender_name, ms.M_name
 
FROM
    Colleagues c
        LEFT JOIN
    Colleagues_mappings cp ON c.User_id = cp.User_id
		LEFT JOIN 
	Designation des on cp.Des_id = des.Des_id
		LEFT JOIN 
	Department dep on cp.Dep_id = dep.Dep_id
		LEFT JOIN 
	Gender g on cp.Gender_id = g.Gender_id
		LEFT JOIN 
	Marital_status ms on cp.M_id = ms.M_id
    WHERE
    c.User_id = userid;
   
END$$

DELIMITER ;


