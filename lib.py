def convert_list_to_dict(lst):
    it = iter(lst)
    res_dct = dict(zip(it, it))
    return res_dct
 
