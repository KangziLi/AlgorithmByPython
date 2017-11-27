#Algorithm notes

Python Solutions to problems on [LintCode](http://www.lintcode.com) 

源码地址为：[KangziLi/**AlgorithmByPython**](https://github.com/KangziLi/AlgorithmByPython)

##1. A + B 问题 · A + B Problem

> 给出两个整数a和b, 求他们的和, 但不能使用 `+` 等数学运算符。
>
> Write a function that add two numbers A and B. You should not use `+` or any arithmetic operators.

此题参考了[jaychsu](https://github.com/jaychsu/algorithm/blob/master/shared/calculator_in_bit.py)的解法，他给出的思路如下：

Python 有个问题是 int 超过 0x7FFFFFFF 之后会自动转成 long (2 还会标记为 long, 3 直接当 int 处理了)，所以在 `(a & b) << 1` 时会就这么不断的往前进位，跳不出循环。

对应的思路是每次越界(超过 0x7FFFFFFF * 2 + 1, 所有 int 个数)就 and 一次，最后再判断有没有最高位，有则为负数。

```python
class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        INT_RANGE = 0xFFFFFFFF
        while b:
            a,b = a ^ b, (a & b)<<1
            a &= INT_RANGE
        if a >>31 == 0:
            return a
        else:
            return a ^ ~INT_RANGE
```

## 2. 尾部的零 · Trailing Zeros

> 设计一个算法，计算出n阶乘中尾部零的个数
>
> Write an algorithm which computes the number of trailing zeros in n factorial.
>

能产生尾数0的素数因子为 2 * 5，像5,10,15,20等数只有一个5的因子，因此count++就可以了，但碰到25,50,75等数，包含了2个5的因子，因此count应该加2，碰到125等含3个5的因子，count应该加3。因此，可以采用下面的算法。例如105的阶乘，1~105有21个能被5整除的数，105/5=21，1~21中有4个能被5整除的数，21/5=4，1~4中没有，count=21+4+0=25.即从1~105中挑出5=5*1,10=5*2，15=5*3,20=5*4,25=5*5,30=5*6...100=5*20,105=5*21这21个数，在从这21个数中挑出能继续被5整除的25,50,75,100这四个数。0的个数=5的倍数+5^2的倍数+5^3的倍数+5^4的倍数+5^5的倍数+...

```python
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0
        while n:
            n /= 5
            count += n
        return count
```

## 3. 统计数字 · digit counts

> 计算数字k在0到n中的出现的次数，k可能是0~9的一个值
>
> Count the number of *k*'s between *0* and *n*. *k* can be *0* - *9*.

digitCounts1方法，当n非常大时，就需要很长的运行时间，而且容易产生MemoryError

digitCounts2方法，思路来源于《编程之美》，假设一个5位数N=abcde，我们现在来考虑百位上出现2的次数，即，从0到abcde的数中， 有多少个数的百位上是2。分析完它，就可以用同样的方法去计算个位，十位，千位， 万位等各个位上出现2的次数。

当百位c为0时，比如说12013，0到12013中哪些数的百位会出现2？我们从小的数起， 200~299, 1200~1299, 2200~2299, … , 11200~11299, 也就是固定低3位为200~299，然后高位依次从0到11，共12个。再往下12200~12299 已经大于12013，因此不再往下。所以，当百位为0时，百位出现2的次数只由更高位决定， 等于更高位数字(12)x当前位数(100)=1200个。当百位c为1时，比如说12113。分析同上，并且和上面的情况一模一样。 最大也只能到11200~11299，所以百位出现2的次数也是1200个。上面两步综合起来，可以得到以下结论：

- 当某一位的数字小于2时，那么该位出现2的次数为：更高位数字x当前位数

当百位c为2时，比如说12213。那么，我们还是有200~299, 1200~1299, 2200~2299, … , 11200~11299这1200个数，他们的百位为2。但同时，还有一部分12200~12213， 共14个(低位数字+1)。所以，当百位数字为2时， 百位出现2的次数既受高位影响也受低位影响，结论如下：

- 当某一位的数字等于2时，那么该位出现2的次数为：更高位数字x当前位数+低位数字+1

当百位c大于2时，比如说12313，那么固定低3位为200~299，高位依次可以从0到12， 这一次就把12200~12299也包含了，同时也没低位什么事情。因此出现2的次数是： (更高位数字+1)x当前位数。结论如下：

- 当某一位的数字大于2时，那么该位出现2的次数为：(更高位数字+1)x当前位数

```python
class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts1(self, k, n):
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        for i in range(n + 1):
            num = i
            while True:
                if num % 10 == k:
                    count += 1
                num /= 10
                if num == 0:
                    break
        return count
    def digitCounts2(self, k, n):
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        base = 1
        while n / base > 0:
            curbit = (n / base) % 10
            lowbit = n - (n / base) * base
            highbit = n /(base * 10)
            if curbit < k:
                count += highbit * base
            elif curbit == k:
                count += highbit * base + lowbit + 1
            else:
                count += (highbit +1) * base
            base *= 10
        if k == 0:
            if n == 0:
                count = 1
            else:
                count -= base / 10 
        return count
```

## 4. 丑数 II · Ugly Number II

> 设计一个算法，找出只含素因子`2`，`3`，`5` 的第 *n* 小的数。
>
> 符合条件的数如：`1, 2, 3, 4, 5, 6, 8, 9, 10, 12...`
>
> Ugly number is a number that only have factors `2`, `3` and `5`.
>
> Design an algorithm to find the *n*th ugly number. The first 10 ugly numbers are `1, 2, 3, 4, 5, 6, 8, 9, 10, 12...`

丑陋数序列可以拆分为下面3个子列表：

(1) **1x2**,  2x2, **2x2**, 3x2, **3x2**, **4x2**, 5x2...

(2) 1x3,  **1x3**, 2x3, 2x3, **2x3**, 3x3, **3x3**...

(3) 1x5,  1x5, 1x5, **1x5,** 2x5, 2x5, 2x5...

仔细观察上述三个列表，我们可以发现每个子列表都是一个丑陋数分别乘以2,3,5，而要求的丑陋数就是从已经生成的序列中取出来的，我们每次都从三个列表中取出当前最小的那个加入序列

```python
class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        list = [1]
        i2, i3, i5=0,0,0
        while len(list)<n:
            m2 = list[i2]*2
            m3 = list[i3]*3
            m5 = list[i5]*5
            m =min(m2,m3,m5)
            if m == m2:
                i2 += 1
            if m==m3:
                i3 += 1
            if m==m5:
                i5 +=1
            list.append(m)
        return list[-1]
```

## 