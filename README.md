# king-gizzard-discog
This webapp was created for the University of Florida course, Advanced Web Apps. :cowboy_hat_face:
## What the app does
This app contains pages that detail each album in King Gizzard and the Lizard Wizard's discography. Each page contains the same information about an album: 
-Title
-Release year
-Runtime (in minutes and seconds)
-Score on music review site, Rate Your Music
These pages also provide a link to the app's index.htlm page, which lists each album in order. It also has a very cool photo of the band.
## How I did it
Starting with a csv file, I compiled the above facts about each album in the band's discography as well as the file names of the album art. I then copied a module that turned my csv data into a python dictionary. This app was built as a flask app, which used a template I created (```album.html```) to fill in each album page. Jinja directives allowed me to pull the keys and values from my dictionary into the template. Its also important to add that for loop wrote all the album titles and links to their respective pages into a list on the ```index.html``` page. 
## Some struggles I had
I ran into trouble trying to combine ```flask-bootstrap``` and CSS on my pages. The bootstrap overrode any CSS I tried to link or style inline. Unfortunately, I had to fall back on an ugly white background and standard link hover effects.
Also, I originally tried to deploy the app via NameCheap, but ran into technical difficulty there. Instead, I used ```flask-freeze``` to bake in my templates. I then uploaded my build to my domain using FileZilla.
That's all! I hope you learned a little about this goofy band. They have a new project dropping in April.
