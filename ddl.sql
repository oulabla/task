-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
drop table if exists department;
create table department
(
    id   BIGINT NOT NULL,
    name VARCHAR(30),
    PRIMARY KEY (ID)
);

insert into department
values (1, 'rechtech'),
       (2, 'iot'),
       (3, 'new idea');


-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
drop table if exists user;
create table user
(
    id    BIGINT NOT NULL,
    name  VARCHAR(30),
    grade VARCHAR(30),
    PRIMARY KEY (ID)
);

insert into user
values (1, 'Mike', 'A'),
       (2, 'Helen', 'A'),
       (3, 'John', 'B'),
       (4, 'Rick', 'C'),
       (5, 'Rooney', 'D');

-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
drop table if exists salary;
create table salary
(
    user_id BIGINT        NOT NULL,
    salary  NUMERIC(6, 2) NOT NULL
);
insert into salary
values (1, 100),
       (2, 110),
       (3, 90),
       (4, 70),
       (5, 50);

-------------------------------------------------------
-------------------------------------------------------
-------------------------------------------------------
drop table if exists mtm;
create table mtm
(
    department_id BIGINT NOT NULL,
    user_id       BIGINT NOT NULL
);

insert into mtm
values (1, 1),
       (1, 2),
       (2, 2),
       (1, 3),
       (1, 4),
       (2, 5);
