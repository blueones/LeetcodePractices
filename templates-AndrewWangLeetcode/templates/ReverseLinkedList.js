//recursive way
var reverseList = function(head) {
    if(head && head.next){
        let res = reverseList(head.next)
        head.next.next = head
        head.next = null
        return res
    }else{
        return head
    }
};

//iterative way
var reverseList = function(head) {
    let prev = null
    let cur = head
    while(cur){
        let tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    }
    return prev
};