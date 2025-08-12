
# Synthetic Project Management Dataset Analysis

This repository contains a synthetic dataset and an exploratory and predictive analysis aimed at demonstrating skills relevant to business analysis, project/program management, and data analytics. The data is **entirely fictional** yet structured to reflect plausible project management scenarios.

## Dataset

The dataset (`synthetic_project_data.csv`) consists of 200 projects with the following columns:

| Column | Description |
| ------ | ----------- |
| `project_id` | Unique identifier for each project |
| `team_size` | Number of people assigned to the project |
| `budget_k` | Project budget in thousands of dollars |
| `duration_months` | Planned duration of the project in months |
| `complexity_score` | Numeric score (1–10) representing project complexity |
| `methodology` | Project management methodology used (Agile, Waterfall, Hybrid) |
| `manager_experience_yrs` | Experience of the project manager in years |
| `num_changes` | Number of change requests during the project |
| `risk_score` | Numeric score (1–10) estimating project risk |
| `domain` | Domain/industry of the project (IT, Finance, Healthcare, Manufacturing, Retail) |
| `status` | Target variable indicating whether the project was Successful or Failed |

The target variable `status` is generated based on a logistic function combining various features such that higher risk, complexity, budget, and changes decrease the probability of success while higher team size and manager experience increase it. The values are still synthetic and should not be interpreted as real-world insights.

## Analysis Notebook

The Jupyter notebook (`analysis.ipynb`) performs:

- **Exploratory Data Analysis (EDA)**: understanding distributions, relationships, and key drivers of project outcomes through descriptive statistics and visualizations.
- **Predictive Modeling**: building and evaluating a classification model (e.g., Random Forest) to predict project success. Feature importances are visualized and model performance metrics are reported.

The notebook is organized into clear sections with narrative markdown, making it easy to follow the data exploration and modeling steps. Executing the notebook allows you to reproduce and extend the analysis.

## Usage

1. Clone this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the notebook:

```bash
jupyter notebook analysis.ipynb
```

Feel free to experiment with the data, modify the model, or explore additional visualizations. Since the dataset is synthetic, the primary focus is on showcasing analytical workflow rather than deriving actionable business recommendations.

## Requirements

See `requirements.txt` for the list of Python libraries needed.

## License

This project is released under the MIT License.
