## README FILE HOMEWORK UNIT 14 DEEP LEARNING

Which model has a lower loss?

With default setting (window=10, batch_size=1, epochs=10), FNG model generates loss rate of 0.1285 while the clsoing prices model generated loss rate of only 0.0562, considerably lower.


Hyperparameter tuning FNG model:
- increasing epochs from 10 to 30 lowered lower loss rates from 0.093 to 0.089 
- increasing number_units from 10 to 20 increased loss rate from 0.098 to 0.1056
- increasing batch size from 1 to 100 reduced loss rate from 0.102 tp 0.0802


Which model tracks the actual values better over time?

The closing prices model tracks actual values better, especially when window size is reduced to 1. While there is still significant discrepancy, the predicted trend matches actual upward trend.


Which window size works best for the model?

Both models seem to generate a better fitting prediction curve with a window of 1 (especially the closing prices model) which seems to suggest that any trend data from windows >1 do not seem to add value.