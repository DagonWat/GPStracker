function initMap()
{

  var a = $('#main-container').data('list');
  var coords = [];

  for (var i = 0; i < a.length; i++)
  {
    coords.push({lat: a[i].lat, lng: a[i].lon});
  }

  var map = new google.maps.Map(document.getElementById('map'),
  {
    zoom: 15,
    center: coords[0],
    mapTypeId: 'terrain'
  });

  var flightPlanCoordinates = coords;

  var flightPath = new google.maps.Polyline(
    {
    path: flightPlanCoordinates,
    geodesic: true,
    strokeColor: '#0000FF',
    strokeOpacity: 1.0,
    strokeWeight: 2
    }
  );

  flightPath.setMap(map);
}
