-- this file creates the access.platform table

use dagger.access;

create table if not exists access.platform (
    -- default attributes
    platform_id varchar(255) not null primary key,
    create_ts datetime not null default current_timestamp,
    -- platform attributes
    platform_name varchar(255) null,
    platform_description varchar(255) null,
    owner_identity_ids variant null,
    status boolean null
);

create stream if not exists platform_stream on table platform;

create table if not exists access.platform_aud (
    -- audit attributes
    audit_insert_ts datetime not null default current_timestamp,
    audit_action varchar(10) not null,
    audit_is_update varchar(10) not null,
    -- default attributes
    platform_id varchar(255) not null,
    create_ts datetime not null default current_timestamp,
    -- platform attributes
    platform_name varchar(255) null,
    platform_description varchar(255) null,
    owner_identity_ids variant null,
    status boolean null
);