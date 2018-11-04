const jsonStr = $("#varContainer").data("listings").replace(/\'/g, '"');
const listings = JSON.parse(jsonStr);

$("#myCarousel").on('slide.bs.carousel', function(e) {
  const $e = $(e.relatedTarget);
  const idx = $e.index();
  const itemsPerSlide = 3;
  const totalItems = $(".carousel-item").length;

  if (idx >= totalItems - (itemsPerSlide - 1)) {
    const it = itemsPerSlide - (totalItems - idx);
    for (let i = 0; i < it; i++) {
      // append slides to end
      if (e.direction == "left") {
        $(".carousel-item")
          .eq(i)
          .appendTo(".carousel-inner");
      } else {
        $(".carousel-item")
          .eq(0)
          .appendTo($(this).find(".carousel-inner"));
      }
    }
  }
});

listings.forEach((listing, index) => {
  const starPercentage = (listing.rating / 5) * 100;
  const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
  const ratingElement = document.getElementById(`rating${index + 1}`);
  ratingElement.style.width = starPercentageRounded;
});
