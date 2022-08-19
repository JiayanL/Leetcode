class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high, i = 0, len(arr) - 1, 0
        
        while (i <= high):
            if arr[i] == 0:
                arr[low], arr[i] = arr[i], arr[low]
                i += 1
                low += 1
            elif arr[i] == 1:
                i += 1
            elif arr[i] == 2:
                arr[high], arr[i] = arr[i], arr[high]
                high -= 1
            # print(arr)