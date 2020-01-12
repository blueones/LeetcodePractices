var shortestPathBinaryMatrix = function(grid) {
    //grid of only 0 and 1
    //0 means it's a valid route
    //1 means it's blocked
    //return -1 if there is no path
    //this is a BFS search template
    let directions = [
        [-1,-1],
        [-1,0],
        [-1,1],
        [0,-1],
        [0, 1],
        [1,-1],
        [1, 0],
        [1, 1]
    ]
    let queue = []
    let path = new Array(grid.length).fill(0).map(a=> new Array(grid.length).fill(-1))

    if(grid.length>0 && grid[0][0]===0 && grid[grid.length-1][grid.length-1]===0){
        queue.push([0,0])
        path[0][0]=1
    }else{
        return -1
    }
    
    const validPos = (x, y)=>{
        if( x>=0 && x<grid.length 
            && y>=0 && y<grid.length
            && path[x][y]===-1 && grid[x][y]===0){
                //check boundary conditions
                //check if the path has not been traversed already
                //because it's BFS, if it has been set already, it's always the lowest number already
                
            return true
        }else{
            return false
        }
    }
    
    while(queue.length>0){
        let start = queue.shift();
        for(let i=0; i<directions.length; i++){
            let x = start[0]+directions[i][0]
            let y = start[1]+directions[i][1]
            if(validPos(x, y)){
                path[x][y]=path[start[0]][start[1]]+1
                queue.push([x,y])
            }
        }
    }

    return path[grid.length-1][grid.length-1]
};
