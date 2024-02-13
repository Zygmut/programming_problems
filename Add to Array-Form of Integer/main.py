class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k_list: List[int] = [int(x) for x in str(k)]
        iter_a, iter_b = len(num) - 1, len(k_list) - 1
        carry: bool = False
        result: List[int] = []
        while iter_a >= 0 or iter_b >= 0:
            sum = carry
            if iter_a >= 0:
                sum += num[iter_a]
            if iter_b >= 0:
                sum += k_list[iter_b]

            carry = sum > 9
            iter_a, iter_b = iter_a - 1, iter_b - 1
            result.append(sum % 10)

        if carry:
            result.append(1)

        return result[::-1]
