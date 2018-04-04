let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template
//https://api.jquery.com/data/
//https://stackoverflow.com/questions/21626048/unable-to-pass-jinja2-variables-into-javascript-snippet
//http://jquery.malsup.com/cycle2/api/
//http://api.jquery.com/appendto/
//https://stackoverflow.com/questions/19504018/show-seconds-on-input-type-date-local-in-chrome
function getImages(){
    latestimages = $('#path_to_latestimages').data();
    datetimeimages = $('#path_to_datetimeimages').data();

    for (let i=0; i < latestimages.paths.length; i++){
        temp = latestimages.paths[i].path;
        image = temp.substring(55);
        test = $("<img src='/static/uploads/" + image + "'>").appendTo('.cycle-slideshow');
    }

    for (let i=0; i < datetimeimages.paths.length; i++){
        temp = datetimeimages.paths[i].path;
        image = temp.substring(55);
        test = $("<img src='/static/uploads/" + image + "'>").appendTo('.slideshow');
    }
    $('.slideshow').cycle();

}
getImages()
