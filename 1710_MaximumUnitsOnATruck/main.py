class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        Solution.sortList(boxTypes)
        counter = 0
        for box in boxTypes:
            print(f'Trucksize: {truckSize}')
            if truckSize == 0:
                break
            elif truckSize - box[0] > -1:
                truckSize -= box[0]
                counter += box[0] * box[1]
            else:
                counter += truckSize * box[1]
                truckSize = 0
        return counter

    # bubble sort
    @staticmethod
    def sortList(list):
        n = len(list) - 1
        for i in range(len(list)):
            for j in range(n):
                if list[j][1] < list[j + 1][1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
            n -= 1