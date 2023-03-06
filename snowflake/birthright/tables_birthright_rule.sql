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