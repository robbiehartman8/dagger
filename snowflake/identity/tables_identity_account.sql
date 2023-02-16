-- this file creates the identity.identity_account table

-- TODO: stream and sproc

use dagger.identity;

create table if not exists identity.identity_account (
    -- default attributes
    identity_id varchar(255) not null foreign key,
    account_id varchar(255) not null foreign key,
    create_ts datetime not null
);