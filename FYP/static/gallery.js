let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template
//https://api.jquery.com/data/
//https://stackoverflow.com/questions/21626048/unable-to-pass-jinja2-variables-into-javascript-snippet
function getImages(){
    paths = $('#path_to_images').data();
}
getImages()