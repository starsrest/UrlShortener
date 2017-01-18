from flask import Flask, render_template, request, flash, redirect, url_for
from converter import encode, decode
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

app.secret_key = 'allyourbasearebelongtous'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        _longurl = request.form['longurl']

        if _longurl:
            conn = sqlite3.connect('/var/www/FlaskApps/UrlShortener/shortener_database.sqlite3')
            cur = conn.cursor()

            # Get tuple index of table
            ti = 0
            cur.execute('SELECT COUNT(*) FROM URLtable')
            for i in cur:
                ti = i[0] + 1
            
            # Convert base 10 index number into base 62 number which is a part of short url
            su = encode(ti)

            cur.execute('INSERT INTO URLtable (tableindex, shorturl, longurl) VALUES (?, ?, ?)', (ti, su, _longurl))
            conn.commit()

            flash('Your short URL: 52.14.45.104/%s' % (su))
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/<su>')
def fetchlongurl(su):
    conn = sqlite3.connect('/var/www/FlaskApps/UrlShortener/shortener_database.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT longurl FROM URLtable WHERE shorturl=?', (su, ))
    url = cur.fetchone()

    if url:
        result = ''
        for i in url:
            result = i
        if 'http://' in result or 'https://' in result:
            return redirect(result)
        else:
            return redirect('http://%s' % (result))
    else:
        flash('Invalid Short URL!')
        return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
