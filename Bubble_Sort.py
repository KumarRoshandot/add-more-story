#------Bubble Sort-----------------------------------------#
#-- Enter your input as comma separated numbers          --#
#-- Swap Position Until all the elements are sorted      --#
#----------------------------------------------------------#

def bubble_sort(arr):
    
    def swap_idx(idx1,idx2):
        arr[idx2],arr[idx1] = arr[idx1],arr[idx2]
        
    arr_len = len(arr)
    swap_flag = True
    
    while swap_flag:
        count = 0
        for i in range(1,arr_len):
            if arr[i-1] > arr[i]:
                swap_idx(i-1,i)
            else:
                count += 1
        if count+1 == arr_len:swap_flag = False
    
    print('Bubble Sort Output')
    print(arr,end = ' ')


def main():
    try:
        arr = list(map(int,input().split(',')))
    except:
        print('Enter Valid input')
    bubble_sort(arr)
    

if __name__ == "__main__":
    main()