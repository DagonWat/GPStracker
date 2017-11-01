var display = function()
{
  var a = $('#main-container').data('way');
  var distance = 0;

  for (var i = 0; i < a.length - 1; i++)
  {
    distance += Math.sqrt(Math.pow((a[i].lon - a[i + 1].lon) * 111.13486111, 2) + Math.pow((a[i].lat - a[i + 1].lat) * 71.2403572324, 2));
  }

  document.getElementById("number").innerHTML = "Today you walked " + Math.floor(distance) + "km appr.";
}

$(document).ready(display);
