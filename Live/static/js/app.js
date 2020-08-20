function CheckTime1(total_seconds1) {
    var s1 = total_seconds1;
    console.log(s1);
    if (s1 < 10) {
        document.getElementById("t1").innerHTML = '0' + total_seconds1;

    }
    else {
        document.getElementById("t1").innerHTML = total_seconds1;

    }
    if (s1 <= 0) {
        document.getElementById("t1").innerHTML = "--";
        document.getElementById('g1').style.opacity = 0.3;
        document.getElementById('y1').style.opacity = 1;
        setTimeout("document.getElementById('y1').style.opacity = 0.3;", 7000);
        setTimeout("document.getElementById('r1').style.opacity = 1;", 7000);
        document.getElementById("submit5").click();

    }
    else {
        s1 = s1 - 1;
        g1 = parseInt(s1);
        console.log(s1);
        setTimeout("CheckTime1(g1)", 1000);
    }
}

function CheckTime2(total_seconds1) {
    var s1 = total_seconds1;
    console.log(s1);
    if (s1 < 10) {
        document.getElementById("t2").innerHTML = '0' + total_seconds1;

    }
    else {
        document.getElementById("t2").innerHTML = total_seconds1;

    }
    if (s1 <= 0) {
        document.getElementById("t2").innerHTML = "--";
        document.getElementById('g2').style.opacity = 0.3;
        document.getElementById('y2').style.opacity = 1;
        setTimeout("document.getElementById('y2').style.opacity = 0.3;", 7000);
        setTimeout("document.getElementById('r2').style.opacity = 1;;", 7000);
        document.getElementById("submit5").click();

    }
    else {
        s1 = s1 - 1;
        g1 = parseInt(s1);
        console.log(s1);
        setTimeout("CheckTime2(g1)", 1000);
    }
}

function CheckTime3(total_seconds1) {
    var s1 = total_seconds1;
    console.log(s1);
    if (s1 < 10) {
        document.getElementById("t3").innerHTML = '0' + total_seconds1;

    }
    else {
        document.getElementById("t3").innerHTML = total_seconds1;

    }

    if (s1 <= 0) {
        document.getElementById("t3").innerHTML = "--";
        document.getElementById('g3').style.opacity = 0.3;
        document.getElementById('y3').style.opacity = 1;
        setTimeout("document.getElementById('y3').style.opacity = 0.3;", 7000);
        setTimeout("document.getElementById('r3').style.opacity = 1;", 7000);
        document.getElementById("submit5").click();

    }
    else {
        s1 = s1 - 1;
        g1 = parseInt(s1);
        console.log(s1);
        setTimeout("CheckTime3(g1)", 1000);
    }
}
 function CheckTime4(total_seconds1) {
    var s1 = total_seconds1;
    console.log(s1);
    if (s1 < 10) {
        document.getElementById("t4").innerHTML = '0' + total_seconds1;

    }
    else {
        document.getElementById("t4").innerHTML = total_seconds1;

    }

    if (s1 <= 0) {
        document.getElementById("t4").innerHTML = "--";
        document.getElementById('g4').style.opacity = 0.3;
        document.getElementById('y4').style.opacity = 1;
        setTimeout("document.getElementById('y4').style.opacity = 0.3;", 7000);
        setTimeout("document.getElementById('r4').style.opacity = 1;", 7000);
        document.getElementById("submit5").click();
        }
    else {
        s1 = s1 - 1;
        g1 = parseInt(s1);
        console.log(s1);
        setTimeout("CheckTime4(g1)", 1000);
    }
}


function pass(s1) {
    document.getElementById("myVideo1").pause();
    document.getElementById("myVideo2").pause();
    document.getElementById("myVideo3").pause();
    document.getElementById("myVideo4").pause();
    document.getElementById(s1).play();

}

function setClr() {
    document.getElementById('g1').style.opacity = 0.3;
    document.getElementById('g2').style.opacity = 0.3;
    document.getElementById('g3').style.opacity = 0.3;
    document.getElementById('g4').style.opacity = 0.3;

    document.getElementById('r1').style.opacity = 1;
    document.getElementById('r2').style.opacity = 1;
    document.getElementById('r3').style.opacity = 1;
    document.getElementById('r4').style.opacity = 1;

    // CheckTime1(0);
    // CheckTime2(0);
    // CheckTime3(0);
    // CheckTime4(0);
}


function setLight(data) {
    setClr();
    active = data['a']
    if (active == 1) {
        document.getElementById('g1').style.opacity = 1;
        document.getElementById('r1').style.opacity = 0.3;
        CheckTime1( data['d']);
        pass("myVideo1");
    }
    else if (active == 2) {
        document.getElementById('g2').style.opacity = 1;
        document.getElementById('r2').style.opacity = 0.3;
        CheckTime2( data['d']);
        pass("myVideo2");

    }
    else if (active == 3) {
        document.getElementById('g3').style.opacity = 1;
        document.getElementById('r3').style.opacity = 0.3;
        CheckTime3( data['d']);
        pass("myVideo3");

    }
    else if (active == 4) {
        document.getElementById('g4').style.opacity = 1;
        document.getElementById('r4').style.opacity = 0.3;
        CheckTime4( data['d']);
        pass("myVideo4");


    }
}


