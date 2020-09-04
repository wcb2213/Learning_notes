#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


class Solution:
    def InversePairs(self, data):
        # write code here
        n = len(data)
        p = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if data[i] > data[j]:
                    p += 1
        return (p % 1000000007)

if __name__ == '__main__':
    a = Solution()
    l = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    print(a.InversePairs(l))