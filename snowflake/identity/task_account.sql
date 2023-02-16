-- this file creates the identity.account task

use dagger.identity;

create or replace task account
    schedule = '60 minutes'
when system$stream_has_data('account_stream')
as
insert into account_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from account_stream as s;

-- alter task account resume;
-- alter task account suspend;