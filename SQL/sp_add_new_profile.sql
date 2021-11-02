DELIMITER $$
DROP PROCEDURE IF EXISTS sp_add_new_profile $$
CREATE PROCEDURE sp_add_new_profile(
IN emailId VARCHAR(255),
IN fn VARCHAR(50),
IN ln VARCHAR(100),
IN dob DATETIME,
IN doJ DATETIME,
IN contactno nvarchar(255),
IN userpassword NVARCHAR(255),
IN photourl nvarchar(255)
)
BEGIN
	
    DECLARE userid INT;
	INSERT into Colleagues(First_name, Last_name, Email, Dob, DOJ, Contact_no, Password, Photo_url) values (fn, ln, emailId, dob, doj, contactno, userpassword, photourl ) ;
 
	SELECT User_id into userid FROM Colleagues where email = emailId;
    SELECT userid;
    
END$$

DELIMITER ;
