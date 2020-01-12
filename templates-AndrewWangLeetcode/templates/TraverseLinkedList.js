var copyRandomList = function(head) {   
    if(!head){
        return null
    }
    let dummyHead1 = head
    
    while(dummyHead1){
        let tmpNext = dummyHead1.next
        dummyHead1.next = new Node(dummyHead1.val, dummyHead1.next)
        dummyHead1 = tmpNext
    }
    
    let randomHead = head
    let cloneRandom = head.next
    while(cloneRandom){
        cloneRandom.random = randomHead.random ? randomHead.random.next : null
        randomHead = randomHead.next.next
        cloneRandom = cloneRandom.next ? cloneRandom.next.next : null
    }
    
    let original = head
    let cloned = head.next
    let ans = head.next
    while(cloned){
        original.next = original.next.next
        cloned.next = cloned.next ? cloned.next.next : null
        original = original.next
        cloned = cloned.next
    }
    
    return ans
};