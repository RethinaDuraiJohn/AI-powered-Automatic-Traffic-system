    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");

    ctx.rect(0, 0, 200, 300);
    ctx.fillStyle = "#333";
    ctx.fill();

    var colours=["red", "yellow", "green", "black","red yellow"];
    var current=colours[0];
    // var col = 2;

    function offlight() {
      ctx.beginPath();
      ctx.arc(95,50,40,10,12*Math.PI);
      ctx.fillStyle = "black";
      ctx.fill();
      ctx.stroke();
    }
  
    function offlight1() {
      ctx.beginPath();
      ctx.arc(95,150,40,10,12*Math.PI);
      ctx.fillStyle = "black";
      ctx.fill();
      ctx.stroke();
    }
  
    function offlight2() {
      ctx.beginPath();
      ctx.arc(95,250,40,10,12*Math.PI);
      ctx.fillStyle = "black";
      ctx.fill();
      ctx.stroke();
    }
  
    function drawLight1() {
      ctx.beginPath();
      ctx.arc(95,50,40,10,12*Math.PI);
      ctx.fillStyle = "red";
      ctx.fill();
      ctx.stroke();
    }
  
    function drawLight2() {
      ctx.beginPath();
      ctx.arc(95,150,40,10,12*Math.PI);
      ctx.fillStyle = "yellow";
      ctx.fill();
      ctx.stroke();
    }

    function drawLight3() {
      ctx.beginPath();
      ctx.arc(95,250,40,10,12*Math.PI);
      ctx.fillStyle = "green";
      ctx.fill();
      ctx.stroke();
    }

    function changelight(col){

      if (col==0){
        drawLight1();
        offlight1();
        offlight2();
        //++col;
      }
        else if (col==1){
        offlight();
        offlight1();
        drawLight2();
        offlight2();
        //++col;
      } 
      else if (col==2) {
        offlight();
        offlight1();
        drawLight3();
        //++col;
      } 
      

    }

// changelight(1);
  
