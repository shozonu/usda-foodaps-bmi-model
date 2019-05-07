update t1 set breakfast = 0 where breakfast < 0;
update t1 set lunch = 0 where lunch < 0;
update t1 set dinner_supper = 0 where dinner_supper < 0;
update t1 set snack_drink = 0 where snack_drink < 0;
update t1 set placedist_s = null where placedist_s < 0;
select * from t1;
