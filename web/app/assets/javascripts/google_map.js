function initMap(){

  var colors = ['#0000FF', '#FF0000', '#00FF00', '#000088', '#880000', '#008822'];
  var trackers = $('#main-container').data('list');

  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 15,
    center: {lat: trackers[0][0].lat, lng: trackers[0][0].lon},
    mapTypeId: 'terrain'
  });

  for (var i = 0; i < trackers.length; i++){
    var flightPlanCoordinates = [];

    for (var k = 0; k < trackers[i].length; k++){
      flightPlanCoordinates.push({lat: trackers[i][k].lat, lng: trackers[i][k].lon});
    }

    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: colors[i % colors.length],
      strokeOpacity: 1.0,
      strokeWeight: 2
      }
    );


    flightPath.setMap(map);
  }
}
