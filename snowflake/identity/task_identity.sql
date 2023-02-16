-- this file creates the identity.identity task

use dagger.identity;

create or replace task identity
    schedule = '60 minutes'
when system$stream_has_data('identity_stream')
as
insert into identity_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from identity_stream as s;

-- alter task identity resume;
-- alter task identity suspend;