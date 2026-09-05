🏗️ Construction Cost Overrun Prediction

A machine learning project that predicts the expected **percentage cost overrun of construction projects** using project characteristics, planned costs, resources, changes, quality indicators, safety factors, risk, and environmental conditions.

The project combines **Quantity Surveying knowledge with Data Science and Machine Learning** to demonstrate how predictive analytics can support construction cost management and risk assessment.

Live Application

**Try the model online:**

https://construction-cost-overrun-dqrjkuavvfxf5avfkjkvlu.streamlit.app/


Project Overview

Cost overruns are a major challenge in construction projects. A project may exceed its original budget because of factors such as changes, resource constraints, project risk, defects, accidents, and environmental conditions.

This project develops a regression-based machine learning model to estimate the expected **Cost Overrun** of a construction project.

The predicted value is converted into a percentage and used to provide a simple risk interpretation:

* 🟢 **Low Risk:** Less than 10%
* 🟡 **Moderate Risk:** 10%–25%
* 🔴 **High Risk:** 25% or more

The application also estimates:

* Expected cost overrun amount
* Estimated final project cost
* Predicted cost-overrun percentage


Objectives

The main objectives of this project were to:

1. Explore construction project data.
2. Identify factors associated with cost overruns.
3. Prepare numerical and categorical features for machine learning.
4. Develop multiple regression models.
5. Compare model performance.
6. Tune the best-performing model.
7. Analyse prediction errors and feature importance.
8. Deploy the final model as an interactive web application.



Quantity Surveying Relevance

This project demonstrates the application of Data Science to Quantity Surveying.

A Quantity Surveyor is involved in areas such as:

* Cost planning
* Cost control
* Budget management
* Risk assessment
* Variation/change management
* Construction project monitoring

Machine learning can complement these activities by identifying patterns in historical project information and providing estimates that can support professional decision-making.

The model is therefore intended as a **decision-support tool**, rather than a replacement for professional Quantity Surveying judgement.


Dataset

The project uses an integrated construction dataset containing **100,000 project records and 24 variables**.

The dataset contains information relating to:

* Project characteristics
* Planned costs
* Planned duration
* Labour
* Equipment
* Resource utilisation
* Change orders
* Change costs
* Defects
* Repairs
* Accidents
* Project risk
* Temperature
* Rainfall

The target variable is:

`Cost_Overrun`

It is calculated as:

`(Actual Cost - Planned Cost) / Planned Cost`

For example:

* `0.10` = 10% cost overrun
* `0.25` = 25% cost overrun
* `0.55` = 55% cost overrun

Important note

The dataset is used as a machine-learning project dataset and should not be interpreted as a verified database of actual Ugandan construction projects or market prices.

The application displays project costs in **UGX as a project assumption** for demonstration and Quantity Surveying context.


Features Used

The final model uses 19 input features.

 Categorical Features

* Project Type
* Structure Type
* Contract Type

 Numerical Features

* Area
* Floor Count
* Planned Cost
* Planned Duration
* Labour Total
* Equipment Count
* Resource Utilisation
* Change Order Count
* Change Cost Ratio
* Defect Count
* Defect Severity
* Repair Cost
* Accident Count
* Risk Level
* Temperature
* Rainfall

 Features excluded from the model

The following variables were excluded to reduce data leakage and ensure that the prediction does not directly depend on information that would only be known after the project outcome:

* Project ID
* Actual Cost
* Actual Duration
* Schedule Delay
* Cost Overrun



 Machine Learning Models

Three regression models were evaluated:

 1. Linear Regression

Baseline model used to establish an initial performance benchmark.

**Test-set results:**

* R²: **0.8391**
* MAE: **0.0322**
* RMSE: **0.0404**

 2. Random Forest Regressor

A tree-based ensemble model capable of capturing nonlinear relationships between construction project variables.

**Test-set results:**

* R²: **0.8445**
* MAE: **0.0311**
* RMSE: **0.0397**

 3. Gradient Boosting Regressor

A boosting-based ensemble model used as another nonlinear regression benchmark.

**Test-set results:**

* R²: **0.8407**
* MAE: **0.0318**
* RMSE: **0.0402**


 Final Model

The final model is a **tuned Random Forest Regressor**.

Hyperparameter search was performed using `RandomizedSearchCV`.

The selected configuration was:

* `n_estimators = 200`
* `max_depth = None`
* `min_samples_split = 2`
* `min_samples_leaf = 1`

### Final test-set performance

| Metric |     Result |
| ------ | ---------: |
| R²     | **0.8454** |
| MAE    | **0.0310** |
| RMSE   | **0.0396** |

