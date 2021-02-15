drop table gift_idea;
drop table person;

create table person (
  person_id SERIAL PRIMARY KEY,
  description text default '',
  name varchar(255) NOT NULL
);

create table gift_idea (
  gift_idea_id SERIAL PRIMARY KEY,
  person_id int references person,
  product varchar(255) NOT NULL,
  external_link varchar(255)
);

insert into person (name) values ('Yang He');
insert into person (name) values ('Daniel Kluver');

-- I know a weird number of people named laura
insert into person (name) values ('Laura');
insert into person (name) values ('Laura (house)');
insert into person (name) values ('Laura (family)');
