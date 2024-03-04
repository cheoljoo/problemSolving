
# 180. Minimum Time to Complete Trips (#2187) - medium / python / 30M / 2023.03.08 / binary search
- medium
- problem :
  - You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.
  - Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.
  - You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
  - Constraints : 1 <= time.length <= 10^5 / 1 <= time[i], totalTrips <= 10^7
  - ```
    Input: time = [1,2,3], totalTrips = 5
    Output: 3
    Explanation:
    - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
      The total number of trips completed is 1 + 0 + 0 = 1.
    - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
      The total number of trips completed is 2 + 1 + 0 = 3.
    - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
      The total number of trips completed is 3 + 1 + 1 = 5.
    So the minimum time needed for all buses to complete at least 5 trips is 3.
    ```
- https://leetcode.com/problems/minimum-time-to-complete-trips/
- [minimumTime.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minimumTime.py) : passed
  - Runtime 4008 ms / Beats 18%
- algorithm : binary search
- complexity : O(NlogN)
- TODO : learn more 

# 181. Koko Eating Bananas (#875) - medium / python / 20M / 2023.03.08 / binary search
- medium
- problem :
  - Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
  - Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
  - Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
  - Return the minimum integer k such that she can eat all the bananas within h hours.
  - Constraints : 1 <= piles.length <= 10^4 / piles.length <= h <= 10^9 / 1 <= piles[i] <= 10^9
  - ```
    IInput: piles = [3,6,7,11], h = 8
    Output: 4
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23
    ```
- https://leetcode.com/problems/koko-eating-bananas
- [minEatingSpeed.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minEatingSpeed.py) : passed
  - Runtime 464 ms / Beats 77.33% / Memory 15.5 MB / Beats 16.17%
- algorithm : binary search
- complexity : O(NlogN)

# 182. Convert Sorted List to Binary Search Tree (#109) - medium / python / 20M / 2023.03.11 
- medium
- problem :
  - Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
- https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
- [sortedListToBST.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sortedListToBST.py) : passed
  - Runtime 121 ms / Beats  75.46% / Memory 20.3 MB / Beats 26.76%
- complexity : O(N)

# 183. Sum Root to Leaf Numbers (#129) - medium / python / 20M / 2023.03.14 / tree traverse
- medium
- problem :
  - You are given the root of a binary tree containing digits from 0 to 9 only.
  - Each root-to-leaf path in the tree represents a number.
    - For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
  - Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
  - A leaf node is a node with no children.
  - Constraints : The number of nodes in the tree is in the range [1, 1000]. / 0 <= Node.val <= 9 / The depth of the tree will not exceed 10.
  - ```
    Input: root = [4,9,0,5,1]
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
    ```
- https://leetcode.com/problems/sum-root-to-leaf-numbers/
- [sumNumbers.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/sumNumbers.py) : passed
  - Runtime 32 ms  Beats 70.48% / Memory 13.8 MB  Beats 95.89%
- algorithm : tree traverse
- complexity : O(N)


# 184. Implement Trie (Prefix Tree) (#208) - medium / python / 20M / 2023.03.17
- medium
- problem :
  - A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
  - Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
  - ```
    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
    ```
- https://leetcode.com/problems/implement-trie-prefix-tree/
- [Trie.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/Trie.py) : passed
  - Runtime 799 ms  Beats 5% / Memory 20.8 MB Beats 97.63%


# 185. Design Browser History (#1472) - medium / python / 20M / 2023.03.18
- medium
- problem :
  - You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
  - Implement the BrowserHistory class:
    - BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    - void visit(string url) Visits url from the current page. It clears up all the forward history.
    - string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    - string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
  - ```
    Input:
    ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    Output:
    [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

    Explanation:
    BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
    browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
    browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
    browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
    browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
    browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
    browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
    browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
    ```
- https://leetcode.com/problems/design-browser-history/
- [BrowserHistory.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minCoBrowserHistoryst.py) : passed
  - Runtime 217 ms  Beats 86.77% /  Memory 16.7 MB  Beats 37.23%



# 186. template (#) - medium / python / 20M / 2023.03.14 / (ing)
- medium
- problem :
  - 
  - Constraints : 
  - ```

    ```
- 
- [minCost.py](https://github.com/cheoljoo/problemSolving/blob/master/leetcode/minCost.py) :
  - 
- algorithm :
- complexity :


1.    Longest String Chain
https://leetcode.com/problems/longest-string-chain/
- algorithm :
  - how to find fast that one character is different
    - ?bb  b?b bb? 
    - nei{h_t , [hot,...]} 와 같이 가지면 된다. 3개의 문자로 될수 있는 것을 미리 table에 조사를 해두는 것이다. 
