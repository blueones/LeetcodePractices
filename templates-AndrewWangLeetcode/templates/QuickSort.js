//This algo takes nlog(n) time complexity
//This algo is done in place so take constant time
const sortIntegers = function (inputArray) {
    //MAIN FUNCTION
    const quickSort = (nums, l, r) => {
        if (l >= r) {
            return
        }
        let pivotIndex = pivot(nums, l, r)
        quickSort(nums, l, pivotIndex - 1)
        quickSort(nums, pivotIndex + 1, r)
    }

    //pivot helper
    //the core of the algo
    const pivot = (nums, l, r) => {
        //a pivot can be picked in many ways
        //but easiest is to pick the last element in the current list
        //as you will always want to move the chosen pivot to the last spot to get it out of the way
        let pivotNum = nums[r]
        //starting with the left side of the current segment
        //pivotPos essentially guarantees that all elements to the left of it
        //are smaller than pivotNum, it keeps track of the position the pivot is at
        let pivotPos = l
        for (let i = l; i < r; i++) {
            //swap only if the ith number is smaller than pivotNum
            if (nums[i] < pivotNum) {
                //swap the i-th element with the pivotPos
                //essentially saying i belongs to the left side
                //since there is now an additional number to the left of pivot
                //the position of the pivot needs to increase
                [nums[pivotPos], nums[i]] = [nums[i], nums[pivotPos]]
                pivotPos++
            }
        }
        //swap the pivot element into the pivot position, 
        //since it was previously at the end of the list
        [nums[r], nums[pivotPos]] = [nums[pivotPos], nums[r]]
        return pivotPos
    }

    //CALLING THE MAIN FUNCTION
    quickSort(inputArray, 0, inputArray.length - 1)
}