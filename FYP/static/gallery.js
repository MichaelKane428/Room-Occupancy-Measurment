let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template
//https://api.jquery.com/data/
//https://stackoverflow.com/questions/21626048/unable-to-pass-jinja2-variables-into-javascript-snippet
function getImages(){
    paths = $('#path_to_images').data();
    $('.cycle-slideshow').html("<img src='/static/uploads/" + "daisychain.jpg'>");
}
getImages()

/*
<a target="_blank" href="/static/uploads/">
    <img src="/static/uploads/test2.jpg" alt="image" width="300" height="200">
</a>

*/