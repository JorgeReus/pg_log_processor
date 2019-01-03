--TIMESTAMP: 02/enero/2019 miércoles a las 17:54:39 - TIMESTAMP_HASH: 6062a2433fe728d67188dd98b5621104 - USER: reus - DATABASE: test
create table example(id Serial);

--TIMESTAMP: 02/enero/2019 miércoles a las 18:23:00 - TIMESTAMP_HASH: df0b0e388e1c5e4f1c13fab35cc6a0ff - USER: reus - DATABASE: test
insert into test2 values(1);

--TIMESTAMP: 02/enero/2019 miércoles a las 18:37:17 - TIMESTAMP_HASH: 89acb488b6efc1f9612d4987df0078df - USER: reus - DATABASE: test
drop table example;

--TIMESTAMP: 02/enero/2019 miércoles a las 18:38:04 - TIMESTAMP_HASH: 993c0ce5fdfeb9b41357764c1fb0caf8 - USER: reus - DATABASE: test
create table example(id serial);

--TIMESTAMP: 03/enero/2019 jueves a las 00:40:52 - TIMESTAMP_HASH: 448fd5498c497faf3d6e6203ed98c220 - USER: reus - DATABASE: test
insert into example values(1, 'holas');

--TIMESTAMP: 03/enero/2019 jueves a las 00:40:56 - TIMESTAMP_HASH: 8763781e1e53fb848317d996a707dce5 - USER: reus - DATABASE: test
insert into example values(1, 'adios');

--TIMESTAMP: 03/enero/2019 jueves a las 00:41:34 - TIMESTAMP_HASH: cf86d1ec8e6a06aa3668ca26cfc8515e - USER: reus - DATABASE: test
update example set name = 'test';

