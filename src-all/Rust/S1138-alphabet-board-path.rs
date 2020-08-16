/*
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

	&#39;U&#39; moves our position up one row, if the position exists on the board;
	&#39;D&#39; moves our position down one row, if the position exists on the board;
	&#39;L&#39; moves our position left one column, if the position exists on the board;
	&#39;R&#39; moves our position right one column, if the position exists on the board;
	&#39;!&#39; adds the character board[r][c] at our current position (r, c) to the answer.

(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 
Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

 
Constraints:
	1 <= target.length <= 100
	target consists only of English lowercase letters.

*/
pub struct Solution {}
impl Solution {
    pub fn alphabet_board_path(target: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::alphabet_board_path(0));
  println!("Pass test cases!");
}
