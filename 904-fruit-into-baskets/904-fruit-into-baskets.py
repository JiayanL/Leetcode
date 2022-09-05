class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 2 types of fruit
        # pick every fruit
        # longest substring with 2 elements
        
        # initialize variables
        fruit_basket = collections.Counter()
        max_fruits = 0
        start = 0
        
        # move through fruits
        for end in range(len(fruits)):
            # add fruit to basket
            fruit_basket[fruits[end]] += 1

            # while I have more fruit than I need, shrink my basket
            while len(fruit_basket) > 2:
                remove_fruit = fruits[start]
                fruit_basket[remove_fruit] -= 1
                if fruit_basket[remove_fruit] == 0:
                    del fruit_basket[remove_fruit]
                start += 1

            # count the amount of fruit I have right now
            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
            
            