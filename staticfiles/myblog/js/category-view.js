document.addEventListener('DOMContentLoaded', function() {
    // Confirm delete action
    document.querySelectorAll('a[href*="delete_post"]').forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('آیا از حذف این پست اطمینان دارید؟')) {
                e.preventDefault();
            }
        });
    });

    // Copy email to clipboard
    document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const email = this.textContent;
            navigator.clipboard.writeText(email).then(() => {
                const originalText = this.textContent;
                this.textContent = 'ایمیل کپی شد!';
                this.parentElement.style.animation = 'highlight 1s ease';

                setTimeout(() => {
                    this.textContent = originalText;
                }, 2000);
            });
        });
    });

    // Lazy loading for post content
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        });

        document.querySelectorAll('.post-item').forEach(post => {
            observer.observe(post);
        });
    }
});