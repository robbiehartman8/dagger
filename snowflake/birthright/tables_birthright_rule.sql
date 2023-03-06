-- this file creates the birthright.birthright_rule table

use dagger.birthright;

create table if not exists birthright.birthright_rule (
    -- default attributes
    birthright_rule_id varchar(255) not null primary key,
    create_ts datetime not null default current_timestamp,
    -- birthright_rule attributes
    status boolean null,
    access_catalog_id varchar(255) not null,
    rule variant not null
);

create stream if not exists birthright_rule_stream on table birthright_rule;

create table if not exists birthright.birthright_rule_aud (
    -- audit attributes
    audit_insert_ts datetime not null default current_timestamp,
    audit_action varchar(10) not null,
    audit_is_update varchar(10) not null,
    -- default attributes
    birthright_rule_id varchar(255) not null,
    create_ts datetime not null default current_timestamp,
    -- birthright_rule attributes
    status boolean null,
    access_catalog_id varchar(255) not null,
    rule variant not null
);


-- insert into birthright.birthright_rule(birthright_rule_id, status, access_catalog_id, rule) select '1', True, '1',
-- parse_json($${
--   "job_title_code": "eng",
--   "location_code": "1001"
-- }$$);

-- select birthright_rule_id, access_catalog_id, rule
-- from birthright.birthright_rule
-- where 
-- (rule:location_code::varchar = '1003' or rule:location_code::varchar = 'NULL' or rule:location_code::varchar is null)
-- and
-- (rule:job_title_code::varchar = 'ceo' or rule:job_title_code::varchar = 'NULL' or rule:job_title_code::varchar is null)
-- and
-- (rule:job_title_level::varchar = '100' or rule:job_title_level::varchar = 'NULL' or rule:job_title_level::varchar is null)
-- and
-- (rule:employee_type::varchar = 'ft' or rule:employee_type::varchar = 'NULL' or rule:employee_type::varchar is null)
-- ;