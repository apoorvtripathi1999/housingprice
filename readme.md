# Housing Price Prediction Dashboard

A comprehensive machine learning project that predicts housing prices using multiple ensemble techniques and provides an interactive web dashboard for model comparison and predictions.

## Preview
[Link](https://predictprice-9qtr.onrender.com)
## 🏠 Project Overview

This project implements a complete machine learning pipeline for housing price prediction, featuring:

- **Data preprocessing and feature engineering** with automated null handling and outlier detection
- **Multiple ML models** including Linear Regression, Bagging, Voting Ensemble, and Gradient Boosting
- **MLflow integration** for experiment tracking and model versioning
- **Interactive Streamlit dashboard** for model comparison and batch predictions
- **Docker containerization** for easy deployment

## 📊 Dataset

The project uses the Ames Housing dataset with **81 features** including:
- **Numerical features**: Lot area, square footage, year built, etc.
- **Categorical features**: Neighborhood, house style, quality ratings, etc.
- **Target variable**: SalePrice (house prices in USD)

## 🔬 Machine Learning Workflow

### 1. Data Preprocessing (`house-price-prediction.ipynb`)

#### **Data Cleaning & Null Handling**
- **Automated null detection**: Identifies columns with >10% null values for removal
- **Smart imputation**: 
  - Categorical features: Mode imputation
  - Numerical features: Median imputation
- **Feature type identification**: Automated separation of numerical and categorical columns

#### **Feature Engineering**
- **One-Hot Encoding**: Converts categorical variables to numerical format
- **Scaling & Normalization**: 
  - StandardScaler for initial normalization
  - PowerTransformer for distribution normalization
- **Outlier Handling**: IQR-based capping to reduce extreme values
- **Duplicate Feature Removal**: Eliminates redundant columns
- **Feature Selection**:
  - Correlation-based removal (threshold: 0.75)
  - Variance threshold filtering (threshold: 0.05)

#### **Model Development Pipeline**

1. **Base Model (Linear Regression)**
   - RMSE: 46,685.57
   - R² Score: 0.69
   - Simple baseline for comparison

2. **Enhanced Linear Regression**
   - Applied preprocessing pipeline
   - RMSE: 34,980.45
   - R² Score: 0.83
   - Cross-validation score: 0.78

3. **Ensemble Methods**
   - **Bagging Regressor**: RMSE: 26,240.55, R²: 0.90
   - **Voting Ensemble** (LR + Random Forest + KNN): RMSE: 27,983.37, R²: 0.89
   - **Gradient Boosting**: RMSE: 26,277.26, R²: 0.90

### 2. Model Performance Comparison

| Model | RMSE | R² Score | Cross-Val Score |
|-------|------|----------|-----------------|
| Base Model | 46,685.57 | 0.69 | - |
| Linear Regression | 34,980.45 | 0.83 | 0.78 |
| Bagging Regressor | 26,240.55 | 0.90 | 0.79 |
| Voting Ensemble | 27,983.37 | 0.89 | 0.85 |
| Gradient Boosting | 26,277.26 | 0.90 | 0.85 |

### 3. MLflow Integration

- **Experiment tracking** for all model iterations
- **Model versioning** and artifact storage
- **Metrics logging** (RMSE, R², Cross-validation scores)
- **Parameter tracking** for hyperparameter optimization

## 🚀 Streamlit Dashboard

### **Multi-Page Application Structure**

#### **1. Prediction Tool** (`pages/prediction.py`)
- **Model Selection**: Choose from 5 trained models
- **Template Downloads**: 
  - Base model template (simplified features)
  - Full model template (all engineered features)
- **Batch Prediction**: Upload CSV files for bulk predictions
- **Result Export**: Download predictions as CSV

#### **2. Model Performance** (`pages/performance.py`)
- **Interactive Visualizations**: Plotly charts for metric comparison
- **Metrics Comparison**: R² Score, RMSE, Cross-validation scores
- **Parameter Analysis**: Model hyperparameters comparison table
- **Real-time Updates**: Dynamic charts based on selected metrics

#### **3. Feature Documentation** (`pages/document.py`)
- **Complete Feature Guide**: Detailed descriptions of all 81 features
- **Data Dictionary**: Categorical value mappings and explanations
- **Reference Material**: For understanding input data requirements

### **Key Features**
- **Responsive Design**: Works on desktop and mobile devices
- **User-Friendly Interface**: Intuitive navigation and clear instructions
- **Error Handling**: Graceful handling of invalid inputs
- **Template System**: Pre-formatted CSV templates for easy data preparation

## 🛠️ Technical Stack

### **Core Technologies**
- **Python 3.13**: Main programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **MLflow**: Experiment tracking and model management

### **Visualization & UI**
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Matplotlib/Seaborn**: Statistical plotting

### **Deployment**
- **Docker**: Containerization
- **Cloudpickle**: Model serialization

## 📁 Project Structure

```
housingrates/
├── app.py                          # Main Streamlit application
├── house-price-prediction.ipynb    # ML pipeline notebook
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container configuration
├── data/                          # Dataset files
│   ├── train.csv                  # Training data
│   ├── test.csv                   # Test data
│   ├── template.csv               # Full model template
│   └── basetemplate.csv           # Base model template
├── models/                        # Trained model files
│   ├── basemodel.cloudpickle      # Base linear regression
│   ├── lrmodel.cloudpickle        # Enhanced linear regression
│   ├── baggingmodel.cloudpickle   # Bagging regressor
│   ├── votingmodel.cloudpickle    # Voting ensemble
│   ├── boostingmodel.cloudpickle  # Gradient boosting
│   └── run_dict.cloudpickle       # MLflow experiment data
├── pages/                         # Streamlit pages
│   ├── prediction.py              # Prediction interface
│   ├── performance.py             # Model comparison
│   └── document.py                # Feature documentation
├── basetemplates/                 # Template files
│   ├── basetemplate.csv           # Base model template
│   ├── template.csv               # Full model template
│   └── data_description.txt       # Feature descriptions
├── mlruns/                        # MLflow experiment data
└── mlartifacts/                   # MLflow model artifacts
```

## 🚀 Getting Started

### **Prerequisites**
- Python 3.13+
- Docker (optional, for containerized deployment)

### **Installation**

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd housingrates
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - Open your browser to `http://localhost:8501`
   - Navigate between pages using the sidebar

### **Docker Deployment**

1. **Build the Docker image**
   ```bash
   docker build -t housing-prediction .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 housing-prediction
   ```

## 📈 Usage Guide

### **Making Predictions**

1. **Navigate to Prediction Tool**
2. **Select a model** from the dropdown menu
3. **Download the appropriate template**:
   - Use `basetemplate.csv` for Base Model
   - Use `template.csv` for other models
4. **Fill in your data** following the template format
5. **Upload the CSV file** and download predictions

### **Comparing Models**

1. **Go to Model Performance page**
2. **Select a metric** to visualize (R², RMSE, Cross-validation)
3. **View interactive charts** comparing all models
4. **Check the parameters table** for hyperparameter details

### **Understanding Features**

1. **Visit Feature Documentation page**
2. **Browse the complete feature dictionary**
3. **Understand categorical value mappings**
4. **Reference for data preparation**

## 🔧 Model Training

To retrain models or experiment with new approaches:

1. **Open the Jupyter notebook**: `house-price-prediction.ipynb`
2. **Run cells sequentially** to execute the full pipeline
3. **Modify parameters** in the notebook for experimentation
4. **MLflow will automatically track** new experiments

## 📊 Key Insights

### **Best Performing Model**
- **Gradient Boosting Regressor** achieves the best balance of performance and stability
- **RMSE: 26,277.26** (lowest error)
- **R² Score: 0.90** (explains 90% of variance)
- **Cross-validation: 0.85** (good generalization)

### **Feature Engineering Impact**
- **Outlier handling** reduced RMSE by ~5,000
- **Feature selection** improved model stability
- **Power transformation** enhanced linear model performance

### **Ensemble Benefits**
- **Bagging and Boosting** significantly outperform single models
- **Voting ensemble** provides good balance between performance and interpretability
- **Cross-validation scores** indicate robust generalization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Ames Housing dataset for providing comprehensive housing data
- Scikit-learn team for excellent ML tools
- Streamlit for the intuitive web framework
- MLflow for experiment tracking capabilities
