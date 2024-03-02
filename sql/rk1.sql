select * from items;
create table design(
  did int not null,
  dtime varchar(50),
  im blob,
  primary key(did)
);