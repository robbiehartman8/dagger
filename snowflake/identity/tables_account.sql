-- this file creates the identity.account table

-- TODO: stream and sproc
-- TODO: action flags in the table

use dagger.identity;

create table if not exists identity.account (
    -- default attributes
    account_id varchar(255) not null primary key,
    create_ts datetime not null,
    -- account attributes
    identity_correliation_attribute varchar(255) null,
    platform varchar(255) null,
    application varchar(255) null,
    user_name varchar(255) null,
    last_login datetime,
    account_status varchar(255),
    account_provisioned boolean
);

create stream if not exists account_stream on table account;

create table if not exists identity.account_aud (
    -- audit attributes
    audit_insert_ts datetime not null default current_timestamp,
    audit_action varchar(10) not null,
    audit_is_update varchar(10) not null,
    -- default attributes
    account_id varchar(255) not null,
    create_ts datetime not null,
    -- account attributes
    identity_correliation_attribute varchar(255) null,
    platform varchar(255) null,
    application varchar(255) null,
    user_name varchar(255) null,
    last_login datetime,
    account_status varchar(255),
    account_provisioned boolean
);