function initMap(){

  var colors = ['#0000FF', '#FF0000', '#00FF00', '#000088', '#880000', '#008822'];
  var trackers = $('#main-container').data('list');
  var infowindow = []

  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < trackers.length; i++) {
    bounds.extend(new google.maps.LatLng(trackers[i].lat, trackers[i].lon));
  }

  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 13,
    center: {lat: bounds.getCenter().lat(), lng: bounds.getCenter().lng()},
    mapTypeId: 'terrain'
  });

  var geocoder = new google.maps.Geocoder;
  var infowindow = new google.maps.InfoWindow;

  for (var i = trackers[0].group; i <= trackers[trackers.length - 1].group; i++){
    geocodeLatLng(geocoder, map, infowindow);

    var flightPlanCoordinates = [];
    for (var k = 0; k < trackers.length; k++){
      if (trackers[k].group == i){
        flightPlanCoordinates.push({lat: trackers[k].lat, lng: trackers[k].lon});
      }
    }

    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: colors[(i - 1) % colors.length],
      strokeOpacity: 1.0,
      strokeWeight: 2
      }
    );

    flightPath.setMap(map);
  }
}

function geocodeLatLng(geocoder, map, infowindow) {
  var trackers = $('#main-container').data('list');
  var latlng = {lat: trackers[0].lat, lng: trackers[0].lon};
  geocoder.geocode({'location': latlng}, function(results, status) {
    if (status === 'OK') {
      if (results[0]) {
        var marker = new google.maps.Marker({
          position: latlng,
          map: map
        });
        infowindow.setContent(results[0].formatted_address);
        infowindow.open(map, marker);
      } else {
        window.alert('No results found');
      }
    } else {
      window.alert('Geocoder failed due to: ' + status);
    }
  });
}
