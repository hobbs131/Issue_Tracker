drop table issues;

create table issues (
  id SERIAL PRIMARY KEY,
  issue varchar(255),
  priority varchar(255),
  opened_on varchar(255),
  opened_by varchar(255),
  assignee varchar(255),
  closed_on varchar(255),
  closed_by varchar(255),
  status varchar(255),
  deletedAt Date
);

