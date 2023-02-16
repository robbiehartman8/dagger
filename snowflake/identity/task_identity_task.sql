-- this file creates the identity.identity_task task

use dagger.identity;

create or replace task identity_task 
    schedule = '5 minute'
when system$stream_has_data('identity_stream')
as
insert into identity_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from identity_stream as s;

alter task identity_task resume;
-- alter task identity_task suspend;