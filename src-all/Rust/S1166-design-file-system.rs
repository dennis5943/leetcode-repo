/*
You are asked to design a file system which provides two functions:

	createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn&#39;t exist.
	get(path): Returns the value associated with a path or returns -1 if the path doesn&#39;t exist.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

 
Example 1:
Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1

Example 2:
Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn&#39;t exist.
fileSystem.get("/c"); // return -1 because this path doesn&#39;t exist.

 
Constraints:
	The number of calls to the two functions is less than or equal to 10^4 in total.
	2 <= path.length <= 100
	1 <= value <= 10^9

NOTE: create method has been changed on August 29, 2019 to createPath. Please reset to default code definition to get new method signature.

*/
pub struct Solution {}
struct FileSystem {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FileSystem {

    fn new() -> Self {
        
    }
    
    fn create_path(&self, path: String, value: i32) -> bool {
        
    }
    
    fn get(&self, path: String) -> i32 {
        
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * let obj = FileSystem::new();
 * let ret_1: bool = obj.create_path(path, value);
 * let ret_2: i32 = obj.get(path);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
