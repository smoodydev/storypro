var active = 0;
var stringer = "";

function checkString(stringer){
    console.log(stringer);

}


function keyCode(){
    var x = event.keyCode;
    if (x == 222) {
        active = active+1;
        console.log(active);
    }
    else if (active == 1){
        stringer = stringer + String.fromCharCode(x);
        console.log("Checking 1");
        checkString(stringer);
    
    }
    else if (active == 2){
        console.log("Checking 2")
    }
    else{
        console.log("Nothing Here");
    }
}






// Register # marks and work on the next Steps
// 