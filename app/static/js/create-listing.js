let mapNotShown = true;

function initMap() {
  const position = { lat: 42.6977, lng: 23.3219 };

  const mapElement = document.getElementById('map');
  const map = new google.maps.Map(mapElement, {
    center: position,
    zoom: 13,
  });

  $('#map').show();
}

$('#newImageBtn').click(function(e) {
  e.preventDefault();

  $('#imagesForm').append('<input type="file" class="form-control-file" id="imageUpload" aria-describedby="fileHelp">');
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
