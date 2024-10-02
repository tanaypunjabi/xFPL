# TODO List

This is the list of tasks to be completed for the **xFPL** project. The tasks are organized into sections based on the project’s phases (e.g., data collection, model development, frontend integration, testing, etc.). Each task is prioritized and can be marked as complete when done.

---

## 1. Data Collection & Preprocessing
- [x] Identify and download historical FPL data from [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League)
- [ *in progress* ] Write ETL scripts to load raw data into the system
- [ *in progress* ] Clean and normalize player data (handle missing values, standardize formats)
<!-- - [ ] Extract and preprocess fixture data for upcoming gameweeks -->
- [ *in progress* ] Engineer key features from raw data (e.g., average points, fixture difficulty)
<!-- - [ ] Integrate external football data (optional: xG, xA, etc.) -->

## 2. Model Development
- [ ] Perform exploratory data analysis (EDA) on player statistics
- [ ] Develop initial regression model to predict points in next gameweek
    - [ ] Select features for model training
    - [ ] Tune hyperparameters (e.g., number of trees in Random Forest)
- [ ] Implement classification models (for binary outcomes like clean sheets, goals)
- [ ] Evaluate model performance (use cross-validation, RMSE, MAE)
- [ ] Optimize models based on evaluation results

## 3. Recommendation System
- [ *in progress* ] Outline/Finalize system functionalities
- [ ] Implement logic to generate transfer and captaincy recommendations
- [ ] Test recommendation logic with historical data
- [ ] Implement functionality to update recommendations based on real-time data
- [ ] Add logic for bench and squad rotation suggestions

## 4. Frontend Integration
- [ ] Design basic UI to display player recommendations
<!-- - [ ] Implement interactive frontend (React, Flask, or other technology) -->
- [ ] Integrate model outputs with frontend to provide real-time recommendations
- [ ] Test frontend with multiple scenarios

## 5. Testing & Evaluation
<!-- - [ ] Write unit tests for data pipeline (`tests/test_data_pipeline.py`)
- [ ] Write unit tests for model (`tests/test_models.py`) -->
- [ ] Perform offline simulations with historical FPL seasons
- [ ] Conduct real-time testing during current FPL season
- [ ] Collect feedback from real FPL users
- [ ] Compare performance with existing tools (e.g., FPL Scout, Fantasy Football Hub)

## 6. Documentation & Finalization
- [x] Create `README.md` for repository
<!-- - [ ] Document setup instructions in `docs/setup_guide.md` -->
- [ ] Add model explanation and feature descriptions in documentation
- [ ] Write final project report/presentation

<!-- ## 7. Future Enhancements (Optional)
- [ ] Integrate advanced metrics like expected goals (xG) or expected assists (xA)
- [ ] Build a more robust user feedback system for recommendations
- [ ] Explore additional machine learning models (e.g., deep learning models)
- [ ] Extend the system to other fantasy football leagues (e.g., Champions League, La Liga) -->

---

## Notes
- Keep track of weekly progress.
- Prioritize essential tasks for initial release.
- Move completed tasks to the top of the list to reflect progress.