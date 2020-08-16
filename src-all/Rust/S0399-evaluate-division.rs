/*
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given  a / b = 2.0, b / c = 3.0.
queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return  [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is:  vector<pair<string, string>> equations, vector<double>&amp; values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return  vector<double>.

According to the example above:

equations = [ [&quot;a&quot;, &quot;b&quot;], [&quot;b&quot;, &quot;c&quot;] ],
values = [2.0, 3.0],
queries = [ [&quot;a&quot;, &quot;c&quot;], [&quot;b&quot;, &quot;a&quot;], [&quot;a&quot;, &quot;e&quot;], [&quot;a&quot;, &quot;a&quot;], [&quot;x&quot;, &quot;x&quot;] ]. 

 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

*/
pub struct Solution {}
impl Solution {
    pub fn calc_equation(equations: Vec<Vec<String>>, values: Vec<f64>, queries: Vec<Vec<String>>) -> Vec<f64> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::calc_equation(0));
  println!("Pass test cases!");
}
