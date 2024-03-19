# PupML
Project to predict electric guitar pickup build spec and adjacent parameters using ML, GPT API, and various web development tools. Deliver as webapp.

Updates:
3/19/2024 - Start of database and ML
Use SQL Lite as database system due to relatively low dataset. Data is resistance, inductance, wire gauge, wind count, and magnet specs (gauss measured at bar / polepiece level, will be used to adjust inductance values at full charge)

Prep ML model, define relevant parameters to be trained on and what/how to predict them. Training data set, with validation/target dataset.

Use Scikit-learn and or other python libraries to preprocess data, train various ml models and evaluate performance. Train with validation techniques on target dataset to verify.
