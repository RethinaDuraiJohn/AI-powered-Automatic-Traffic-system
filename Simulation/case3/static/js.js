var i = 0;
$(function() {
    $('a#calculate').bind('click', function() {
      var count = $(this).data("count") || 0;
            $(this).data("count", ++count);
            // $('#wrapper6').append($('#wrapper6').html());
            // $('#wrapper6_1').append($('#wrapper6_1').html());

      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val(),
        c: $('input[name="c"]').val(),
        d: $('input[name="d"]').val(),
        e: $('input[name="e"]').val(),
        f: $('input[name="f"]').val(),
        h: $('input[name="h"]').val(),
        g: count

      }, function(data) {
        // console.log(data);
        $("#result").text(data.c1);
        $("#result1").text(data.c2);
        $("#result2").text(data.c3);
        $("#result3").text(data.c4);
        $("#result4").text(data.c5);
        $("#result5").text(data.c6);

        $("#result6").text(data.g);
        $("#extra").val(data.g);


        activity(data);

        // changelight(1);
      });
      return false;
    });
  });
function activity(res)
{
console.log(res);
if(res.a == 1)
{
  
  change6(4);
  change3(4);
  change2(1);
  change5(1);
  change1(3);
  CheckTime1(res.b);
  CheckTime4(res.b);
  change4(3);
  def1(res.c1);
  mover();
  def4(res.c4);
  movel();
  def6(res.c3);
  moveu1();
  def3(res.c6);
  moved1();
  CheckTime6(res.b);
  CheckTime3(res.b);
  def6add(res.c3);
  moveu1add();
  def3add(res.c6);
  moved1add();



}
if (res.a == 2)
{
  change6(3);
  change3(3);
  change1(1);
  change4(1);
  change5(3);
  change2(3);
  CheckTime2(res.b);
  CheckTime6(res.b);
  CheckTime3(res.b);
  CheckTime5(res.b);
  def5(res.c5);
  moveu();
  def2(res.c2);
  movedn();
  def6(res.c3);
  moveu1();
  def3(res.c6);
  moved1();

}
}

    