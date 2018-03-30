let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template

function getImages(){
    paths = ['{{ images }}'];
    alert(paths)
}
getImages()