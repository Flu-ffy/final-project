document.getElementById("educationButton").addEventListener("click", function() {
    var form = document.getElementById("educationForm");
    if (form.style.display === "block") {
        form.style.display = "none";
    } else {
        form.style.display = "block";
    }
});
function showCourseInput() {
    var educationLevel = document.getElementById("education-level").value;
    var courseInputGroup = document.getElementById("course-input-group");
    if (educationLevel) {
        courseInputGroup.style.display = "block";
    } else {
        courseInputGroup.style.display = "none";
    }
}
function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
        }
        
        window.onclick = function(event) {
            if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            var i;
            for (i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
                }
            }
            }
        }

// js code that enables to diplay the course pursued section once the level of the course is choosen
    