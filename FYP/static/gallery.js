let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template
//https://api.jquery.com/data/
//https://stackoverflow.com/questions/21626048/unable-to-pass-jinja2-variables-into-javascript-snippet
//http://jquery.malsup.com/cycle2/api/
//http://api.jquery.com/appendto/
//https://stackoverflow.com/questions/19504018/show-seconds-on-input-type-date-local-in-chrome
function getImages(){
    //Retrieve the JSON query's from python using html and jinja2.
    latestimages = $('#path_to_latestimages').data();
    datetimeimages = $('#path_to_datetimeimages').data();

    //This for loop fills the left slideshow with the latest images.
    for (let i=0; i < latestimages.paths.length; i++){
        temp = latestimages.paths[i].path;
        image = temp.substring(55); //removing everything from the string except the filename and extension.
        $("<img src='/static/uploads/" + image + "'>").appendTo('.cycle-slideshow');
    }

    //This for loop fills the right slideshow with the selected date time images.
    for (let i=0; i < datetimeimages.paths.length; i++){
        temp = datetimeimages.paths[i].path;
        image = temp.substring(55);
        $("<img src='/static/uploads/" + image + "'>").appendTo('.slideshow');
    }
    $('.slideshow').cycle();

}
getImages()
