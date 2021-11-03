ALTER TABLE Colleagues_mappings
ADD PRIMARY KEY(User_id);

ALTER  TABLE Address
ADD UNIQUE INDEX idx_name (Add_id, Apt_no, Street, City, State, Pincode);

