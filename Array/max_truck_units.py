class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse = True)
        total_units = 0
        
        for boxes, units in sorted_boxes:            
            if boxes <= truckSize:
                truckSize -= boxes
                total_units += (boxes * units)
            else:
                total_units += (truckSize * units)
                break
                
        return total_units
