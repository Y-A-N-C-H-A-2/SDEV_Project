/**
 * CrossPaths - Main JavaScript
 * Client-side functionality for culturally adaptive features
 */

document.addEventListener('DOMContentLoaded', function() {
    // Get current locale from body class
    const locale = document.body.className.match(/locale-(\w+)/)?.[1] || 'en_IE';

    // Initialize features based on locale
    initializeLocaleFeatures(locale);

    // Initialize mobile nav toggle
    initializeMobileNav();

    // Add smooth scrolling for anchor links
    initializeSmoothScrolling();

    // Add form validation
    initializeFormValidation();
});

/**
 * Initialize locale-specific features
 */
function initializeLocaleFeatures(locale) {
    switch(locale) {
        case 'uk_UA':
            // Ukrainian: highlight safety information prominently
            highlightSafetyFeatures();
            break;

        case 'pt_BR':
            // Brazilian: Add social interaction animations
            addSocialAnimations();
            break;

        case 'en_IE':
        default:
            break;
    }
}

/**
 * Highlight safety features (Ukrainian locale)
 */
function highlightSafetyFeatures() {
    const safetyElements = document.querySelectorAll('.verified-badge, .safety-item');
    safetyElements.forEach(element => {
        element.style.transition = 'all 0.3s ease';
    });
}

/**
 * Add social animations (Brazilian locale)
 */
function addSocialAnimations() {
    const cards = document.querySelectorAll('.event-card, .feature-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

/**
 * Initialize mobile navigation toggle
 */
function initializeMobileNav() {
    const toggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (toggle && navLinks) {
        toggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
        });
    }
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#e74c3c';
                } else {
                    field.style.borderColor = '';
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });
}

/**
 * Show/hide checkmark for input fields
 */
document.querySelectorAll('.input_wrapper .form-input').forEach(function(input) {
    var check = input.nextElementSibling;

    function update() {
      if (input.value.trim().length > 0) {
        check.classList.add('visible');
      } else {
        check.classList.remove('visible');
      }
    }

    input.addEventListener('input', update);
    update();
  });
