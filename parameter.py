def func(first, second):
    first += 10
    second.add(4)

number=1 #immutable : 원본이 수정되지 않음 ( ex : number , string , tuple )
set={1,2,3} #mutable : 원본이 수정됨 ( ex : list , dictionary , set )
func(number, set)
print(number, set)
