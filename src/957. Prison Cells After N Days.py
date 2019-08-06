class Solution:
    # There are only 2^6 possible values of cells, so there must be cycles.
    # N appears first time - second is the cycle length
    # So mode the cycle length will reduce redundent operation
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextCell(cells):
            return [0]+[int(cells[i-1]==cells[i+1]) for i in range(1,7)]+[0]
        seen={}
        while N:
            c=tuple(cells)
            if c in seen:
                N%=seen[c]-N
            seen[c]=N
            
            if N>=1:
                N-=1
                cells=nextCell(cells)
       

        return cells
        
