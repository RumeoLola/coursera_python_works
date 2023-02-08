# main function
def main():
    # user prompt
    sort_list = []
    for prompt_val in range(3):
        print("Input 3 different numbers ")
        user_prompt = int(input())
        sort_list.append(user_prompt)
        sort_list.sort()
    print("Sorted list is ", sort_list)


main()
