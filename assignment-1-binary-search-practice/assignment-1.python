def count_rotations_linear(nums):
    position = 0                 # What is the intial value of position?
    
    while position < len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position]<nums[position-1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return 0     

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = (hi+lo)//2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        #print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and mid_number == nums[hi]:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
            
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0
