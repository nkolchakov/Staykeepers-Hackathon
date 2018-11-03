// const listing = '{{ listing }}';
const listing = {
  guests: 5,
  bedrooms: 3,
  beds: 4,
  baths: 2,
  lat: 42.6977,
  lng: 23.3219,
  address: 'Random Address, Sofia, Bulgaria',
  landmarks: [{
    title: 'Sveta Sofia',
    lat: 42.696522,
    lng: 23.331367,
  }, {
    title: 'Aleksandar Nevski',
    lat: 42.695808,
    lng: 23.332794,
  }],
  events: [{
    title: 'RIP',
    date: {
      year: 2018,
      month: 10,
      day: 2,
    }
  }, {
    title: 'Hello World',
    date: {
      year: 2018,
      month: 10,
      day: 11,
    }
  }],
  rating: 3.5,
}; // TEMP
const { guests, bedrooms, beds, baths, lat, lng, address, landmarks, events, rating } = listing;

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
const calendarElement = document.getElementById('caleandar');
const calendarEvents = events.map(event => ({
  Date: new Date(event.date.year, event.date.month, event.date.day),
  Title: event.title,
}));
caleandar(calendarElement, calendarEvents);

// google maps
function initMap() {
  const position = { lat, lng };

  const mapElement = document.getElementById('map');
  const map = new google.maps.Map(mapElement, {
    center: position,
    zoom: 13,
  });

  const marker = new google.maps.Marker({
    position,
    map,
    title: address,
  });

  const landmarkMarkers = landmarks.map(landmark => new google.maps.Marker({
    position: { lat: landmark.lat, lng: landmark.lng },
    map,
    title: landmark.title,
  }));
}
