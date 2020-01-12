class UnionFind{
    constructor(numVertices, edges){
        this.numVertices = numVertices
        this.edges = edges
        this.roots = [...Array(numVertices).keys()]
    }
    union(v1, v2){
        let r1 = this.find(v1)
        let r2 = this.find(v2)
        if(r1===r2)return false
        this.roots[r1] = r2
    }
    find(v){
        let parent = this.roots[v]
        if(parent === v){
            return v
        }else{
            return this.roots[v] = this.find(parent)
        }
    }
    startUnion(){
        for(let i=0; i<this.edges.length; i++){
            this.union(this.edges[i][0], this.edges[i][1])
        }
    }
    getDistinctSets(){
        let count = 0;
        for(let i=0; i<this.numVertices; i++){
            if(this.roots[i]===i){
                count++
            }
        }
        return count
    }
}
let uf = new UnionFind(6, [[0,1], [2,1], [3,4]])
uf.startUnion()
console.log(uf.getDistinctSets())