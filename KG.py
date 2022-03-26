from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# call Bootstrap
Bootstrap(app)

# create a list of dicts from a CSV
album_list = convert_to_dict("KGAlbums.csv")

# create a list of tuples in which the first item is the number
# (Album) and the second item is the name (Title)
pairs_list = []
for p in album_list:
    pairs_list.append( (p['Album'], p['Title']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Album Index")

# second route

@app.route('/album/<num>')
def detail(num):
    try:
        album_dict = album_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for album: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('album.html', album=album_dict, ord=ord, the_title=album_dict['Title'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
