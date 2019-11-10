console.log(tags);

var active = false;

function checkNext(key){
    var returning = "";
    var letter = String.fromCharCode(key);
    console.log(letter);
    for (var i = 0; i < tags.length; i++){
        for (var x = 0; x < tags[i].length; x++){
            if (tags[i][x] == letter){
                returning = returning + "<li>"+tags[i]+"</li>";
            }
        }
        document.getElementById("llist").innerHTML = returning;
    }

}

function keyCode(event) {
    var x = event.keyCode;
    if (active) {
        checkNext(x);

    }
    if (x == 222) {
        active = true;
        console.log(active);
    }
}
