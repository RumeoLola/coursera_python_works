def name_shuffler(str_):
    #your code here
    if len(str_) <= 1:
        return str_
    mid = str_[1:len(str_) - 1]
    return str_[len(str_) - 1] + mid + str_[0]
