var i = 0;
$(function() {
    $('a#calculate').bind('click', function() {
      var count = $(this).data("count") || 0;
            $(this).data("count", ++count);
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a1: $('input[name="a1"]').val(),
        a2: $('input[name="a2"]').val(),
        a3: $('input[name="a3"]').val(),
        b1: $('input[name="b1"]').val(),
        b2: $('input[name="b2"]').val(),
        b3: $('input[name="b3"]').val(),
        c1: $('input[name="c1"]').val(),
        c2: $('input[name="c2"]').val(),
        c3: $('input[name="c3"]').val(),
        d1: $('input[name="d1"]').val(),
        d2: $('input[name="d2"]').val(),
        d3: $('input[name="d3"]').val(),
        e: $('input[name="e"]').val(),
        f: count

      }, function(data) {
        // console.log(data);
        $("#result").text(data.a);
        $("#result1").text(data.b);
        $("#result2").text(data.c);
        $("#result3").text(data.d);
        // $("#result4").text(data.b2);
        // $("#result5").text(data.b3);
        // $("#result6").text(data.c1);
        // $("#result7").text(data.c2);
        // $("#result8").text(data.c3);
        // $("#result9").text(data.d1);
        // $("#result10").text(data.d2);
        // $("#result11").text(data.d3);
        $("#result12").text(data.f);

        $("#extra").val(data.f);


        activity(data);

        // changelight(1);
      });
      return false;
    });
  });
function activity(res)
{
console.log(res);
// change1(res.a);
// change2(res.b);
// change3(res.c);
// change4(res.d);
// }
if(res.a==1)
{
  change1(3);
  change2(1);
  change3(1);
  change4(1);
  CheckTime1(res.d);
  def1(res.b);
  mover();
}
if(res.a==2)
{
  change1(1);
  change2(3);
  change3(1);
  change4(1);
  CheckTime2(res.d);
  def2(res.b);
  moved();
}

if(res.a==3)
{
  change1(1);
  change2(1);
  change3(3);
  change4(1);
  CheckTime3(res.d);
  def3(res.b);
  movel();
}
if(res.a==4)
{
  change1(1);
  change2(1);
  change3(1);
  change4(3);
  CheckTime4(res.d);
  def4(res.b);
  moveu();
}

}



    