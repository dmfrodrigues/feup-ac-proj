# Keypoints

The bank wants to improve their understanding of customers and seek specific actions to improve services.
Therefore it is looking for an instrument that evaluates the risk of non-payment of loans by clients.

## BU: analysis of requirements with the end user

The user requirements, put in a concise way, are:

- To solve the descriptive problem
  - Which consists of understanding client, and creating standardized client profiles by grouping them based on their data and behavior
- To solve the predictive problem
  - By implementing a predictive system
    - To better understand new clients, by fitting them into the previously discovered client profiles.
    - To help bank employees in decision-making when assessing risk in a loan request.
    - To speed up the loan application process, by making an automatic profile analysis and risk assessment.
    - To reduce loan defaulting by denying credit to clients we do not expect to be able to pay off.
    - To reduce loan defaulting by anticipating loan default, and negotiate a change of terms with the client.
    - To reduce the losses associated to loan defaulting by adjusting interest in proportion to the risk of defaulting (a client with a higher risk of defaulting will be made to pay more interests because banks want to take as much interest out of the client before he/she defaults).
    - To give more favorable conditions to good clients by reducing interests in their loans, thus making the bank more attractive and competitive for those customers when compared to other banks.

## BU: definition of business goals

The positive case is the one where the borrower defaults.

The business goal is to design a predictive system that helps the bank to reach the following goals:
- Reduce defaulting significantly
  - Assuming we don't give credit to people that we think won't pay off; we simply don't give them credit
  - Reduce defaulting by 75% (force false negatives rate below 25%, or keep true positive rate above 75%)
  - I.e., among those that defaulted, we intend to have a system that can detect at least 75% of those that defaulted that went undetected (and whose result we now know, because bank data says they defaulted).
- Do not significantly reduce credit to good clients
  - Give credit to at least 95% of the good clients (keep true negative rate above 95%, or keep false positive rate below 5%)
  - I.e., if a manual analysis led to approved credit for a set of clients and all of them paid, the system must correctly predict as the negative case at least 95% of those that paid off.

## BU: translation of business goals into data mining goals

As stated, we want to develop a system that, at a certain certainty threshold, has:
- TPR > 0.75
- FPR < 0.05

This means that the ROC curve should, at least in one point, be in the area defined by the above condition. This is a small area in the top left of the ROC graph, which is taller (0.25) than it is wide (0.05).

The smallest possible AUC value for this constraint is 0.7125 (Fig. 1), by taking the area in the rectangle with sides x=[0.05, 1] and y=[0, 0.75]. It is however very naive and highly unlikely that a ROC with AUC=0.7125 can, at some point, meet the established threshold.

The minimum AUC that we even believe might meet the threshold is the area below the graph if it is a straight line from (0,0) to (0.05, 0.75), and from there to (1,1) (Fig. 2). This gives 0.85, which we consider to be our threshold for considering the result quality as reasonable.

A good AUC would be if the vertex on the constraint area was near (0.025, 0.85) (Fig. 3), which gives an AUC of 0.9125. This is the AUC we will use to consider the result quality as good.

| Figure 1 | Figure 2 | Figure 3 |
|:-:|:-:|:-:|
| ![](https://i.imgur.com/O2hT26B.png) | ![](https://i.imgur.com/SOgWkYe.png) | ![](https://i.imgur.com/XrBSbUA.png) |
