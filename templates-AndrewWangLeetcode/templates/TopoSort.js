var findOrder = function(numVertex, inputEdgeArray) {
    let result = []
    let visited = new Array(numVertex).fill(false)
    let sorted = new Array(numVertex).fill(false)
    let edgeDict = {}

    //transform into object for easy lookup
    inputEdgeArray.forEach(prereq=>{
        if(!edgeDict[prereq[0]]){
            edgeDict[prereq[0]] = [prereq[1]]
        }else{
            edgeDict[prereq[0]].push(prereq[1])
        }
    })
    
    //essentially a dfs algo
    const topoSort = (node)=>{
        if(visited[node]) return false //loop
        visited[node]=true //mark as visited for this iteration of search
        
        let res = true
        let neighbors = edgeDict[node]
        if(neighbors && neighbors.length>0){
            for(let i=0; i<neighbors.length; i++){
                res = res && topoSort(neighbors[i])
            }
        }
        if(!res) return false//loop detected from neighbor

        if(!sorted[node]){
            sorted[node]=true
            result.push(node)
        }
        visited[node]=false
        return true
    }
    
    //initializing the topo sort
    //traverse through each unsorted vertex
    for(let i=0; i<numVertex; i++){
        if(!sorted[i]){
            let res = topoSort(i)
            if(!res) break;
        }
    }
    
    if(result.length===numVertex){
        return result
    }else{
        return []
    }
};