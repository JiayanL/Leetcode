class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high = 0, len(arr) - 1
        i = 0
        
        while (i <= high):
            if arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                i += 1
                low += 1
            elif arr[i] == 1:
                i += 1
            elif arr[i] == 2:
                arr[i], arr[high] = arr[high], arr[i]
                high -= 1