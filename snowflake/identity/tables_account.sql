-- this file creates the identity.account table

-- TODO: stream and sproc
-- TODO: action flags in the table

use dagger.identity;

create table if not exists identity.identity (
    -- default attributes
    account_id varchar(255) not null primary key,
    create_ts datetime not null,
    update_ts datetime not null,
    -- account attributes

);