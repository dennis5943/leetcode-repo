"""
A transaction is possibly invalid if:

	the amount exceeds $1000, or;
	if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 
Example 1:
Input: transactions = [&quot;alice,20,800,mtv&quot;,&quot;alice,50,100,beijing&quot;]
Output: [&quot;alice,20,800,mtv&quot;,&quot;alice,50,100,beijing&quot;]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:
Input: transactions = [&quot;alice,20,800,mtv&quot;,&quot;alice,50,1200,mtv&quot;]
Output: [&quot;alice,50,1200,mtv&quot;]

Example 3:
Input: transactions = [&quot;alice,20,800,mtv&quot;,&quot;bob,50,1200,mtv&quot;]
Output: [&quot;bob,50,1200,mtv&quot;]

 
Constraints:
	transactions.length <= 1000
	Each transactions[i] takes the form &quot;{name},{time},{amount},{city}&quot;
	Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
	Each {time} consist of digits, and represent an integer between 0 and 1000.
	Each {amount} consist of digits, and represent an integer between 0 and 2000.


"""
from typing import List
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().invalidTransactions(0) == 0

