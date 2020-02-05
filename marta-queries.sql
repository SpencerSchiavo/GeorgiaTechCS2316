# Spencer Schiavo
# 903125926
# sschiavo3

select stop_name, sum(on_number) as num_on_count from stops join passenger_data using (stop_id) group by stop_id order by num_on_count desc;

select vehicle_id, count(vehicle_id) as num_stops from vehicles join passenger_data using (vehicle_id) group by vehicle_id order by num_stops desc;



