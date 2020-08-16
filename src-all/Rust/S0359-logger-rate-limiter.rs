/*
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string &quot;foo&quot; at timestamp 1
logger.shouldPrintMessage(1, &quot;foo&quot;); returns true; 

// logging string &quot;bar&quot; at timestamp 2
logger.shouldPrintMessage(2,&quot;bar&quot;); returns true;

// logging string &quot;foo&quot; at timestamp 3
logger.shouldPrintMessage(3,&quot;foo&quot;); returns false;

// logging string &quot;bar&quot; at timestamp 8
logger.shouldPrintMessage(8,&quot;bar&quot;); returns false;

// logging string &quot;foo&quot; at timestamp 10
logger.shouldPrintMessage(10,&quot;foo&quot;); returns false;

// logging string &quot;foo&quot; at timestamp 11
logger.shouldPrintMessage(11,&quot;foo&quot;); returns true;

*/
pub struct Solution {}
struct Logger {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Logger {

    /** Initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    fn should_print_message(&self, timestamp: i32, message: String) -> bool {
        
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * let obj = Logger::new();
 * let ret_1: bool = obj.should_print_message(timestamp, message);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
