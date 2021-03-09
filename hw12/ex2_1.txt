select concat ('we have  ', count(*) , case when sex ='m' then ' boys ' else ' girls ' end) from users group by sex;
      concat
-------------------
 we have  3 boys
 we have  3 girls

py7=# select concat('This is   ', name, case when sex = 'm' then ' he has email ' else ' she has email ' end, email) from users;
                     concat
------------------------------------------------
 This is   Vasya he has email mmm@mail.com
 This is   Alex he has email mmm@gmail.com
 This is   Alexey he has email mmm@gmail.com
 This is   Helen she has email hell@gmail.com
 This is   Jenny she has email eachup@gmail.com
 This is   Lora she has email tpicks@gmail.com
(6 rows)