-- this file creates the identity.identity table

use dagger.identity;

create table if not exists identity.identity_tmp (
    -- default attributes
    identity_id varchar(255) not null,
    create_ts datetime not null,
    update_ts datetime not null,
    -- identity attributes
    hr_id varchar(100) not null,
    user_id varchar(100) not null,
    legal_first_name varchar(255) null,
    legal_middle_name varchar(255) null,
    legal_last_name varchar(255) null,
    preferred_first_name varchar(255) null,
    preferred_middle_name varchar(255) null,
    preferred_last_name varchar(255) null,
    job_title_code varchar(100) null,
    job_title_description varchar(100) null,
    job_title_level varchar(100) null,
    location_code varchar(100) null,
    location_name varchar(100) null,
    location_address varchar(100) null,
    phone_number_work varchar(100) null,
    phone_number_work_mobile varchar(100) null,
    phone_number_home varchar(100) null,
    phone_number_home_mobile varchar(100) null,
    email_work varchar(500) null,
    email_home varchar(500) null,
    status varchar(100) null,
    hire_start_date varchar(100) null,
    termination_date varchar(100) null,
    leave_of_absense_start_date varchar(100) null,
    leave_of_absense_end_date varchar(100) null,
    employee_type varchar(100) null,
    cost_center varchar(100) null,
    --manager_identity_id varchar(100) null, create query to populate this
    manager_hr_id varchar(100) null,
    manager_user_id varchar(100) null
);

create table if not exists identity.identity (
    -- default attributes
    identity_id varchar(255) not null primary key,
    create_ts datetime not null,
    update_ts datetime not null,
    -- identity attributes
    hr_id varchar(100) not null,
    user_id varchar(100) not null,
    legal_first_name varchar(255) null,
    legal_middle_name varchar(255) null,
    legal_last_name varchar(255) null,
    preferred_first_name varchar(255) null,
    preferred_middle_name varchar(255) null,
    preferred_last_name varchar(255) null,
    job_title_code varchar(100) null,
    job_title_description varchar(100) null,
    job_title_level varchar(100) null,
    location_code varchar(100) null,
    location_name varchar(100) null,
    location_address varchar(100) null,
    phone_number_work varchar(100) null,
    phone_number_work_mobile varchar(100) null,
    phone_number_home varchar(100) null,
    phone_number_home_mobile varchar(100) null,
    email_work varchar(500) null,
    email_home varchar(500) null,
    status varchar(100) null,
    hire_start_date varchar(100) null,
    termination_date varchar(100) null,
    leave_of_absense_start_date varchar(100) null,
    leave_of_absense_end_date varchar(100) null,
    employee_type varchar(100) null,
    cost_center varchar(100) null,
    --manager_identity_id varchar(100) null, create query to populate this
    manager_hr_id varchar(100) null,
    manager_user_id varchar(100) null
);