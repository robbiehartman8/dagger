-- this file creates the access.access_catalog table

use dagger.access;

create table if not exists access.access_catalog (
    -- default attributes
    access_catalog_id varchar(255) not null primary key,
    create_ts datetime not null default current_timestamp,
    -- access_catalog attributes
    platform_id varchar(255) null,
    access_name varchar(255) null,
    access_display_name varchar(255) null,
    access_description varchar(3500) null,
    owner_identity_ids variant null,
    approver_identity_ids variant null,
    requestable boolean null,
    priviledged boolean null,
    sox boolean null,
    pci boolean null,
    pii boolean null,
    secondary_account_required boolean null,
    jit_access boolean null,
    status boolean
);

create stream if not exists access_catalog_stream on table access_catalog;

create table if not exists access.access_catalog_aud (
    -- audit attributes
    audit_insert_ts datetime not null default current_timestamp,
    audit_action varchar(10) not null,
    audit_is_update varchar(10) not null,
    -- default attributes
    access_catalog_id varchar(255) not null,
    create_ts datetime not null default current_timestamp,
    -- access_catalog attributes
    platform_id varchar(255) null,
    access_name varchar(255) null,
    access_display_name varchar(255) null,
    access_description varchar(3500) null,
    owner_identity_ids variant null,
    approver_identity_ids variant null,
    requestable boolean null,
    priviledged boolean null,
    sox boolean null,
    pci boolean null,
    pii boolean null,
    secondary_account_required boolean null,
    jit_access boolean null,
    status boolean
);