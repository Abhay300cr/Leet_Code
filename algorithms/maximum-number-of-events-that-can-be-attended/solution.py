import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort events by start day
        events.sort(key=lambda x: x[0])
        
        min_heap = []
        ans = 0
        i = 0
        n = len(events)
        
        # Max end day specified in constraints is 100000
        # Jump directly to the next event's start day if heap is empty
        day = 0
        
        while i < n or min_heap:
            # If no ongoing events, fast-forward to the next available event's start day
            if not min_heap:
                day = events[i][0]
                
            # Add all events starting on the current day to the heap
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
                
            # Remove all events that have already ended before 'day'
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
                
            # Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                ans += 1
                day += 1
                
        return ans