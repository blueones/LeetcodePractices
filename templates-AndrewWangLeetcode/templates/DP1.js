//A simple DP formula that derives the answer from a 2-D matrix
//In this case answers are derived from it's neighbors
//Solution(i,j) is derived from Solution(i-1, j), Solution(i, j-1) and Solution(i-1, j-1)
//This is often the case for many DP problems

var minDistance = function(word1, word2) {

    //initialize the memo for DP
    //in this case the size is one bigger than the words
    let matrix = new Array(word1.length+1).fill(0).map(a=>{
        return new Array(word2.length+1)
    })
    
    for(let i=0; i<word1.length+1; i++){
        for(let j=0; j<word2.length+1; j++){
            //the if and else if statements are there to initialize the matrix (for this scenario)
            if(i===0 && j===0){
                matrix[i][j]= 0;
            }else if(i===0){
                matrix[i][j]= j;
            }else if(j===0){
                matrix[i][j]= i;
            }else{
                //Here is the core of hte problem
                //the solution is the min of:
                //top neigbor +1
                //left neightbor +1
                //top-left neighbor +1/+0 depend on if the current character is the same
                matrix[i][j]= Math.min(matrix[i-1][j]+1, 
                                       matrix[i][j-1]+1, 
                                       matrix[i-1][j-1]+(word1.charAt(i-1)===word2.charAt(j-1)?0:1) )
            }
        }
    }
    return matrix[word1.length][word2.length]
};