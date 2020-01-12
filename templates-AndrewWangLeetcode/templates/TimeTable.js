var minMeetingRooms = function(intervals) {
    let timeTable = {}
    intervals.forEach(meet=>{
        if(!timeTable[meet[0]]){
            timeTable[meet[0]] = 1
        }else{
            timeTable[meet[0]]++
        }
        
        if(!timeTable[meet[1]]){
            timeTable[meet[1]] = -1
        }else{
            timeTable[meet[1]]--
        }
    })
    
    //not necessary if it all numbers
    let orderedKeys = Object.keys(timeTable).sort((timea, timeb)=>{
        return timea-timeb
    })
    
    let curr = 0;
    let maxOverlap = 0;
    for(let i=0; i<orderedKeys.length; i++){
        curr += timeTable[orderedKeys[i]]
        maxOverlap = Math.max(maxOverlap, curr)
    }
    return maxOverlap;
};