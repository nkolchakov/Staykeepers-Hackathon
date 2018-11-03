
// jQuery
const jsonStr = $("#varContainer").data("listing").replace(/\'/g, '"');
var listing = JSON.parse(jsonStr);
console.log(listing)

const { guests = 1, bedroom = 1, beds = 1, baths = 1, lat = 51.5136, lng = 23.3219, address = 'SOHO', landmarks = [], events = [], rating = 5 } = listing;


// rating
const starPercentage = (rating / 5) * 100;
const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
const ratingElement = document.getElementById('rating');
ratingElement.style.width = starPercentageRounded;

// radar chart
const color = 'rgb(153, 102, 255)';
const colorWithAlpha = 'rgba(153, 102, 255, 0.2)';
const labels = ['Guests', 'Bedrooms', 'Beds', 'Baths'];
const datasetData = [guests, bedrooms, beds, baths];
const data = {
  labels,
  datasets: [{
    backgroundColor: colorWithAlpha,
    borderColor: color,
    pointBackgroundColor: color,
    data: datasetData,
  }],
};

const radarChartElement = document.getElementById('radarChart');
const radarChart = new Chart(radarChartElement, {
  type: 'radar',
  data,
  options: {
    scale: {
      pointLabels: {
        fontSize: 20,
      },
      ticks: {
        beginAtZero: true,
        stepSize: 1,
        max: Math.max(...datasetData) + 1,
      },
    },
    legend: {
      display: false,
    },
  }
});

// calendar
const checkIfDateIsUnavailable = (date) => {
  for (let event of events) {
    const eventDate = event.date;
    if (eventDate.year === date.year && eventDate.month === date.month && eventDate.day === date.day) {
      return true;
    }
  }

  return false;
};

$('#calendar').daterangepicker({
  isInvalidDate: (date) => {
    var year = date._d.getUTCFullYear();
    var month = date._d.getUTCMonth() + 1;
    var day = date._d.getUTCDate() + 1;

    return checkIfDateIsUnavailable({
      year,
      month,
      day,
    });
  },
});

// google maps
function initMap() {
  google.maps.Map.prototype.clearActiveInfoWindow = function() {
    if (this.activeInfoWindow) {
      this.activeInfoWindow.close()
    }
  };

  const position = { lat, lng };

  const mapElement = document.getElementById('map');
  const map = new google.maps.Map(mapElement, {
    center: position,
    zoom: 13,
  });

  const addMarkerWithInfoWindow = (markerPosition, infoWindowContent, display) => {
    const marker = new google.maps.Marker({
      position: markerPosition,
      map,
    });

    const infoWindow = new google.maps.InfoWindow({
      content: infoWindowContent,
    });

    if (display) {
      infoWindow.open(map, marker);
      google.maps.Map.prototype.activeInfoWindow = infoWindow;
    }

    marker.addListener('click', function() {
      google.maps.Map.prototype.clearActiveInfoWindow();
      infoWindow.open(map, marker);
      google.maps.Map.prototype.activeInfoWindow = infoWindow;
    });
  }

  addMarkerWithInfoWindow(position, address, true);

  landmarks.map(landmark => addMarkerWithInfoWindow({ lat: landmark.lat, lng: landmark.lng }, landmark.title));
}
