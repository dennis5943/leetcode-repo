/*
In the video game Fallout 4, the quest &quot;Road to Freedom&quot; requires players to reach a metal dial called the &quot;Freedom Trail Ring&quot;, and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

	You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring&#39;s characters at the 12:00 direction, where this character must equal to the character key[i].
	If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you&#39;ve finished all the spelling.

Example:

 

Input: ring = &quot;godding&quot;, key = &quot;gd&quot;
Output: 4
Explanation:
For the first key character &#39;g&#39;, since it is already in place, we just need 1 step to spell this character. 
For the second key character &#39;d&#39;, we need to rotate the ring &quot;godding&quot; anticlockwise by two steps to make it become &quot;ddinggo&quot;.
Also, we need 1 more step for spelling.
So the final output is 4.

Note:
	Length of both ring and key will be in range 1 to 100.
	There are only lowercase letters in both strings and might be some duplcate characters in both strings.
	It&#39;s guaranteed that string key could always be spelled by rotating the string ring.


*/
pub struct Solution {}
impl Solution {
    pub fn find_rotate_steps(ring: String, key: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_rotate_steps(0));
  println!("Pass test cases!");
}
