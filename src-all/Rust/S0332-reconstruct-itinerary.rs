/*
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
	If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary [&quot;JFK&quot;, &quot;LGA&quot;] has a smaller lexical order than [&quot;JFK&quot;, &quot;LGB&quot;].
	All airports are represented by three capital letters (IATA code).
	You may assume all tickets form at least one valid itinerary.
	One must use all the tickets once and only once.

Example 1:
Input: [[&quot;MUC&quot;, &quot;LHR&quot;], [&quot;JFK&quot;, &quot;MUC&quot;], [&quot;SFO&quot;, &quot;SJC&quot;], [&quot;LHR&quot;, &quot;SFO&quot;]]
Output: [&quot;JFK&quot;, &quot;MUC&quot;, &quot;LHR&quot;, &quot;SFO&quot;, &quot;SJC&quot;]

Example 2:
Input: [[&quot;JFK&quot;,&quot;SFO&quot;],[&quot;JFK&quot;,&quot;ATL&quot;],[&quot;SFO&quot;,&quot;ATL&quot;],[&quot;ATL&quot;,&quot;JFK&quot;],[&quot;ATL&quot;,&quot;SFO&quot;]]
Output: [&quot;JFK&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;SFO&quot;]
Explanation: Another possible reconstruction is [&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;ATL&quot;,&quot;SFO&quot;].
             But it is larger in lexical order.


*/
pub struct Solution {}
impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_itinerary(0));
  println!("Pass test cases!");
}
