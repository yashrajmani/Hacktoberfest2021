-- this query will basically tells us about any new info added about which need information if else can be used for required conditions.
-- imp note "From delimiter $$ run in command line client as it is a trigger till delimiter ;",after wriitng the above query query of insertion of new row will update trigger table
--  and add the msg u can also add column name of table on which trigger is applied.
   
 -- for workbench
 create table trigger_test(
message varchar(20)
);
 -- command line script start
delimiter $$
create 
trigger my_trigger before insert 
on <TABLE NAME>
for each  row begin 
insert into trigger_test values("added employee"); 
end $$
delimiter ;
-- command line script end
