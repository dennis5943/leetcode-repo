/*
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

	push(int x), which pushes an integer x onto the stack.
	pop(), which removes and returns the most frequent element in the stack.
	
		If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
	
	

 

Example 1:
Input: 
[&quot;FreqStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].

 

Note:
	Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
	It is guaranteed that FreqStack.pop() won&#39;t be called if the stack has zero elements.
	The total number of FreqStack.push calls will not exceed 10000 in a single test case.
	The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
	The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

 


*/
pub struct Solution {}
struct FreqStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FreqStack {

    fn new() -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj = FreqStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
