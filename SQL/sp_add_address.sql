DELIMITER $$
DROP PROCEDURE IF EXISTS sp_add_address $$
CREATE PROCEDURE sp_add_address(
IN emailid varchar(255),
IN ad_street varchar(255),
IN ad_city varchar(100),
IN ad_aptno varchar(150),
IN ad_state varchar(100),
IN ad_pincode varchar(100)
)
BEGIN
	-- Declare all variables
	DECLARE userid_local int;
    DECLARE addid INT;	
	DECLARE userid INT;	
    
    -- Get user id from email
    SELECT User_id into userid FROM Colleagues where Email = emailid LIMIT 1;
    
    -- Check mapping exisiting in table
	SELECT User_id into userid_local FROM Colleagues_mappings where User_id = userid LIMIT 1;    
     
     -- Check address exists in the table
    SELECT Add_id into addid from Address where Apt_no= ad_aptno and Street = ad_street and City=ad_city and State= ad_state and Pincode=ad_pincode  LIMIT 1;

	--  if does not exist add 
    if(addid is NULL or addid = "") then
		INSERT into Address(Apt_no, Street, City, State, Pincode) VALUES (ad_aptno,ad_street, ad_city , ad_state,ad_pincode );
	-- Else update exisitng entry
    else
		update Address set
			Apt_no = ad_aptno,
            Street =ad_street,
            City = ad_city,
            State = ad_state,
            Pincode =ad_pincode
	   where	
            Add_id = addid;
	end if;				

	SELECT Add_id into addid from Address where Apt_no= ad_aptno and Street = ad_street and City=ad_city and State= ad_state and Pincode=ad_pincode  LIMIT 1;
	
    if userid_local is NULL or userid_local = "" then		
		INSERT into Colleagues_mappings(User_id, Add_id) VALUES (userid, addid);
	else    
    
		update  Colleagues_mappings set
			 Add_id =  addid
		where 
			User_id = userid;			
    end if;    
END$$
DELIMITER ;


