# 🎓 Student Performance Predictor

A modern Flask-based web application that predicts student performance using machine learning. The project features a clean, responsive UI with real-time score validation, progress indicators, and instant performance feedback for an enhanced user experience.

---

## 🚀 Features

* ✅ Predicts student performance based on academic and demographic inputs
* 🎯 Real-time validation for reading & writing scores
* 📊 Dynamic progress bars reflecting score range (0–100)
* 🧠 Live performance indicator: Low / Medium / High
* 💎 Modern glassmorphism UI with Bootstrap 5
* ⚡ Instant prediction powered by a machine learning backend
* 📱 Fully responsive design for all screen sizes

---

## 🛠 Tech Stack

| Layer       | Technology                         |
| ----------- | ---------------------------------- |
| Frontend    | HTML, CSS, Bootstrap 5, JavaScript |
| Backend     | Flask (Python)                     |
| ML Pipeline | Scikit-learn, Pandas, NumPy        |
| Styling     | Custom CSS (Glass UI)              |

---

## 📂 Project Structure

```
student-performance-predictor/
│
├── app.py
├── src/
│   └── pipeline/
│       └── predict_pipeline.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── home.html
├── static/
│   └── styles.css
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧪 How It Works

1. User fills in student details and scores.
2. JavaScript validates inputs in real-time.
3. Flask sends the data to the ML prediction pipeline.
4. The model returns a predicted performance value.
5. Result is displayed along with visual indicators.

---

## 📌 Input Parameters

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score (0–100)
* Writing Score (0–100)

---

## 🎨 UI Highlights

* Glass-style cards and smooth gradients
* Equal-height feature tiles
* Real-time feedback components
* Clean typography and modern spacing

---

## 📈 Future Improvements

* Add user authentication
* Export prediction reports as PDF
* Store prediction history
* Add more performance metrics
* Integrate advanced analytics dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature/awesome-feature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 🙌 Acknowledgements

* Flask documentation
* Scikit-learn community
* Bootstrap UI framework
* Open-source contributors

---

### ⭐ If you like this project, consider giving it a star on GitHub!

Happy coding! 🚀
