1: 1.py 1.data
	python3 ./1.py < ./1.data

2: 2.c 2.data
	gcc 2.c -o 2
	./2 < ./2.data

3: 3.cpp 3.data
	g++ -std=c++1z 3.cpp -o 3
	./3 < ./3.data

3r: 3r.cpp 3.data
	g++ -std=c++1z 3r.cpp -o 3r -Wall
	./3r < ./3.data

4: 4.c 4.data
	gcc 4.c -o 4
	./4 < ./4.data

5: 5.c 5.data
	gcc 5.c -o 5 -Wall
	./5 < ./5.data

6: 6.c 6.data
	gcc 6.c -o 6
	./6 < ./6.data

6cpp: 6.cpp 6.data
	g++ -std=c++1z 6.cpp -o 6
	./6 < ./6.data

6big: 6big.cpp 6.data
	g++ -std=c++1z 6big.cpp -o 6
	./6 < ./6.data
