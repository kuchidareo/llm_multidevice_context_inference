taskset -c 0 python client_pytorch.py --cid=3 --num_clients=40 --dataset=wisdm_watch --partition_type=user & taskset -c 1 python client_pytorch.py --cid=13 --num_clients=40 --dataset=wisdm_watch --partition_type=user & taskset -c 2 python client_pytorch.py --cid=23 --num_clients=40 --dataset=wisdm_watch --partition_type=user & taskset -c 3 python client_pytorch.py --cid=33 --num_clients=40 --dataset=wisdm_watch --partition_type=user &