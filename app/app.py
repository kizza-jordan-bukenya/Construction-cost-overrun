import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Construction Cost Overrun Predictor",
    page_icon="🏗️",
    layout="wide"
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("construction_cost_overrun_model.pkl")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏗️ Construction Cost Overrun Predictor")

st.write(
    """
    Predict the expected percentage cost overrun of a construction project
    using project characteristics, planned costs, resources, changes,
    quality indicators, safety factors, risk, and environmental conditions.
    """
)

st.info(
    "This machine learning model is designed as a decision-support tool "
    "for assessing construction cost-overrun risk. Predictions are estimates "
    "and should be considered alongside professional Quantity Surveying "
    "judgement and project information."
)


# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

st.header("Project Information")

col1, col2, col3 = st.columns(3)

with col1:
    project_type = st.selectbox(
        "Project Type",
        ["Building", "Infrastructure", "Remodeling"]
    )

with col2:
    structure_type = st.selectbox(
        "Structure Type",
        ["RC", "Steel", "Composite", "SRC", "Masonry", "Concrete"]
    )

with col3:
    contract_type = st.selectbox(
        "Contract Type",
        ["DBB", "Design-Build", "Turnkey", "CM-at-Risk"]
    )


# --------------------------------------------------
# PROJECT SIZE & PLANNING
# --------------------------------------------------

st.header("Project Size & Planning")

col1, col2, col3 = st.columns(3)

with col1:
    area = st.number_input(
        "Project Area",
        min_value=500,
        max_value=500000,
        value=25000,
        step=500
    )

with col2:
    floor_count = st.number_input(
        "Number of Floors",
        min_value=1,
        max_value=49,
        value=10,
        step=1
    )

with col3:
    planned_duration = st.number_input(
        "Planned Duration (days)",
        min_value=90,
        max_value=2190,
        value=300,
        step=10
    )


# --------------------------------------------------
# COST & RESOURCES
# --------------------------------------------------

st.header("Cost & Resources")

col1, col2, col3 = st.columns(3)

with col1:
    planned_cost = st.number_input(
        "Planned Cost (UGX)",
        min_value=1000000,
        value=1000000000,
        step=10000000
    )

with col2:
    labor_total = st.number_input(
        "Total Labour",
        min_value=10,
        max_value=567,
        value=80,
        step=1
    )

with col3:
    equipment_count = st.number_input(
        "Equipment Count",
        min_value=1,
        max_value=65,
        value=5,
        step=1
    )

resource_utilization = st.slider(
    "Resource Utilization",
    min_value=0.40,
    max_value=0.99,
    value=0.73,
    step=0.01
)


# --------------------------------------------------
# CHANGE ORDERS & DEFECTS
# --------------------------------------------------

st.header("Changes & Quality")

col1, col2, col3 = st.columns(3)

with col1:
    change_order_count = st.number_input(
        "Change Order Count",
        min_value=0,
        max_value=11,
        value=2,
        step=1
    )

with col2:
    change_cost_ratio = st.number_input(
        "Change Cost Ratio",
        min_value=0.0,
        max_value=0.1847,
        value=0.03,
        step=0.01
    )

with col3:
    defect_count = st.number_input(
        "Defect Count",
        min_value=0,
        max_value=19,
        value=4,
        step=1
    )

col1, col2 = st.columns(2)

with col1:
    defect_severity = st.slider(
        "Defect Severity",
        min_value=0.01,
        max_value=0.95,
        value=0.32,
        step=0.01
    )

with col2:
    repair_cost = st.number_input(
        "Repair Cost (UGX)",
        min_value=0,
        max_value=30345300000,
        value=0,
        step=1000000
    )


# --------------------------------------------------
# RISK & ENVIRONMENT
# --------------------------------------------------

st.header("Risk & Environmental Conditions")

col1, col2, col3 = st.columns(3)

with col1:
    accident_count = st.number_input(
        "Accident Count",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

with col2:
    risk_level = st.slider(
        "Risk Level",
        min_value=0.0,
        max_value=0.5034,
        value=0.20,
        step=0.01
    )

with col3:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=-10.0,
        max_value=40.0,
        value=15.0,
        step=1.0
    )

rainfall = st.number_input(
    "Rainfall",
    min_value=0.0,
    max_value=350.0,
    value=50.0,
    step=5.0
)


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------


st.divider()

if st.button("🔮 Predict Cost Overrun", type="primary"):

    input_data = pd.DataFrame([{
        "Project_Type": project_type,
        "Area": area,
        "Floor_Count": floor_count,
        "Structure_Type": structure_type,
        "Contract_Type": contract_type,
        "Planned_Cost": planned_cost,
        "Planned_Duration": planned_duration,
        "Labor_Total": labor_total,
        "Equipment_Count": equipment_count,
        "Resource_Utilization": resource_utilization,
        "Change_Order_Count": change_order_count,
        "Change_Cost_Ratio": change_cost_ratio,
        "Defect_Count": defect_count,
        "Defect_Severity": defect_severity,
        "Repair_Cost": repair_cost,
        "Accident_Count": accident_count,
        "Risk_Level": risk_level,
        "Temperature": temperature,
        "Rainfall": rainfall
    }])

    prediction = model.predict(input_data)[0]

    overrun_percentage = prediction * 100

    st.success(
        f"### Predicted Cost Overrun: {overrun_percentage:.2f}%"
    )

    st.write(
        f"The model estimates that the project's final cost may be "
        f"approximately **{overrun_percentage:.2f}%** above the planned cost."
    )

    estimated_overrun_cost = planned_cost * prediction
    estimated_actual_cost = planned_cost + estimated_overrun_cost

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Estimated Overrun Amount",
            f"UGX {estimated_overrun_cost:,.0f}"
        )

    with col2:
        st.metric(
            "Estimated Final Project Cost",
            f"UGX {estimated_actual_cost:,.0f}"
        )

    st.caption(
        "The estimated final project cost is calculated as planned cost "
        "plus the model's predicted cost overrun."
    )

    if prediction < 0.10:
        st.info(
            "🟢 **Low predicted cost-overrun risk.** "
            "The estimated overrun is below 10% of the planned project cost."
        )

    elif prediction < 0.25:
        st.warning(
            "🟡 **Moderate predicted cost-overrun risk.** "
            "The estimated overrun is between 10% and 25% of the planned cost."
        )

    else:
        st.error(
            "🔴 **High predicted cost-overrun risk.** "
            "The estimated overrun is 25% or more of the planned cost. "
            "Further cost and risk review is recommended."
        )
# --------------------------------------------------
# MODEL PERFORMANCE
# --------------------------------------------------

st.divider()

st.header("📊 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("R² Score", "0.845")

with col2:
    st.metric("MAE", "3.10 percentage points")

with col3:
    st.metric("RMSE", "3.96 percentage points")

st.caption(
    "Performance was evaluated on a held-out test set of 20,000 projects. "
    "The R² score indicates that the model explains approximately 84.5% "
    "of the variation in the test-set cost-overrun values."
)