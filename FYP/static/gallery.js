let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template
//https://api.jquery.com/data/
//https://stackoverflow.com/questions/21626048/unable-to-pass-jinja2-variables-into-javascript-snippet
//http://jquery.malsup.com/cycle2/api/
//http://api.jquery.com/appendto/
//https://stackoverflow.com/questions/19504018/show-seconds-on-input-type-date-local-in-chrome
function getImages(){
    paths = $('#path_to_images').data();
    paths = ['breadboard', 'Goals', 'daisychain'];
    for (let i=0; i < paths.length; i++){
        $("<img src='/static/uploads/" + paths[i] + ".jpg'>").appendTo('.cycle-slideshow');
        $("<img src='/static/uploads/" + paths[i] + ".jpg'>").appendTo('.slideshow');
    }
    $('.slideshow').cycle();
}
getImages()

/*
<a target="_blank" href="/static/uploads/">
    <img src="/static/uploads/test2.jpg" alt="image" width="300" height="200">
</a>

*/