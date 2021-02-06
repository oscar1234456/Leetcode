class Solution:
    def simplifyPath(self, path: str) -> str:
        mystack = list()
        component = path.split("/")
        res = ""

        for item in component[1:]:
            if item == "..":
                if len(mystack)!=0:
                    mystack.pop()
            elif item == "." or item =='':
                continue
            else:
                mystack.append(item)
        if len(mystack)==0:
            return "/"
        while len(mystack)>0:
            res = "/"+mystack.pop() + res
        return res
#beats 72.80%