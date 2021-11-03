# AC

## Log

- **2021/11/03**: Date format is "YYMMDD"; e.g., "930101" means 1931-01-01
- **2021/11/03**: Currency is in Czech koruna in the 1990s
- **2021/11/03**: Fixed dates from strange format into a simpler, universal format "YYYY-MM-DD"

- **2021/11/03**: Perfect AUC is 1.0, AUC of random classifier is 0.5
- **2021/11/03**: Decision tree with different criterions:

| Criterion          | AUC   |
|--------------------|-------|
| `gain_ratio`       | 0.556 |
| `information_gain` | 0.556 |
| `gini_index`       | 0.574 |
| `accuracy`         | 0.498 |

- **2021/11/03**: Some important ideas:
    - Filter out variables that are not of interest.
        - For instance, the date of creation of an account is not, by itself, relevant; the number of years since the account was created until the loan starts is a better loyalty indicator
        - IDs are not of interest, as they are arbitrary and do not add any information; a district ID is arbitrary, but that same district's average income or criminality rate is more revealing of that person's context

- **2021/11/03**: Some ideas of interesting variables:
    - For each account, calculate a score that evaluates how "good" that account is (i.e., the higher the score, the more likely it is that a loan on that account will be paid)
        - The account score can be calculated from the number of previous paid loans, as well as the total movements on that account
            - Maybe normalize those using the loan being requested; if a client has a lot of successful small loans, that is not an indicator that he/she will not default on a larger loan
    - For each client, calculate a score that evaluates how "good" that client is (i.e., the higher the score, the more likely it is that a loan on an account of that client will be paid)
        - The client score may be calculated from:
            - All the client's accounts scores
            - The data from the district the client lives in
            - The age of the client at the end of the loan (if he/she dies she's likely to default)
