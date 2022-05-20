# https://codeup.kr/problem.php?id=2128&rid=0
# 2128 : 집합은 a, b를 싫어해
1: 1.py 1.data
	#python3 -m memory_profiler ./1.py --debug < ./1.data
	echo "10000000000000000000000000 100 1" | python3 1-lowMem3.py

2: 2.py 2.data
	python3 ./2.py --debug < ./2.data

3: 3.py 3.data
	python3 ./3.py --debug < ./3.data

# 1.6. 수열과 인연
4: 4.py 4.data
	#python3 ./4.py --debug < ./4.data
	python3 ./4.py < ./4.data
	python3 ./4-2.py < ./4.data

5: 5.py 5.data
	python3 ./5.py --debug < ./5.data
	#python3 ./5.py < ./5.data

6: 6.py
	echo "55-50+40" | python3 ./6.py --debug

7: 7.py
	echo "18115211" | python3 ./7.py --debug

marathon: marathon.py marathon.data
	cat  marathon.data | python3 ./marathon.py

coaltar : coalTar.py
	python3 ./coalTar.py

histgram: histogram2.py histogram.data
	cat  histogram.data | python3 ./histogram2.py

hiking: hiking_Dijkstra2.py
	python3 ./hiking_Dijkstra2.py

main_word_searching: main_word_searching.py
	python3 main_word_searching.py

decoding: decoding.py
	python3 decoding.py

plant_trees: plant_trees.py
	python3 plant_trees.py

fisher: fisher.py fisher.data
	python3 fisher.py  < fisher.data
