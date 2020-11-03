top -b -d 1 | grep --line-buffered -e ^top -e htop$ > test.t
top -b -d 1 | grep --line-buffered -e ^top | cut -f 1 -d ,
top -b -d 1 | grep --line-buffered -e ^top -e htop$ | tee test.t
top -b -d 1 | grep --line-buffered -A2 -e PID -e ^top | grep -v -e Tasks: -e ^%Cpu -e KiB
top -b -d 1 | grep --line-buffered -A3 -e PID -e ^top | egrep -v -e '^[A-Z|%]'
