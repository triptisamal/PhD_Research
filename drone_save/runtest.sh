#!/bin/sh


echo "Choose what test scenario (1/0)"
echo "0. Effect of increase in number of nodes"
echo "1. Effect of increase in eccentricity"
echo "2. Check delay related"
read testnumber

if [ "$testnumber" -ne "2" ]
then
	echo "Choose what algorithm (1/0)"
	echo "0. Flooding"
	echo "1. Petal Routing"
	read algorithm
fi

#echo "Choose what topology (1/0)"
##echo "0. Lattice"
#echo "1. Guassian Perturbed Lattice"
#read topology

#echo "Choose what zone (1/0)"
#echo "0. Single"
#echo "1. Multi"
#read zone
#echo "Choose what mobility model (2/1/0)"
#echo "0. No mobility"
#echo "1. All nodes moving with same velocity"
#echo "2. Some nodes moving with same velocity"
#read mobility

if [ "$testnumber" -eq "2" ]
then
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 64 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 64 0.4 1 1 1 $c 0
#		c=$(( c+1 ))
#	done
#
#	#move files
#	mv petal_source.txt model1/64
#	mv petal_dest.txt model1/64
#	mv flood_source.txt model1/64
#	mv flood_dest.txt model1/64
#	mv *500* model1/64
#	mv *.c model1/64
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 125 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 125 0.4 1 1 1 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model1/125
#	mv petal_dest.txt model1/125
#	mv flood_source.txt model1/125
#	mv flood_dest.txt model1/125
#	mv *500* model1/125
#	mv *.c model1/125
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 216 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 216 0.4 1 1 1 $c 0
#		c=$(( c+1 ))
#	done
#	#move files
#	mv petal_source.txt model1/216
#	mv petal_dest.txt model1/216
#	mv flood_source.txt model1/216
#	mv flood_dest.txt model1/216
#	mv *500* model1/216
#	mv *.c model1/216
#	#mobility 2
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 64 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 64 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/64
#	mv petal_dest.txt model2/64
#	mv flood_source.txt model2/64
#	mv flood_dest.txt model2/64
#	mv *500* model2/64
#	mv *.c model2/64
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 125 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 125 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/125
#	mv petal_dest.txt model2/125
#	mv flood_source.txt model2/125
#	mv flood_dest.txt model2/125
#	mv *500* model2/125
#	mv *.c model2/125
#	c=1
#	while [ "$c" -le "500" ]
#	do
#	#	echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 216 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 216 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/216
#	mv petal_dest.txt model2/216
#	mv flood_source.txt model2/216
#	mv flood_dest.txt model2/216
#	mv *500* model2/216
#	mv *.c model2/216
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		#multi-zone
		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
		python3 simulator_drone.py 1 343 0.4 1 1 2 $c 1
		python3 simulator_drone.py 0 343 0.4 1 1 2 $c 0
		c=$(( c+1 ))
	done
		#move files
	mv petal_source.txt model2/343
	mv petal_dest.txt model2/343
	mv flood_source.txt model2/343
	mv flood_dest.txt model2/343
	mv *500* model2/343
	mv *.c model2/343
	#mobility1
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		#multi-zone
		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 1
		python3 simulator_drone.py 0 343 0.4 1 1 1 $c 0
		c=$(( c+1 ))
	done
	#move files
	mv petal_source.txt model1/343
	mv petal_dest.txt model1/343
	mv flood_source.txt model1/343
	mv flood_dest.txt model1/343
	mv *500* model1/343
	mv *.c model1/343
fi



if [ "$testnumber" -eq "0" ]
then
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 64 0.9 $topology 0 $c 
	#	python3 simulator_drone.py $algorithm 64 0.4 $topology 1 
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.9 $topology 0 $c
	#	python3 simulator_drone.py $algorithm 125 0.4 $topology 1 
		c=$(( c+1 ))
	done
       c=1
       while [ "$c" -le "500" ]
       do
       	echo "RUN $c"
       	python3 simulator_drone.py $algorithm 216 0.9 $topology 0 $c 
       #	python3 simulator_drone.py $algorithm 216 0.4 $topology 1
       	c=$(( c+1 ))
       done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 343 0.9 $topology 0 $c
	#	python3 simulator_drone.py $algorithm 343 0.4 $topology 1
		c=$(( c+1 ))
	done
fi


if [ "$testnumber" -eq "1" ]
then
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		python3 simulator_drone.py $algorithm 125 0.4 $topology $zone 
#		c=$(( c+1 ))
#	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.5 $topology 0
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.6 $topology 0
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.7 $topology 0 
		c=$(( c+1 ))
	done
fi
