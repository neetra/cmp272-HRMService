CREATE TABLE IF NOT EXISTS `hrm_db`.`Colleagues_mappings` (
  `User_id` INT NOT NULL,
  `Salary_id` INT  NULL,
  `Add_id` INT  NULL,
  `Time_id` INT  NULL,
  `Gender_id` INT  NULL,
  `Des_id` INT  NULL,
  `M_id` INT  NULL,
  `Dep_id` INT  NULL,
  `Manager_id` INT  NULL,
  INDEX `fk_Colleagues_mappings_Colleagues_idx` (`User_id` ASC),
  INDEX `fk_Colleagues_mappings_Salary1_idx` (`Salary_id` ASC),
  INDEX `fk_Colleagues_mappings_Address1_idx` (`Add_id` ASC),
  INDEX `fk_Colleagues_mappings_Timesheet1_idx` (`Time_id` ASC),
  INDEX `fk_Colleagues_mappings_Gender1_idx` (`Gender_id` ASC),
  INDEX `fk_Colleagues_mappings_Designation1_idx` (`Des_id` ASC),
  INDEX `fk_Colleagues_mappings_Marital_status1_idx` (`M_id` ASC),
  INDEX `fk_Colleagues_mappings_Department1_idx` (`Dep_id` ASC),
  INDEX `fk_Colleagues_mappings_Colleagues1_idx` (`Manager_id` ASC),
  CONSTRAINT `fk_Colleagues_mappings_Colleagues`
    FOREIGN KEY (`User_id`)
    REFERENCES `hrm_db`.`Colleagues` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Salary1`
    FOREIGN KEY (`Salary_id`)
    REFERENCES `hrm_db`.`Salary` (`Salary_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Address1`
    FOREIGN KEY (`Add_id`)
    REFERENCES `hrm_db`.`Address` (`Add_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Timesheet1`
    FOREIGN KEY (`Time_id`)
    REFERENCES `hrm_db`.`Timesheet` (`Time_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Gender1`
    FOREIGN KEY (`Gender_id`)
    REFERENCES `hrm_db`.`Gender` (`Gender_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Designation1`
    FOREIGN KEY (`Des_id`)
    REFERENCES `hrm_db`.`Designation` (`Des_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Marital_status1`
    FOREIGN KEY (`M_id`)
    REFERENCES `hrm_db`.`Marital_status` (`M_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Department1`
    FOREIGN KEY (`Dep_id`)
    REFERENCES `hrm_db`.`Department` (`Dep_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Colleagues1`
    FOREIGN KEY (`Manager_id`)
    REFERENCES `hrm_db`.`Colleagues` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)