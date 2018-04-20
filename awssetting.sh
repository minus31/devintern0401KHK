#! bin/bash

# move .ssh

cd ~/.ssh


aws ec2 run-instances --image-id ami-2945eb47 --count 1 --instance-type t2.micro --key-name minus31 --security-group-ids sg-12d11678 --subnet-id subnet-e2c527ae


instance_id=$(aws ec2 run-instances --image-id ami-2945eb47 --count 1 --instance-type t2.micro --key-name minus31 --security-group-ids sg-12d11678 --subnet-id subnet-e2c527ae)

instance_state=$(aws ec2 instance-running --instance-ids $instance_id \
        --query 'Reservations[].Instances[].State.Name')
while [ "$instance_state" != "running" ]
do
    sleep 1
    instance_state=$(aws ec2 describe-instances --instance-ids $instance_id \
        --query 'Reservations[].Instances[].State.Name')
done


cd /tmp

curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh

bash Anaconda3-5.0.1-Linux-x86_64.sh

echo "enter"

echo 'yes'




