// Page Load Animations
const PageAnimations = {
    init() {
        // Fade in main content
        const mainContent = document.getElementById('main-content');
        if (mainContent) {
            mainContent.style.opacity = '0';
            mainContent.style.transform = 'translateY(10px)';

            requestAnimationFrame(() => {
                mainContent.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                mainContent.style.opacity = '1';
                mainContent.style.transform = 'translateY(0)';
            });
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Page Animations
    PageAnimations.init();

    // Back to Top Button Logic
    const backToTopButton = document.getElementById('back-to-top');

    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopButton.classList.remove('opacity-0', 'invisible');
                backToTopButton.classList.add('opacity-100', 'visible');
            } else {
                backToTopButton.classList.add('opacity-0', 'invisible');
                backToTopButton.classList.remove('opacity-100', 'visible');
            }
        });

        backToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Reading Progress Bar Logic
    const progressBar = document.getElementById('reading-progress');

    if (progressBar) {
        window.addEventListener('scroll', () => {
            const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (window.scrollY / totalHeight) * 100;
            progressBar.style.width = `${progress}%`;
        });
    }
});

// Re-initialize on HTMX content swaps
document.addEventListener('htmx:afterSwap', () => {
    PageAnimations.init();
});
