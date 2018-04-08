let paths = [];


//https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template
//https://api.jquery.com/data/
//https://stackoverflow.com/questions/21626048/unable-to-pass-jinja2-variables-into-javascript-snippet
//http://jquery.malsup.com/cycle2/api/
//http://api.jquery.com/appendto/
//https://stackoverflow.com/questions/19504018/show-seconds-on-input-type-date-local-in-chrome
//http://jquery.malsup.com/cycle2/demo/non-image.php
function getImages(){
    //Retrieve the JSON query's from python using html and jinja2.
    latestImages = $('#path_to_latestimages').data();
    datetimeImages = $('#path_to_datetimeimages').data();

    let mean = 0;
    let latestMean = 0;
    let dateMean = 0;
    if(latestImages.paths.length != 0){
        //calculate the mean number of people for both slideshows
        for (let i=0; i < latestImages.paths.length; i++){
            number_of_people = latestImages.paths[i].number_of_people;
            mean = mean + number_of_people;
        }
        latestMean = mean/latestImages.paths.length;
        mean = 0;
    }
    if(datetimeImages.paths.length != 0){
        for (let i=0; i < datetimeImages.paths.length; i++){
            number_of_people = datetimeImages.paths[i].number_of_people;
            mean = mean + number_of_people;
        }
        dateMean = mean/datetimeImages.paths.length;
    }
    //This for loop fills the left slideshow with the latest images.
    for (let i=0; i < latestImages.paths.length; i++){
        temp = latestImages.paths[i].path;
        image = temp.substring(55); //removing everything from the string except the filename and extension.
        date = latestImages.paths[i].date_time;
        number_of_people = latestImages.paths[i].number_of_people;

        $("<img src='/static/uploads/" + image + "'>").appendTo('.cycle-slideshow');
        $("<p>Date: "+date+ " Number of People: "+ number_of_people+ " Average: "+ latestMean+"</p>").appendTo('.latestTextSlideshow');
    }
    $('.latestTextSlideshow').cycle();

    //This for loop fills the right slideshow with the selected date time images.
    for (let i=0; i < datetimeImages.paths.length; i++){
        temp = datetimeImages.paths[i].path;
        image = temp.substring(55);
        date = datetimeImages.paths[i].date_time;
        number_of_people = datetimeImages.paths[i].number_of_people;

        $("<img src='/static/uploads/" + image + "'>").appendTo('.slideshow');
        $("<p>Date: "+date+ " Number of People: "+ number_of_people+" Average: "+ dateMean+"</p>").appendTo('.textSlideshow');
    }
    $('.slideshow').cycle();
    $('.textSlideshow').cycle();

}
getImages()
