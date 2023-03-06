-- this file creates the access.access_catalog task

use dagger.access;

create or replace task access_catalog
    schedule = '60 minutes'
when system$stream_has_data('access_catalog_stream')
as
insert into access_catalog_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from access_catalog_stream as s;

-- alter task access_catalog resume;
-- alter task access_catalog suspend;