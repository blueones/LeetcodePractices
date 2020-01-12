//This algo is to find the K-th smallest element in the array
//can be easily modified to find K-th largest by doing K = inputArray-K

//This algo takes O(2n) so it's O(n) time complexity
//This algo is done it place so it's constant space
const findIntegers = function (inputArray, K) {
    //MAIN FUNCTION
    const quickFind = (nums, l, r) => {
        if (l >= r) {
            return nums[l]
        }
        let pivotIndex = pivot(nums, l, r)
        //The reason this algo is 2n instead of nlogn is is because
        //it does not need to go through both halves, just one half
        if(pivotIndex>K){
            quickFind(nums, l, pivotIndex - 1)
        }else{
            quickFind(nums, pivotIndex + 1, r)
        }
    }

    //pivot helper
    //the core of the algo
    //SAME AS THE QUICK SORT ALGO
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
    return quickFind(inputArray, 0, inputArray.length - 1)
}