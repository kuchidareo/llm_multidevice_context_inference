taskset -c 0 python client_pytorch.py --cid=6 --num_clients=35 --dataset=wisdm_watch --partition_type=user --user_selection 1 2 4 5 6 7 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 37 38 & 
taskset -c 1 python client_pytorch.py --cid=16 --num_clients=35 --dataset=wisdm_watch --partition_type=user --user_selection 1 2 4 5 6 7 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 37 38 &
taskset -c 2 python client_pytorch.py --cid=26 --num_clients=35 --dataset=wisdm_watch --partition_type=user --user_selection 1 2 4 5 6 7 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 37 38 &