/* myblog/static/myblog/js/list.js */
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll to top when changing pages
    document.querySelectorAll('.pagination-container a').forEach(link => {
        link.addEventListener('click', function(e) {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });

    // Add hover effects for post items
    document.querySelectorAll('.post-item').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });

        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    });

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
            const email = this.getAttribute('href').replace('mailto:', '');
            navigator.clipboard.writeText(email).then(() => {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check"></i> ایمیل کپی شد';
                setTimeout(() => {
                    this.innerHTML = originalText;
                }, 2000);
            });
        });
    });
});