/**
 * CrossPaths - Main JavaScript
 * Client-side functionality for culturally adaptive features
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('CrossPaths initialized');
    
    // Get current locale from body class
    const locale = document.body.className.match(/locale-(\w+)/)?.[1] || 'en_IE';
    console.log('Current locale:', locale);
    
    // Initialize features based on locale
    initializeLocaleFeatures(locale);
    
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
            // Ukrainian: Add extra confirmation for actions
            addConfirmationDialogs();
            // Show safety information prominently
            highlightSafetyFeatures();
            break;
            
        case 'pt_BR':
            // Brazilian: Add social interaction animations
            addSocialAnimations();
            // Enable emoji reactions
            enableEmojiReactions();
            break;
            
        case 'en_IE':
        default:
            // Irish/English: Minimal, fast interactions
            enableQuickActions();
            break;
    }
}

/**
 * Add confirmation dialogs for important actions (Ukrainian locale)
 */
function addConfirmationDialogs() {
    const actionButtons = document.querySelectorAll('.btn-primary');
    actionButtons.forEach(button => {
        if (button.textContent.includes('RSVP') || button.textContent.includes('Register')) {
            button.addEventListener('click', function(e) {
                // In production, this would show a proper modal
                console.log('Confirmation dialog for:', button.textContent);
            });
        }
    });
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
    // Add subtle animations to interactive elements
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
 * Enable emoji reactions (Brazilian locale)
 */
function enableEmojiReactions() {
    // Placeholder for emoji reaction feature
    console.log('Emoji reactions enabled');
}

/**
 * Enable quick actions (Irish/English locale)
 */
function enableQuickActions() {
    // Minimize steps for common actions
    console.log('Quick actions enabled');
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
            // Basic validation - can be extended
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
 * Utility: Show notification
 */
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#27ae60' : '#3498db'};
        color: white;
        border-radius: 6px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Utility: Format date based on locale
 */
function formatDate(dateString, locale) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    
    const localeMap = {
        'en_IE': 'en-IE',
        'uk_UA': 'uk-UA',
        'pt_BR': 'pt-BR'
    };
    
    return date.toLocaleDateString(localeMap[locale] || 'en-IE', options);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Export utilities for use in other scripts
window.CrossPaths = {
    showNotification,
    formatDate
};
