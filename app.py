from flask import Flask, render_template, request
from model import predict_cancer, get_accuracy, generate_pca_plot

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    radius = float(request.form['radius'])
    texture = float(request.form['texture'])
    perimeter = float(request.form['perimeter'])
    area = float(request.form['area'])

    features = [radius, texture, perimeter, area]

    result = predict_cancer(features)
    acc = get_accuracy()

    generate_pca_plot(features)

    return render_template(
        'index.html',
        prediction_text=result,
        accuracy_text=acc,
        show_graph=True
    )


if __name__ == "__main__":
    app.run(debug=True)