from typing import List,Tuple , Dict , Union

person : List[int] = [1,5,16,15,12,2]
person : Tuple[str , int] = ("vashu", 16)
source : dict[str , int] = {"vashu" : 100 , "priyansh" :100 }
identifier : Union[str , int] = "ID1215VV"


n : int = 5
name : str = "Priyansh"


def sum(a : int,b : int) -> int:
    return a+b

a = sum(5,6)
print(a)