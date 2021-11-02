from configparser import Error
from typing import Tuple
import mysql.connector 
from helper import get_time_from_string;
from mysqlhelper import  closeMysqlconnection
from datetime import datetime
import config
from user_model import BasicUserProfile

from werkzeug.security import generate_password_hash, check_password_hash
from mysql.connector.cursor import MySQLCursorDict, MySQLCursorPrepared

 

def connect_to_db():
    hrm_db=mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database  
    return hrm_db
 
   
def get_sql_version():
        try:             
            hrm_db =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database,connect_timeout=10000 )#established connection between your database   
            
            my_cursor = hrm_db.cursor(dictionary = True)
            
            query = "SELECT version()"
        
            
            my_cursor.execute(query)
            
            results = my_cursor.fetchone()
            if(results is None):
                return None
                         
            return results["version()"]               
        except mysql.connector.Error as err:
            print (err)     
        finally:
            closeMysqlconnection(hrm_db, my_cursor)                   
        
        return None
        
def get_gender():
        try:             
            hrm_db =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database,connect_timeout=10000 )#established connection between your database   
            
            my_cursor = hrm_db.cursor(dictionary = True)
            
            query = "SELECT * from Gender"        
            
            my_cursor.execute(query)
            
            results = my_cursor.fetchall()
            if(results is None):
                return None
                         
            return results;             
        except mysql.connector.Error as err:
            print (err)     
        finally:
            closeMysqlconnection(hrm_db, my_cursor)                   
        
        return None

def create_user_profile_basic(user_l : BasicUserProfile)  :
    try:     
            
            hrm_db =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            dob = get_time_from_string(user_l['dob'])
            print(user_l)
            doj = get_time_from_string(user_l['doj'])            
            hash_password = generate_password_hash(user_l["password"])   
            my_cursor=hrm_db.cursor()                
            my_cursor.callproc('sp_add_new_profile', 
                (user_l['email'], 
                 user_l['first_name'], 
                 user_l['last_name'], 
                 dob, 
                 doj , 
                 user_l['phone_number'],
                  hash_password , 
                 user_l['photourl']))       
            hrm_db.commit()
            results = my_cursor.stored_results()
            for result in results:
                return result.fetchone()
    except mysql.connector.Error as err:
            print (err)        
            
    finally:
            closeMysqlconnection(hrm_db, my_cursor)  
    return None    

    # def check_user(, username, password):
    #     try: 
    #         hrm_db =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
    #         my_cursor = hrm_db.cursor(dictionary = True)
    #         query = "SELECT u.user_id, u.password, u.email, u.first_name, u.last_name, ur.role_id FROM users u LEFT JOIN users_role ur ON u.user_id = ur.user_id  WHERE email = %s"
        
    #         tuple1 = [username]
    #         my_cursor.execute(query, tuple1)
    #         results = my_cursor.fetchone()          
    #         if(check_password_hash(results['password'], password)):
    #             return results
    #         else:
    #             return None                
    #     except mysql.connector.Error as err:
    #         print (err)
    #     finally:
    #         closeMysqlconnection(hrm_db, my_cursor)         
        
    #     return None

    # def create_user(, user_l):
    #     try:      
            
    #         hrm_db =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            
    #         my_cursor=hrm_db.cursor()    
    #         hash_password = generate_password_hash(user_l["password"])    
    #         my_cursor.callproc('SP_AddNewUser', (user_l['email'],  user_l['first_name'], user_l['last_name'], hash_password))       
    #         hrm_db.commit()
    #         results = my_cursor.stored_results()
    #         for result in results:
    #             return result.fetchone()
    #     except mysql.connector.Error as err:
    #         print (err)          
            
    #     finally:
    #         closeMysqlconnection(hrm_db, my_cursor)  
    #     return None    

print(get_gender())