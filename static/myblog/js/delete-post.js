document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-group');
    const deleteButton = form?.querySelector('.btn-secondary');
    let confirmationStep = false;

    if (form && deleteButton) {
        // Add double confirmation
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            if (!confirmationStep) {
                // First click
                deleteButton.textContent = 'Click again to confirm';
                deleteButton.classList.add('confirming');
                confirmationStep = true;

                // Reset after 3 seconds if not clicked
                setTimeout(() => {
                    if (confirmationStep) {
                        deleteButton.textContent = 'Delete';
                        deleteButton.classList.remove('confirming');
                        confirmationStep = false;
                    }
                }, 3000);
            } else {
                // Second click - proceed with deletion
                form.submit();
            }
        });

        // Add cancel button
        const cancelLink = document.createElement('a');
        cancelLink.href = 'javascript:history.back()';
        cancelLink.className = 'cancel-link';
        cancelLink.textContent = 'Cancel';
        form.appendChild(cancelLink);

        // Add alert animation to form container
        const formLabel = document.querySelector('.form-label');
        formLabel.classList.add('alert');
    }

    // Add warning icon
    const heading = document.querySelector('h1');
    if (heading) {
        heading.innerHTML = '⚠️ ' + heading.innerHTML;
    }
});