-- this file creates the identity.identity_account table

use dagger.identity;

create table if not exists identity.identity_account (
    -- default attributes
    identity_id varchar(255) not null references identity(identity_id),
    account_id varchar(255) not null references account(account_id),
    create_ts datetime not null
);

create stream if not exists identity_account_stream on table identity_account;

create table if not exists identity.identity_account_aud (
    -- audit attributes
    audit_insert_ts datetime not null default current_timestamp,
    audit_action varchar(10) not null,
    audit_is_update varchar(10) not null,
    -- default attributes
    identity_id varchar(255) not null,
    account_id varchar(255) not null,
    create_ts datetime not null
);