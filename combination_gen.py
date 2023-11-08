from numpy import array
import copy
def gen_comb_list(list_set):
    '''
        Parameters:
            list_set: a list of lists where each contains at least one element

        Returns:
            a list of lists, each of which is made from a combination of elements in each list in list_set

        Examples:
            gen_comb_list([[1, 2, 3]]) returns [[1], [2], [3]]
            gen_comb_list([[1, 2, 3], [4, 5]]) returns [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
            gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]) returns [[1, 4, 6], [2, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6], [3, 5, 6], [1, 4, 7], [2, 4, 7], [3, 4, 7], [1, 5, 7], [2, 5, 7], [3, 5, 7], [1, 4, 8], [2, 4, 8], [3, 4, 8], [1, 5, 8], [2, 5, 8], [3, 5, 8]]
    '''
    list_set.reverse()
    new_l = []
    num = 1
    for ele in list_set:
        num *= len(ele)
    for i in range(num):
        new_l.append([])
    pre = 1
    for c, ele in enumerate(list_set):
        i = 0
        num = int(num/len(ele))
        for p in range(int(pre)):
            for j in ele:
                for k in range(num):
                    new_l[i].append(j)
                    i += 1
        pre *= len(ele)
    for ele in new_l:
        ele.reverse()
    return new_l


print(gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]))
