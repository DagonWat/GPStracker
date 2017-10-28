function initMap()
{
  var a = $('#main-container').data('list');
  var colors = ['#0000FF', '#FF0000', '#00FF00', '#000088', '#880000', '#008822'];
  var coords = [[]];
  var ways = 0;

  for (var i = 0; i < a.length; i++)
  {
    if (i == 0)
    {
      coords[0].push({lat: a[i].lat, lng: a[i].lon});
    }
    else
    {
      var date1 = new Date(Date.parse(a[i - 1].created_at));
      var date2 = new Date(Date.parse(a[i].created_at));

      var time1 = date1.getHours() * 60 + date1.getMinutes();
      var time2 = date2.getHours() * 60 + date2.getMinutes();

      if (Math.abs(time2 - time1) > 15)
      {
        coords.push([{lat: a[i].lat, lng: a[i].lon}]);
        ways += 1;
      }
      else
      {
        coords[ways].push({lat: a[i].lat, lng: a[i].lon});
      }
    }
  }

  var map = new google.maps.Map(document.getElementById('map'),
  {
    zoom: 15,
    center: coords[0][0],
    mapTypeId: 'terrain'
  });

  var flightPlanCoordinates = coords;

  for (var i = 0; i < ways + 1; i++)
  {
    var flightPath = new google.maps.Polyline(
      {
      path: flightPlanCoordinates[i],
      geodesic: true,
      strokeColor: colors[i % colors.length],
      strokeOpacity: 1.0,
      strokeWeight: 2
      }
    );

    flightPath.setMap(map);
  }
}
