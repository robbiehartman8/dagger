-- this file creates the birthright.birthright_rule task

use dagger.birthright;

create or replace task birthright_rule
    schedule = '60 minutes'
when system$stream_has_data('birthright_rule_stream')
as
insert into birthright_rule_aud
select current_timestamp, METADATA$ACTION, METADATA$ISUPDATE, s.* exclude (METADATA$ACTION, METADATA$ISUPDATE, METADATA$ROW_ID)
from birthright_rule_stream as s;

-- alter task birthright_rule resume;
-- alter task birthright_rule suspend;