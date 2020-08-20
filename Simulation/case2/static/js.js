var i = 0;
$(function() {
    $('a#calculate').bind('click', function() {
      var count = $(this).data("count") || 0;
            $(this).data("count", ++count);
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val(),
        c: $('input[name="c"]').val(),
        d: $('input[name="d"]').val(),
        e: $('input[name="e"]').val(),
        f: count

      }, function(data) {
        // console.log(data);
        $("#result").text(data.a);
        $("#result1").text(data.b);
        $("#result2").text(data.c);
        $("#result3").text(data.d);
        $("#result4").text(data.f);
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
  change2(3);
  change3(1);
  change4(1);
  CheckTime1(res.d);
  CheckTime2(res.d);
  def1(res.b);
  mover();
  def2(res.g);
  moved();
}
if(res.a==2)
{
  change1(1);
  change2(5);
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
  change2(3);
  change3(1);
  change4(3);
  CheckTime4(res.d);
  CheckTime2(res.d);
  def4(res.b);
  moveu();
  def2(res.g);
  moved();
}

}



    