-- this file creates the access.platform task

use dagger.access;

create or replace task platform
    schedule = '60 minutes'
when system$stream_has_data('platform_stream')
as
insert into platform_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from platform_stream as s;

-- alter task platform resume;
-- alter task platform suspend;