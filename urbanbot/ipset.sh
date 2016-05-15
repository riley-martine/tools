ip=$((RANDOM%=255))"."$((RANDOM%=255))"."$((RANDOM%=255))"."$((RANDOM%=255))"/"$((RANDOM%=32))

echo $ip
sudo ifconfig wlp1s0 $ip netmask 255.0.0.0
