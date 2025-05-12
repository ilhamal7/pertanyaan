from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html", "r") as file:
        content = file.read()
    
    content = content.replace("{{ url_for('static', filename='styles.css') }}", url_for('static', filename='styles.css'))
    content = content.replace("{{ url_for('static', filename='script.js') }}", url_for('static', filename='script.js'))

    return render_template_string(content)

@app.route('/submit', methods=['POST'])
def submit():
    hasil = {
        "Masih sayang?": request.form.get("q1"),
        "Kangen?": request.form.get("q2"),
        "Benci?": request.form.get("q3"),
        "Mau diajak jalan?": request.form.get("q4"),
        "Mau maafin kalo ada bebek jelek?": request.form.get("q5"),
        "Kalau aku masih sayang, gimana?": request.form.get("q6"),
        "Mau makan lele bareng?": request.form.get("q7"),
        "Mau ngopi bean lagi?": request.form.get("q8"),
    }

    if any(value is None for value in hasil.values()):
        return redirect(url_for('index'))

    # Print jawaban di terminal
    print("Jawaban ayangku:")
    for pertanyaan, jawaban in hasil.items():
        print(f"{pertanyaan}: {jawaban}")

    return f"<h2>Makasi udah jawab semua, aku sayang kamu banyak banyaakk banget❤️</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)