class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # init variables
        fruits_in_basket = collections.Counter()
        # fruit counts
        curr_fruits = max_fruits = 0
        # left tree
        first_tree = 0
        
        # go through all fruits
        for i in range(len(fruits)):
            # expand the basket by 1
            fruits_in_basket[fruits[i]] += 1
            
            # check that the basket is in range
            while len(fruits_in_basket) > 2:
                # max_fruits = max(max_fruits, i - first_tree)
                
                fruits_in_basket[fruits[first_tree]] += -1
                if fruits_in_basket[fruits[first_tree]] == 0:
                    del fruits_in_basket[fruits[first_tree]]
                    
                # decrease the left bucket by 1
                first_tree += 1
            max_fruits = max(max_fruits, i - first_tree + 1)
        # just in case checker for the last case (inclusive of the last case)
        # max_fruits = max(max_fruits, i - first_tree + 1)
        
        return max_fruits
                
            
            
            