class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i<len(arr):
            j=0
            while j<len(pieces):
                if arr[i] == pieces[j][0]: #Somebody same
                    if len(pieces[j])>1: #it is two or more elements
                        i+=1
                        k = 1
                        while k< len(pieces[j]):
                            if pieces[j][k] != arr[i]:
                                return False
                            else:
                                k+=1
                                i+=1
                        pieces.remove(pieces[j])
                        break
                    else: #it is one element
                        pieces.remove(pieces[j])
                        i += 1
                        break
                elif j==len(pieces)-1: #Eveybody different
                    return False
                else:
                    j += 1
        return True
#2021/1/2 12:23 p.m. TW Time