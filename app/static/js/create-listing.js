let mapNotShown = true;
let marker;

function initMap() {
  const position = { lat: 42.6977, lng: 23.3219 };

  const mapElement = document.getElementById('map');
  const map = new google.maps.Map(mapElement, {
    center: position,
    zoom: 13,
  });

  function placeMarker(location) {
    if (marker) {
      marker.setMap(null);
    }
    marker = new google.maps.Marker({
      position: location,
      map: map,
      animation: google.maps.Animation.DROP,
    });
  }

  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng);

    latToSend = event.latLng.lat();
    document.getElementById('lat').value = latToSend;
    lngToSend = event.latLng.lng();
    document.getElementById('lng').value = lngToSend;
  });

  $('#map').show();
}

$('#newImageBtn').click(function(e) {
  e.preventDefault();

  $('#imagesForm').append('<input type="file" class="form-control-file" id="imageUpload" aria-describedby="fileHelp" name="image">');
});

$('#newAmenityBtn').click(function(e) {
  e.preventDefault();

  $('#amenitiesForm').append('<div><input class="form-control" type="text" placeholder="Amenity" id="amenities" name="amenities"></div>');
});

$('#selectLocation').click(function(e) {
  e.preventDefault();

  if (mapNotShown) {
    initMap();
    mapNotShown = false;
  }
});

$('#listingForm').ajaxForm(function() {
  window.location.href = "/test";
});
