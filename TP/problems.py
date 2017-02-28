"""
1. LRU Caching
"""

Python
/**
    * 本代码由九章算法编辑提供。版权所有，转发请注明出处。
    * - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
    * - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，Big Data 项目实战班，
    * - 更多详情请见官方网站：http:
        //www.jiuzhang.com /?source = code
    */


class LinkedNode:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


"""
2. Buy sell stock
"""

Monday, November 24, 2014
[LeetCode] Best Time to Buy and Sell Stock I, II, II
Best Time to Buy and Sell Stock I

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.


Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time(ie, you must sell the stock before you buy again).


Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
You may not engage in multiple transactions at the same time(ie, you must sell the stock before you buy again).


思路：Best Time to Buy and Sell Stock I

I限制了只能买卖一次。于是要尽可能在最低点买入最高点抛出。这里的一个隐含的限制是抛出的时间必须在买入的时间之后。所以找整个数组的最大最小值之差的方法未必有效，因为很可能最大值出现在最小值之前。但是可以利用类似思路，在扫描数组的同时来更新一个当前最小值minPrice。这样能保证当扫到i时，minPrices必然是i之前的最小值。当扫到i时：

如果prices[i] < minPrice，则更新minPrice = prices[i]。并且该天不应该卖出。
如果prices[i] >= minPrice，则该天可能是最好的卖出时间，计算prices[i] - minPrice，并与当前的单笔最大利润比较更新。


class Solution {
    public:
    int maxProfit(vector < int > &prices) {
        if(prices.empty()) return 0
        int ret = 0, minPrice = prices[0]
        for(int i=1
            i < prices.size()
            i + +) {
            if(prices[i] < minPrice)
            minPrice = prices[i]
            else
            ret = max(prices[i] - minPrice, ret)
        }
        return ret
    }
}


思路：Best Time to Buy and Sell Stock II

II并没有限制总的买卖次数，只限制了当天只能买或卖。所以可以采用greedy的方法，来获得所有可能的正利润。以如下序列说明：

2 1 3 4 5 4 2 8 7

只要prices[i] - prices[i - 1] > 0，我们就在第i - 1天买入，第i天抛出。这样可以包括所有可能赚取利润的区间。


class Solution {
    public:
    int maxProfit(vector < int > &prices) {
        int ret = 0
        for(int i=1
            i < prices.size()
            i + +) {
            ret += prices[i] > prices[i - 1] ? prices[i] - prices[i - 1]: 0
        }
        return ret
    }
}


思路：Best Time to Buy and Sell Stock III

III是这三题中最难的。允许两次买卖，但同一时间只允许持有一支股票。也就意味着这两次买卖在时间跨度上不能有重叠（当然第一次的卖出时间和第二次的买入时间可以是同一天）。既然不能有重叠可以将整个序列以任意坐标i为分割点，分割成两部分：

prices[0:n - 1] = > prices[0:i] + prices[i:n - 1]

对于这个特定分割来说，最大收益为两段的最大收益之和。每一段的最大收益当然可以用I的解法来做。而III的解一定是对所有0 <= i <= n - 1的分割的最大收益中取一个最大值。为了增加计算效率，考虑采用dp来做bookkeeping。目标是对每个坐标i：

1. 计算A[0:i]的收益最大值：用minPrice记录i左边的最低价格，用maxLeftProfit记录左侧最大收益
2. 计算A[i:n - 1]的收益最大值：用maxPrices记录i右边的最高价格，用maxRightProfit记录右侧最大收益。
3. 最后这两个收益之和便是以i为分割的最大收益。将序列从左向右扫一遍可以获取1，从右向左扫一遍可以获取2。相加后取最大值即为答案。


class Solution {
    public:
    int maxProfit(vector < int > &prices) {
        if(prices.empty()) return 0
        int n = prices.size()
        vector < int > leftProfit(n, 0)

        int maxLeftProfit = 0, minPrice = prices[0]
        for(int i=1
            i < n
            i + +) {
            if(prices[i] < minPrice)
            minPrice = prices[i]
            else
            maxLeftProfit = max(maxLeftProfit, prices[i] - minPrice)
            leftProfit[i] = maxLeftProfit
        }

        int ret = leftProfit[n - 1]
        int maxRightProfit = 0, maxPrice = prices[n - 1]
        for(int i=n - 2
            i >= 0
            i - -) {
            if(prices[i] > maxPrice)
            maxPrice = prices[i]
            else
            maxRightProfit = max(maxRightProfit, maxPrice - prices[i])
            ret = max(ret, maxRightProfit + leftProfit[i])
        }

        return ret
    }
}


<!-- I - - >


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        total = 0
        low, high = sys.maxint, 0
        for x in prices:
            if x - low > total:
                total = x - low
            if x < low:
                low = x
        return total
<!-- < II > -- >
public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0
        for (int i=0
             i < prices.length - 1
             i + +) {
            int diff = prices[i + 1] - prices[i]
            if (diff > 0) {
                profit += diff
            }
        }
        return profit
    }
}


/**
    * 本代码由九章算法编辑提供。版权所有，转发请注明出处。
    * - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
    * - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，Big Data 项目实战班，
    * - 更多详情请见官方网站：http:
        //www.jiuzhang.com /?source = code
    */

public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null | | prices.length <= 1) {
            return 0
        }

        int[] left = new int[prices.length]
        int[] right = new int[prices.length]

        // DP from left to right
        left[0] = 0
        int min = prices[0]
        for (int i=1
             i < prices.length
             i + +) {
            min = Math.min(prices[i], min)
            left[i] = Math.max(left[i - 1], prices[i] - min)
        }

        // DP from right to left
        right[prices.length - 1] = 0
        int max = prices[prices.length - 1]
        for (int i=prices.length - 2
             i >= 0
             i - -) {
            max = Math.max(prices[i], max)
            right[i] = Math.max(right[i + 1], max - prices[i])
        }

        int profit = 0
        for (int i=0
             i < prices.length
             i + +){
            profit = Math.max(left[i] + right[i], profit)
        }

        return profit
    }
}
