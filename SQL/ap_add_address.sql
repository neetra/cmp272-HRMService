DELIMITER $$
DROP PROCEDURE IF EXISTS sp_add_address $$
CREATE PROCEDURE sp_add_address(
IN userid int,
IN ad_street varchar(255),
IN ad_city varchar(100),
IN ad_aptno varchar(150),
IN ad_state varchar(100),
IN ad_pincode varchar(100)
)
BEGIN
	DECLARE userid_local int;
    DECLARE addid INT;	
	SELECT  User_id into userid_local FROM Colleagues_mappings where User_id = userid;
    Select userid_local;
    
    INSERT into Address(Apt_no, Street, City, state, Pincode) VALUES (ad_aptno,ad_street, ad_city , ad_state,ad_pincode );
	SELECT Add_id into addid from Address where Apt_no= ad_aptno  LIMIT 1;
	if userid_local != null then
		INSERT into Colleagues_mappings(User_id, Add_id) VALUES (userid, addid);
	else 
		update  Colleagues_mappings set
			 Add_id =  addid
		where 
			User_id = userid;			
    end if;
    
END$$

DELIMITER ;


