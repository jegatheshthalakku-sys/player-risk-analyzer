## How It Works

Player Data
↓
Churn Prediction
↓
Churn Risk
+
Chat Message
↓
Toxicity Detection
↓
Toxicity Risk
↓
Combined Player Risk

## Installation

Clone the repository:

git clone https://github.com/jegatheshthalakku-sys/player-risk-analyzer.git

cd player-risk-analyzer

Create virtual environment:

python3 -m venv venv

source venv/bin/activate

Install required packages:

pip install flask pandas scikit-learn joblib

## Run the Application

python3 app.py

Open your browser and visit:

http://127.0.0.1:5000

## Risk Calculation

The combined player risk score uses:

- 70% Churn Risk
- 30% Toxicity Risk

## Future Improvements

- Database integration
- Advanced NLP-based toxicity detection
- Player analytics dashboard
- Data visualization
- Cloud deployment

## Author

T Jegathesh

Computer Science and Business Systems Student