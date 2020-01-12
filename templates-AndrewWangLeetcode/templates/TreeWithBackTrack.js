// https://leetcode.com/problems/path-sum-iii/
var pathSum = function(root, sum) {
    //backtrack that keeps the running sum of the current path
    //the data structure for track could be different from problem to problem
    //could be just an in or array or something else
    let track = [0]
    let ans = 0
    
    const traverse = (node)=>{
        //TEST FOR BASE CASE (depends on problem)
        let end = track.length-1
        for(let i=0; i<=end; i++){
            if(track[end]-track[i]+node.val===sum){
                ans++
            }
        }
        //END TEST FOR BASE CASE
        
        
        track.push(node.val+track[end])//add current node's value to the track
        if(node.left) traverse(node.left)
        if(node.right) traverse(node.right)
        track.pop()//remove the current node's value to the track
        
    }
    
    if(root) traverse(root)
    return ans
};