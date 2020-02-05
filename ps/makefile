03:
	python3 no0003.py < no0003.data

03-python2:
	python2 no0003-1.py2 < no0003.data

3cpp: 3.cpp
	g++ -std=c++11 3.cpp -o 3cpp

3r: 3r.cpp
	g++ -std=c++11 3r.cpp -o 3r

4: 4.cpp
	g++ -std=c++11 4.cpp -o 4

4r: 4r.cpp
	g++ -std=c++11 4r.cpp -o 4r

4rd: 4rd.cpp
	g++ -std=c++11 4rd.cpp -o 4rd

4r_lsh: 4r_lsh.cpp
	g++ -std=c++11 4r_lsh.cpp -o 4r_lsh

5: 5.cpp
	g++ -std=c++11 5.cpp -o 5
	./5 < 5.data2

5r: 5r.cpp
	g++ -std=c++11 5r.cpp -o 5r
	@echo ""
	@echo ""
	@echo "answer:3"
	./5r < 5.data
	@echo ""
	@echo ""
	@echo "answer:6"
	./5r < 5.data2
	@echo ""
	@echo ""
	@echo "answer:37"
	./5r < 5.data3

5r2: 5r2.cpp
	g++ -std=c++11 5r2.cpp -o 5r2
	@echo ""
	@echo ""
	@echo "answer:3"
	./5r2  < 5.data
	@echo ""
	@echo ""
	@echo "answer:6"
	./5r2  < 5.data2
	@echo ""
	@echo ""
	@echo "answer:37"
	./5r2  < 5.data3

6r: 6r.cpp 6.data
	g++ -std=c++11 6r.cpp -o 6r
	@echo ""
	@echo ""
	@echo "answer:1"
	./6r  < 6.data

7: 7.cpp 7.data
	g++ -std=c++11 7.cpp -o 7
	@echo ""
	@echo ""
	@echo "answer:1"
	./7  < 7.data

7r: 7r.cpp 7.data
	g++ -std=c++11 7r.cpp -o 7r
	@echo ""
	@echo ""
	@echo "answer:1"
	./7r  < 7.data

8: 8.cpp 8.data
	g++ -std=c++11 8.cpp -o 8
	@echo ""
	@echo ""
	@echo "answer:1"
	./8  < 8.data

8moreC: 8moreC.cpp 8.data
	g++ -std=c++11 8moreC.cpp -o 8
	@echo ""
	@echo ""
	@echo "answer:1"
	./8  < 8.data

9: 9.cpp 9.data 9r1.cpp  9.data3 9r2.cpp
	g++ -std=c++11 9.cpp -o 9
	g++ -std=c++11 9r1.cpp -o 9r1
	g++ -std=c++11 9r2.cpp -o 9r2
	./9r2  < 9.data3

10: 10.cpp 10.data  10r.cpp 10.data2 10ans.cpp
	g++ -std=c++11 10.cpp -o 10
	g++ -std=c++11 10r.cpp -o 10r
	g++ -std=c++11 10ans.cpp -o 10ans
	./10ans  < 10.data3

11: 11.cpp 11.data
	g++ -std=c++11 11.cpp -o 11
	./11 < 11.data

12: 12.cpp 12.data
	g++ -std=c++11 12.cpp -o 12
	./12 < 12.data

12r: 12r.cpp 12.data 12.data2
	g++ -std=c++11 12r.cpp -o 12r       # ok : recursive DFS 
	./12r < 12.data     # 300  2*2+5*2
	./12r < 12.data2    # 80   2*2
	./12r < 12.data3    # 3813498

12r1: 12r1.cpp 12.data      
	g++ -std=c++11 12r1.cpp -o 12r1     # timeout :  stack BFS
	./12r1 < 12.data     # 300  2*2+5*2

12r2: 12r2.cpp 12.data3
	g++ -std=c++11 12r2.cpp -o 12r2     # ok : stack DFS
	./12r2 < 12.data    # 3813498

13: 13.cpp 13.data1 13.data2
	g++ -std=c++11 13.cpp -o 13     
	./13 < 13.data2    # 3813498

# 14 : https://www.acmicpc.net/problem/17610
14: 14.cpp 14.data1
	g++ -std=c++11 14.cpp -o 14     
	./14 < 14.data1    # 2
    
# 15 : https://www.acmicpc.net/problem/2985
15: 15.cpp 15.data1
	g++ -std=c++11 15.cpp -o 15     
	./15 < 15.data1   

# 16 : https://www.acmicpc.net/source/17291850
16: 16.c 16.data1
	gcc 16.c -o 16     
	./16 < 16.data1   

# 17 : https://www.acmicpc.net/problem/15997
17: 17.cpp 17.data1
	g++ -std=c++11 17.cpp -o 17     
	./17 < 17.data1   

temp: temp.cpp
	g++ -std=c++11 temp.cpp -o temp ;  ./temp
