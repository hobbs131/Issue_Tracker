
insert into person (name) values ('Liam'); --3
insert into person (name) values ('Olivia'); --4
insert into person (name) values ('Noah'); --5
insert into person (name) values ('Emma'); --6

insert into skill (person_id, skill) values (5, 'Advising');
insert into skill (person_id, skill) values (3, 'Coaching');
insert into skill (person_id, skill) values (4 'Coaching');
insert into skill (person_id, skill) values (5 'Coaching');
insert into skill (person_id, skill) values (6 'Coaching');
insert into skill (person_id, skill) values (4, 'Delegating');
insert into skill (person_id, skill) values (5, 'Delegating');
insert into skill (person_id, skill) values (6, 'Delegating');
insert into skill (person_id, skill) values (4, 'Diplomacy');
insert into skill (person_id, skill) values (6, 'Diplomacy');
insert into skill (person_id, skill) values (3, 'Interviewing');
insert into skill (person_id, skill) values (6, 'Interviewing');
insert into skill (person_id, skill) values (3, 'Motivation');
insert into skill (person_id, skill) values (5, 'Motivation');
insert into skill (person_id, skill) values (6, 'Motivation');


-- joins let us ask "what skills does Liam have" or "who can delegate?'
