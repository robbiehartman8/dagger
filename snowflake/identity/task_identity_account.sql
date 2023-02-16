-- this file creates the identity.identity_account task

use dagger.identity;

create or replace task identity_account
    schedule = '60 minutes'
when system$stream_has_data('identity_account_stream')
as
insert into identity_account_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from identity_account_stream as s;

-- alter task identity_account resume;
-- alter task identity_account suspend;