# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(nums):

    if sum(nums) <= 21:
        print(sum(nums))
    elif sum(nums) > 21:
        if 11 in nums:
            reduce_by_11 = sum(nums) - 10
            if reduce_by_11 > 21:
                print("Bust")
            else:
                print(reduce_by_11)
        else:
            print("Bust")
    else:
        print("Bust")

blackjack([5,6,7])
blackjack([9,9,9])
blackjack([9,9,11])