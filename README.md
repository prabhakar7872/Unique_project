# Unique_project
This is Sql code that is use in snowflack conector . Link Snowflack :-- https://diochgt-lc76553.snowflakecomputing.com
IF any one are use this code project . (That is set up on the snowflack conector. Steps:-)
1. Firstly user will create acount on the Snowflack conector.
2. Then create your on db paste that code in your db.
3. Then you will back on the python code change the username and the password over there.
Now we are sharing about that code when you will execute or say run. Steps :--
1. Then show that login or signup page . you go on that and fill every thing which are sowing over there.
2. Then When the successfully signup . Now user will go on the snowflack website run the sql code .
3. Then show the email and password in the backend .
4. Now user will come to the login page fill that email and password.
end.

CHANDIGARH_UNIVERSITY.PUBLIC.STUDENT_DETAILSCREATE TABLE Student_details (
    user_id INT AUTOINCREMENT PRIMARY KEY, -- Unique identifier for each user
    first_name VARCHAR(100) NOT NULL,      -- First name of the user
    last_name VARCHAR(100) NOT NULL,       -- Last name of the user
    email_id VARCHAR(255) NOT NULL UNIQUE, -- Email address, unique for each user
    phone_number VARCHAR(15),              -- Phone number of the user
    password VARCHAR(255) NOT NULL,        -- Password (hashed for security)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of signup
);

drop table Student_details;

desc table Student_details;

select * from student_details;

select phone_number, email_id from student_details;SNOWFLAKE
