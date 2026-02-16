# HP-PREDICTIONS
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>House Price Prediction Project</title>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background: #f4f6f9;
    line-height: 1.6;
}

header {
    background: #1e3c72;
    color: white;
    padding: 20px;
    text-align: center;
}

section {
    padding: 30px;
    margin: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

h2 {
    color: #1e3c72;
    border-bottom: 2px solid #1e3c72;
    padding-bottom: 5px;
}

ul {
    margin-left: 20px;
}

code {
    background: #eee;
    padding: 4px 6px;
    border-radius: 4px;
}

footer {
    text-align: center;
    padding: 20px;
    background: #1e3c72;
    color: white;
}
</style>
</head>

<body>

<header>
    <h1>🏠 House Price Prediction Project</h1>
    <p>Machine Learning Web Application using Custom Linear Regression & Flask</p>
</header>

<section>
<h2>📌 Project Overview</h2>
<p>This project predicts house prices using a custom-built Linear Regression model and deploys it using Flask and Render.</p>

<ul>
<li>Real-time house price prediction</li>
<li>17 input features</li>
<li>Custom Linear Regression using SVD</li>
<li>Deployed on Render</li>
</ul>
</section>

<section>
<h2>📊 Dataset Description</h2>
<ul>
<li><strong>Dataset:</strong> House Sales in King County, USA</li>
<li><strong>Total Records:</strong> 21,613</li>
<li><strong>Features:</strong> 18 columns</li>
<li><strong>Time Period:</strong> May 2014 – May 2015</li>
</ul>
</section>

<section>
<h2>💻 Technology Stack</h2>
<ul>
<li><strong>Backend:</strong> Python, Flask, Scikit-learn, NumPy, Pandas</li>
<li><strong>Frontend:</strong> HTML5, CSS3</li>
<li><strong>Deployment:</strong> Render, Gunicorn</li>
<li><strong>Version Control:</strong> Git & GitHub</li>
</ul>
</section>

<section>
<h2>⚙ Implementation Steps</h2>

<h3>1️⃣ Environment Setup</h3>
<pre>
python -m venv venv
venv\Scripts\activate
pip install flask numpy pandas scikit-learn gunicorn
</pre>

<h3>2️⃣ Model Training</h3>
<ul>
<li>Data preprocessing</li>
<li>Feature engineering</li>
<li>Train custom Linear Regression using SVD</li>
<li>Evaluate using RMSE and R²</li>
<li>Save model using pickle</li>
</ul>

<h3>3️⃣ Run Application</h3>
<pre>
python app.py
</pre>

<p>Access at: <code>http://localhost:5000</code></p>

</section>

<section>
<h2>🧠 Model Development</h2>
<p><strong>Model Used:</strong> Custom Linear Regression</p>
<ul>
<li>Singular Value Decomposition (SVD)</li>
<li>Pseudo-inverse calculation</li>
<li>Manual R² & RMSE computation</li>
</ul>
</section>

<section>
<h2>🚀 Deployment Process</h2>

<ul>
<li>Push project to GitHub</li>
<li>Create Web Service on Render</li>
<li>Build Command: <code>pip install -r requirements.txt</code></li>
<li>Start Command: <code>gunicorn app:app</code></li>
</ul>

<p><strong>Live URL:</strong> https://house-price-predictor.onrender.com</p>
</section>

<section>
<h2>📈 Sample Output</h2>

<p><strong>Input:</strong></p>
<ul>
<li>Bedrooms: 4</li>
<li>Bathrooms: 4</li>
<li>Sqft Living: 1340</li>
<li>Year Built: 1995</li>
</ul>

<p><strong>Output:</strong></p>
<code>Estimated House Price: $1,275,464.67</code>

</section>

<section>
<h2>🛠 Challenges & Solutions</h2>

<ul>
<li><strong>Feature Encoding:</strong> Used manual label encoding</li>
<li><strong>Model Persistence:</strong> Saved using pickle</li>
<li><strong>Deployment Errors:</strong> Fixed missing dependencies</li>
</ul>

</section>

<section>
<h2>🔮 Future Enhancements</h2>

<ul>
<li>Random Forest & Gradient Boosting</li>
<li>Neural Networks</li>
<li>Data Visualization Dashboard</li>
<li>Database Integration</li>
<li>Docker Deployment</li>
</ul>

</section>

<section>
<h2>🏁 Conclusion</h2>
<p>This project demonstrates a complete machine learning pipeline from data preprocessing to web deployment.</p>
</section>

<footer>
<p>👨‍💻 Project By: A. Nikhil Goud</p>
<p>Last Updated: 10-02-2026</p>
</footer>

</body>
</html>