$(function () {
    $('#submit1').click(function () {
        event.preventDefault();
        var form_data = new FormData($('#uploadform1')[0]);
        form_data.append("name", "vid1");
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function (data, textStatus, jqXHR) {
            console.log('Success!');
            document.getElementById('uploadform1').style.display = 'none';
            $("#one1").append("<video id=myVideo1 width=100 height=100 autoplay loop muted > <source src=/file/" + data['name'] + " type=video/mp4>  </video>");
        }).fail(function (data) {
            alert('error!');
        });
    });


    $('#submit2').click(function () {
        event.preventDefault();
        var form_data = new FormData($('#uploadform2')[0]);
        form_data.append("name", "vid2");
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function (data, textStatus, jqXHR) {
            console.log('Success!');
            document.getElementById('uploadform2').style.display = 'none';
            $("#one2").append("<video id=myVideo2  width=100 height=100 autoplay loop muted  > <source src=/file/" + data['name'] + " type=video/mp4>  </video>");
        }).fail(function (data) {
            alert('error!');
        });
    });



    $('#submit3').click(function () {
        event.preventDefault();
        var form_data = new FormData($('#uploadform3')[0]);
        form_data.append("name", "vid3");
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function (data, textStatus, jqXHR) {
            console.log('Success!');
            document.getElementById('uploadform3').style.display = 'none';
            $("#one3").append("<video id=myVideo3 width=100 height=100 autoplay loop muted  > <source src=/file/" + data['name'] + " type=video/mp4>  </video>");
        }).fail(function (data) {
            alert('error!');
        });
    });




    $('#submit4').click(function () {
        event.preventDefault();
        var form_data = new FormData($('#uploadform4')[0]);
        form_data.append("name", "vid4");
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function (data, textStatus, jqXHR) {
            console.log('Success!');
            document.getElementById('uploadform4').style.display = 'none';
            $("#one4").append("<video id=myVideo4 width=100 height=100 autoplay loop muted  > <source src=/file/" + data['name'] + " type=video/mp4>  </video>");
        }).fail(function (data) {
            alert('error!');
        });
    });


    $('#submit5').click(function () {
        event.preventDefault();
        var form_data = new FormData();
        form_data.append("v1", document.getElementById("myVideo1").currentTime);
        form_data.append("v2", document.getElementById("myVideo2").currentTime);
        form_data.append("v3", document.getElementById("myVideo3").currentTime);
        form_data.append("v4", document.getElementById("myVideo4").currentTime);
        form_data.append("v1e", document.getElementById("myVideo1").duration);
        form_data.append("v2e", document.getElementById("myVideo2").duration);
        form_data.append("v3e", document.getElementById("myVideo3").duration);
        form_data.append("v4e", document.getElementById("myVideo4").duration);
        $.ajax({
            type: 'POST',
            url: '/getdata',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function (data, textStatus, jqXHR) {
            setLight(data['data']);
            console.log(data['data']['a'])
            console.log(data);
            document.getElementById("delme").outerHTML = "";

            $('#reso').append( "<tbody id=delme>  </tbody>");
            $('#delme').append("<tr><td>1</td> <td>"+data['data']['res'][0][0]+"</td> <td>"+data['data']['res'][0][1]+"</td> <td>" +data['data']['res'][0][2]+"</td></tr>")
            $('#delme').append("<tr><td>2</td> <td>"+data['data']['res'][1][0]+"</td> <td>"+data['data']['res'][1][1]+"</td> <td>" +data['data']['res'][1][2]+"</td></tr>")
            $('#delme').append("<tr><td>3</td> <td>"+data['data']['res'][2][0]+"</td> <td>"+data['data']['res'][2][1]+"</td> <td>" +data['data']['res'][2][2]+"</td></tr>")
            $('#delme').append("<tr><td>4</td> <td>"+data['data']['res'][3][0]+"</td> <td>"+data['data']['res'][3][1]+"</td> <td>" +data['data']['res'][3][2]+"</td></tr>")
            
            console.log('Success!');
        }).fail(function (data) {
            alert('error!');
        });
    });



});



// Setting Variables
var allLights = document.getElementsByClassName("light")
var yellowID = document.getElementById('yellow');
var greenID = document.getElementById('green');
var redID = document.getElementById('red');


// Adding click event listeners to each traffic light color id
for (var i = 0; i < allLights.length; i++) {
    allLights[i].addEventListener("click", displayLight);
}

// This function turns off current light (all lights) and turns on only the selected light
function displayLight(e) {
    lightsOff();

    if (e.target.id === 'red') {

        console.log('red clicked');
        redID.classList.add('light-visible');

    } else if (e.target.id === 'yellow') {

        console.log('yellow clicked');
        yellowID.classList.add('light-visible');

    } else {

        console.log('green clicked');
        greenID.classList.add('light-visible');
    }
}

// Helper function to turn off lights
function lightsOff() {
    for (var i = 0; i < allLights.length; i++) {
        allLights[i].classList.remove("light-visible");
    }
}
