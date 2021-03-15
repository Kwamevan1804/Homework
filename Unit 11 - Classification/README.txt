## README FILE UNIT 11 - CLASSIFICATION

# RESAMPLING MODELS

Which model had the best balanced accuracy score?

The two oversampling models and combination sampling models produced the best balanced accuracy score (0.9934). Followed by the undersampling model (0.9929)
and original data logistic regression model (0.9889)

Which model had the best recall score?

All resampling models recorded a slightly higher combined recall score of 0.99 vs the original data logistic regression model which had slightly lower 'high risk' recall

Which model had the best geometric mean score?

All models had comparable geometric mean scores of 0.99

# ENSEMBLE LEARNING

Which model had the best balanced accuracy score?

Th Easy Ensemble Classifier (EEC) outscores the Balanced Random Forest (BRF) Classifier by 0.83 to 0.76

Which model had the best recall score?

EEC outscores BRF Classifier on recall for high_risk loans by 0.80 to 0.65
 
Which model had the best geometric mean score?

EEC outperforms BRF on geometric mean score 0.83 vs 075 

What are the top three features?

(0.0731885912769716, 'total_rec_prncp'),
 (0.060925386731491366, 'total_pymnt_inv'),
 (0.05995925273012057, 'total_rec_int'),
