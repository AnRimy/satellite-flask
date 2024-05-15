document.addEventListener("DOMContentLoaded", function() {
    const filterButton = document.querySelector('.filter-button');
    const blocks = document.querySelectorAll('.small-block');

    filterButton.addEventListener('click', function() {
        const filterValue = this.getAttribute('data-filter');

        blocks.forEach(block => {
            const status = block.getAttribute('data-status');
            if (filterValue === 'active' && status !== 'active') {
                block.style.display = 'none';
            } else {
                block.style.display = 'block';
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.querySelector('.search');
    var satellites = document.querySelectorAll('.small-block');

    searchInput.addEventListener('input', function() {
        var searchText = searchInput.value.trim().toLowerCase();

        satellites.forEach(function(satellite) {
            var satelliteName = satellite.querySelector('h3').textContent.toLowerCase();
            var satelliteStatus = satellite.dataset.status.toLowerCase();

            if (satelliteName.includes(searchText) || satelliteStatus.includes(searchText)) {
                satellite.style.display = 'block';
            } else {
                satellite.style.display = 'none';
            }
        });
    });


});
document.addEventListener('DOMContentLoaded', function() {
    const filterButton = document.querySelector('.filter-button');
    const resetButton = document.querySelector('.reset-button');
    const searchInput = document.querySelector('.search');
    const satelliteBlocks = document.querySelectorAll('.small-block');

    // Фильтрация активных спутников
    filterButton.addEventListener('click', function(event) {
        event.preventDefault();
        satelliteBlocks.forEach(block => {
            if (block.dataset.status !== 'active') {
                block.style.display = 'none';
            } else {
                block.style.display = 'block';
            }
        });
    });

    // Сброс фильтров
    resetButton.addEventListener('click', function(event) {
        event.preventDefault();
        satelliteBlocks.forEach(block => {
            block.style.display = 'block';
        });
        searchInput.value = '';
    });
});
