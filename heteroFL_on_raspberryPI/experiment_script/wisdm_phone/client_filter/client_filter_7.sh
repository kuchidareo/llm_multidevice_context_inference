taskset -c 0 python client_pytorch.py --cid=6 --num_clients=22 --dataset=wisdm_phone --partition_type=user --user_selection 0 3 4 6 8 9 10 11 14 16 17 19 20 23 24 25 28 29 31 32 33 37 &
taskset -c 1 python client_pytorch.py --cid=16 --num_clients=22 --dataset=wisdm_phone --partition_type=user --user_selection 0 3 4 6 8 9 10 11 14 16 17 19 20 23 24 25 28 29 31 32 33 37 &