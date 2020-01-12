//find the target element in a sorted list

//This algo takes Olog(n)
//This algo is done it place so it's constant space
const findIntegers = function (inputArray, target) {
    //MAIN FUNCTION
    const binarySearch = (inputArray, l, r, target)=>{
        //this is an iterative approach, simplier and more elegant
        //than a recursive approach
        while(l<r){
            let mid = Math.floor((l+r)/2);
            let midNum = inputArray[mid]

            //get the middle number and compare
            //if midNum is too small, get rid of the left half by setting l to the mid point+1
            //if midNum is too big, get rid of the right half by setting r to the mid point-1
            //otherwise it's found then return the position
            if(midNum===target)return mid
            if(midNum<target){
                l = mid+1
            }else{
                r = mid-1
            }
        }
        return -1//not found
    }

    //Calling the main function
    return binarySearch(inputArray,0, inputArray.length-1, target)
}