const Trie=function(){
    let trie = {}
    insert = (wordArray)=>{
        let tempTrie = trie
        wordArray.forEach(letter=>{
            if(!tempTrie[letter]){
                tempTrie[letter]={exists:true}
            }
            tempTrie = tempTrie[letter]
        })
        tempTrie["end"]=true
    }
    findWhole = (wordArray)=>{
        let tempTrie = trie
        wordArray.forEach(letter=>{
            if(!tempTrie[letter]){
                tempTrie = {}
            }else{
                tempTrie = tempTrie[letter]
            }
        })
        return tempTrie["end"]?true:false
    }
    findPart = (wordArray)=>{
        let tempTrie = trie
        tempTrie.forEach(letter=>{
            if(!tempTrie[letter]){
                tempTrie = {}
            }else{
                tempTrie = tempTrie[letter]
            }
        })
        return tempTrie["exists"]?true:false
    }
}