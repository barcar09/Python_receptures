my_simple_list = [1,2,3,8,13,24]
usable = my_simple_list[0:-4]

print(usable)

only_one,_= usable

print(only_one)

more_complicated_structure = [[1,4,5], [8,9,10] ,[12,18,36]]
#get two element of list if first el is divided by 2
for elg in more_complicated_structure:
    print(elg)
mod_2_structure = [els for el, *els in more_complicated_structure if el%2==0] 

print(mod_2_structure)
    

#recursive aglhoritm that add a lists

def sums(lists):
    first,*other = lists
    print(other)
    return first + sums(other) if other else first

print(sums(my_simple_list))

one_more_test = [1]

elgs,*back = one_more_test

print(back,"let's see")
