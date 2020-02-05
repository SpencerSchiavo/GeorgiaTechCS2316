# Spencer Schiavo
# 903125926
# sschiavo3

create database marta;
use marta;

create table routes (
   route_id int primary key auto_increment,
   route_name text
);

create table stops (
   stop_id int primary key auto_increment,
   stop_name text
);

create table vehicles (
   vehicle_id int primary key auto_increment
);

create table passenger_data (
   `index` int primary key auto_increment,
   `date` date,
   route_id int references routes(route_id),
   direction text,
   stop_id int references stops(stop_id),
   on_number int not null default 0,
   off_number int not null default 0,
   vehicle_id int references vehicles(vehicle_id)
);

