## Real-World Problem: Customer Discount Eligibility

**Problem Statement:**

A retail store has a loyalty program. Customers are eligible for a 15% discount on their total purchase if they meet *one* of the following conditions:

1.  They are a member of the loyalty program (indicated by a boolean `is_loyalty_member`).
2.  Their total purchase amount (`purchase_amount`) is over $200.

However, there is an *additional* condition: if a customer uses a special discount coupon (indicated by a boolean `has_discount_coupon`), they are *not* eligible for the loyalty program discount, even if they meet the other criteria.

**Task:**

Write a program that determines if a customer is eligible for the 15% loyalty program discount based on their loyalty membership status, purchase amount, and whether they have a discount coupon. Print a message indicating whether they are eligible and the final price if they are.

**Steps to Solve:**

1.  **Define Variables:** Create variables to represent the customer's `is_loyalty_member` (boolean), `purchase_amount` (float), and `has_discount_coupon` (boolean). Assign sample values to these variables.
2.  **Check Discount Eligibility (Initial):** Use a combination of comparison and logical operators (`>=`, `or`) to check if the customer meets the initial criteria for the loyalty discount (member OR purchase amount > $200).
3.  **Check for Coupon Conflict:** Use a logical operator (`and`) to check if the customer is initially eligible *and* has a discount coupon.
4.  **Determine Final Eligibility:** Use a logical operator (`not`) to negate the result of the coupon conflict check. If they were initially eligible AND did NOT have a coupon, they are finally eligible.
5.  **Apply Discount (if eligible):** If the customer is finally eligible for the discount, calculate the discounted price.
6.  **Print Results:** Use f-strings to print a clear message indicating whether the customer is eligible for the loyalty discount and, if so, their final discounted price.
