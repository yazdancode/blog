    // Add a confirmation before submitting the form
const form = document.querySelector('form');
form.addEventListener('submit', function (e) {
    const isConfirmed = confirm("Are you sure you want to update the post?");
    if (!isConfirmed) {
        e.preventDefault();  // Prevent form submission if not confirmed
    }
});