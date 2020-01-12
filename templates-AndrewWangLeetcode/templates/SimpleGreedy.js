// https://leetcode.com/problems/campus-bikes/

var simpleGreedy = function(origins, targets) {
    let costs = {}
    for(let oi=0; oi<origins.length; oi++){
        let o = origins[oi]
        for(let ti=0; ti<targets.length; ti++){
            let t = targets[ti]
            let d = Math.abs(o[0]-t[0])+Math.abs(o[1]-t[1])
            if(costs[d]){
                costs[d].push([oi, ti])
            }else{
                costs[d]=[[oi, ti]]
            }
        }
    }
    
    let assignedOrigins = new Array(origins.length).fill(-1)
    let assignedTargets = new Array(targets.length).fill(-1)
    //the 2000 here is an artificial limit imposed by the problem
    //in other problems, it is best to either get all keys from costs and iterate over them
    //or figure out the artificial limit for that particular problem
    for(let i=0; i<=2000; i++){
        let currentCost = costs[i]
        if(currentCost){
            currentCost.forEach(cost=>{
                if(assignedOrigins[cost[0]]===-1 && assignedTargets[cost[1]]===-1){
                    assignedOrigins[cost[0]]=cost[1]
                    assignedTargets[cost[1]]=1
                }
            })
        }
    }
    return assignedOrigins
};