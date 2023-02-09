from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


if __name__ == '__main__':
    app.run()


response=requests.get('https://5ffcb43ea77c50001706cab8.mockapi.io/api/v1/students')

telebeler=response.json()

@app.route('/students')
def students():
    return render_template('students.html', students=telebeler)


@app.route('/students/<int:ind>')
def stud(ind):
    
    ttt= telebeler[ind]

    return render_template ('stud.html', stud=ttt)
    # return 'post %d' %ind


   