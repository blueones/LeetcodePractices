var serialize = function(root) {
    if(!root){
        return []
    }
    let binArr = []
    let q = [root]
    while(q.length>0){
        let cur = q.shift()
        if(cur!==null){
            q.push(cur.left)
            q.push(cur.right)
            binArr.push(cur.val)
        }else{
            binArr.push(null)
        }
    }
    return binArr
};

var deserialize = function(data) {
    if(data.length==0){
        return null
    }
    let ans = new TreeNode(data.shift())
    let result = ans
    let level = [ans]
    while(level.length>0){
        let cur = level.shift()
        let left = data.shift()
        let right = data.shift()
        if(left!==null && left!==undefined){
            let nl = new TreeNode(left)
            cur.left = nl
            level.push(nl)
        }
        if(right!==null && right!==undefined){
            let nr = new TreeNode(right)
            cur.right = nr
            level.push(nr)
        }
    }
    return result
};