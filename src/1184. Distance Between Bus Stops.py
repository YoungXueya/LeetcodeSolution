class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        
        clockwise=sum(distance[min(start,destination):max(start,destination)])
        counter=sum(distance)-clockwise
        return min(counter,clockwise)
