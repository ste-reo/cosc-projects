const dropdown = document.querySelector("#dropdown");
const dropdownContent = document.querySelector(".dropdown-content");
dropdown.addEventListener("click", function () {
  if (dropdownContent.style.display === "block") {
    dropdownContent.style.display = "none";
  } else {
    dropdownContent.style.display = "block";
  }
});
