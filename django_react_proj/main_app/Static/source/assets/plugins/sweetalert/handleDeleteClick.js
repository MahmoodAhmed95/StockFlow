// Add an event listener to elements with the 'confirm-text' class
$(".confirm-text").on("click", function () {
  // Call the 'handleDeleteClick' function passing the clicked element as an argument
  handleDeleteClick(this);
});

function handleDeleteClick(element) {
  const itemType = $(element).data("item-type");
  const itemId = $(element).data("item-id");

  Swal.fire({
    title: "Are you fffffffsure?",
    text: "You won't be fffffffffable to revert this!",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, delete it!",
    cancelButtonText: "Cancel",
    confirmButtonClass: "btn btn-primary",
    cancelButtonClass: "btn btn-danger ml-1",
    buttonsStyling: false,
  }).then(function (result) {
    if (result.isConfirmed) {
      // Make an AJAX request to delete the item
      $.ajax({
        type: "POST", // or "DELETE" depending on your backend API
        url: `/${itemType}/${itemId}/delete/`,
        data: {
          // Include any additional data needed for the delete operation
        },
        success: function (response) {
          Swal.fire({
            type: "success",
            title: "Deleted!",
            text: "Your item has been deleted.",
            confirmButtonClass: "btn btn-success",
          }).then(function () {
            // Optionally, you can redirect to a specific URL after successful deletion
            window.location.href = response.redirect_url;
          });
        },
        error: function (error) {
          Swal.fire({
            type: "error",
            title: "Error",
            text: "An error occurred while deleting the item.",
            confirmButtonClass: "btn btn-danger",
          });
        },
      });
    }
  });
}
