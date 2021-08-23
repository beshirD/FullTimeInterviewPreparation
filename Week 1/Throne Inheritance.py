from collections import defaultdict, List
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append((childName))
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []
        visited = set()
        self.successor(self.kingName,inheritanceOrder,visited)
        return inheritanceOrder

    def successor(self,successor,inheritanceOrder,visited):
        visited.add(successor)
        
        if successor not in self.dead:
            inheritanceOrder.append(successor)

        for child in self.graph[successor]:
            if child not in visited:
                self.successor(child,inheritanceOrder,visited)
        
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()