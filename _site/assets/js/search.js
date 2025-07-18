window.onload = function () {
    var $searchbar = document.getElementById('searchbar');
    var $searchResults = document.getElementById('search-results');

    if (!$searchbar || !$searchResults)
        return;

    SimpleJekyllSearch({
        searchInput: $searchbar,
        resultsContainer: $searchResults,
        json: '/techlee/search.json',
        searchResultTemplate: '<a href="{url}" target="_blank">{title}</a>',
        noResultsText: ''
    });

    /* hack ios safari unfocus */
    if (/Safari/.test(navigator.userAgent) && !/Chrome/.test(navigator.userAgent))
        document.body.firstElementChild.tabIndex = 1;

    var $labelGroup = document.querySelector(".posts-labelgroup");
    var $postLabel = document.getElementById("posts-label");
    var labelWidth = $postLabel.scrollWidth;

    $postLabel.style.width = labelWidth + "px";

    $labelGroup.addEventListener("click", function (e) {
        $searchResults.style.display = null;
        $postLabel.style.width = "0";
        $labelGroup.setAttribute("class", "posts-labelgroup focus-within");
        $searchbar.focus();
        e.stopPropagation();
    }, false);

    $labelGroup.addEventListener("mouseleave", function () {
        document.body.onclick = searchCollapse;
    });

    var searchCollapse = function (e) {
        $searchResults.style.display = "none";
        $labelGroup.setAttribute("class", "posts-labelgroup");
        $postLabel.style.width = labelWidth + "px";
        document.body.onclick = null;
    };
}