The model was evaluated on a held-out test set containing **20,000 projects**.

An R² of approximately **0.845** means that the model explains about **84.5% of the variation in the test-set cost-overrun values**.



 Feature Importance

The Random Forest model identified the following variables among the most important predictive features:

| Feature                   | Importance |
| ------------------------- | ---------: |
| Risk Level                |     0.4368 |
| Change Cost Ratio         |     0.2440 |
| Project Type – Remodeling |     0.0650 |
| Project Type – Building   |     0.0579 |
| Contract Type – DBB       |     0.0298 |
| Resource Utilisation      |     0.0262 |
| Rainfall                  |     0.0221 |

The two strongest model features were:

* **Risk Level**
* **Change Cost Ratio**

Together, they represented approximately **68% of the Random Forest's built-in feature-importance measure**.

These results indicate predictive association, not causation. Because the dataset is synthetic/integrated, the relationships should be interpreted cautiously.



 Model Validation

A 5-fold cross-validation procedure was performed on the training data.

Random Forest cross-validation results produced an average R² of approximately:

**0.8389 ± 0.0024**

The relatively small variation between folds suggests that the model's performance was reasonably stable across the training folds.

The final test R² of **0.8454** was also close to the cross-validation performance.



 Example Predictions

The deployed application was tested using different project scenarios.

Example predictions included:

| Scenario               | Predicted Overrun | Interpretation |
| ---------------------- | ----------------: | -------------- |
| Lower-risk scenario    |            11.89% | Moderate       |
| Moderate-risk scenario |            27.53% | High           |
| High-risk scenario     |            53.49% | High           |

The application converts the predicted percentage into an estimated monetary overrun using the project's planned cost.



 Streamlit Application

The model has been deployed using Streamlit.

The application allows users to enter project information and receive:

1. Predicted cost overrun percentage
2. Estimated overrun amount
3. Estimated final project cost
4. Cost-overrun risk classification
5. Model performance information

### Live application

https://construction-cost-overrun-dqrjkuavvfxf5avfkjkvlu.streamlit.app/



 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Streamlit
* Git
* GitHub
* Git LFS
* Jupyter Notebook



 Project Structure


Construction-cost-overrun/
│
├── app/
│   ├── app.py
│   ├── construction_cost_overrun_model.pkl
│   └── requirements.txt
│
├── data/
│   ├── bim_ai_civil_engineering_dataset.csv
│   └── construction_integrated_dataset_100k_v2.csv
│
├── notebooks/
│   ├── Construction cost overrun prediction.ipynb
│   ├── Cost Overrun prediction.ipynb
│   └── data inspection1 .ipynb
│
├── .gitignore
├── .gitattributes
└── requirements.txt


The large `FPDSData.csv` file is intentionally excluded from the repository because of GitHub's individual file-size limitations.



 Running the Project Locally

Clone the repository:
git clone https://github.com/kizza-jordan-bukenya/Construction-cost-overrun.git

Move into the project directory:
cd Construction-cost-overrun


Create a virtual environment:


python -m venv .venv

Activate it on Windows:


.venv\Scripts\Activate.ps1


Install the dependencies:


pip install -r requirements.txt


Run the Streamlit application:


python -m streamlit run app/app.py


 Limitations

This project has several limitations:

* The dataset is synthetic/integrated rather than a verified collection of real construction projects.
* Model performance may differ substantially on real-world project data.
* Predictions should not be treated as guaranteed final project costs.
* The model identifies statistical patterns rather than proving causal relationships.
* Professional Quantity Surveying judgement remains necessary when interpreting predictions.
* Some project variables used by the model may not be available at the very beginning of a project.


 Future Improvements

Potential future development includes:

* Training on verified historical construction projects from Uganda.
* Incorporating historical construction material price indices.
* Adding inflation and exchange-rate variables.
* Including fuel-price information.
* Developing time-series material-price forecasting models.
* Creating separate early-stage and mid-project prediction models.
* Adding explainable AI techniques such as SHAP.
* Improving the Streamlit dashboard with interactive visualisations.
* Integrating project monitoring data for continuous risk prediction.



Author

Kizza Jordan Bukenya

Bachelor of Science in Quantity Surveying
Makerere University

Interested in the intersection of:

**Quantity Surveying × Data Science × Machine Learning × Construction Technology**


 Disclaimer

This application is an educational and portfolio project demonstrating the use of machine learning for construction cost-overrun prediction.

Predictions are estimates and should be considered alongside professional Quantity Surveying judgement, project documentation, market conditions, and other relevant project information.
